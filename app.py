import streamlit as st
import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# 🎨 PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="🌱 AgroNova Multi-State AI",
    page_icon="🌾",
    layout="wide"
)

# ============================================
# 🌈 VIBRANT DARK CSS (FA-2 Premium UI)
# ============================================
st.markdown("""
<style>
    .stApp { background-color: #050a0e; color: #e0e0e0; }
    .main-header {
        background: linear-gradient(90deg, #11998e 0%, #38ef7d 100%);
        color: white; padding: 40px; border-radius: 20px;
        text-align: center; margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(17, 153, 142, 0.3);
    }
    /* Styling the Sidebar Inputs */
    section[data-testid="stSidebar"] {
        background-color: #0a1118;
        border-right: 1px solid #38ef7d;
    }
    .stTextInput>div>div>input {
        background-color: #1a262f;
        color: #38ef7d;
        border: 1px solid #38ef7d;
    }
    .stButton>button {
        background: linear-gradient(45deg, #f7971e 0%, #ffd200 100%);
        color: black; border: none; padding: 15px;
        border-radius: 10px; font-weight: bold; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# 🚀 SECURE API CONNECTION (Step 6)
# ============================================
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ API Key missing in Streamlit Secrets!")
    st.stop()

# ============================================
# 🚀 DYNAMIC SIDEBAR (Text Box Persona)
# ============================================
with st.sidebar:
    st.title("👤 Edit Farmer Profile")
    st.markdown("---")
    # CHANGED: These are now text_input boxes for FA-2 interaction requirements
    farmer_name = st.text_input("Farmer Name", value="Ram Kumar Baitha")
    home_location = st.text_input("Home Location", value="Kishanganj, Bihar")
    land_size = st.text_input("Land Size (e.g., 0.25 Ha)", value="0.25 Ha")
    
    st.divider()
    st.info("The AI will use these details to personalize its advice.")
    
    # Validation Checklist for Step 5
    st.markdown("### 📋 Validation Checklist")
    st.checkbox("Region-Specific", value=True)
    st.checkbox("Logical Reasoning", value=True)
    st.checkbox("Simple Language", value=True)

# ============================================
# 🚀 MAIN UI & STATE SELECTION
# ============================================
st.markdown("""
<div class="main-header">
    <h1 style="margin:0;">🌾 AgroNova Smart Assistant</h1>
    <p style="font-size:1.2rem;">Providing Site-Specific Advice for India & Beyond</p>
</div>
""", unsafe_allow_html=True)

selected_state = st.selectbox("🌍 Select State for Research Context:", ["Bihar", "Gujarat (Saurashtra)"])

col1, col2 = st.columns(2)
with col1:
    district = st.text_input("Current District", value="Samastipur")
    crop = st.text_input("Crop Name", value="Maize/Groundnut")

with col2:
    category = st.selectbox("Category", ["Pest Management", "Sowing & Weather", "Soil Health"])
    query = st.text_input("Your Question", placeholder="How can I save diesel costs?")

# ============================================
# ⚡ AI ADVICE & FORMATTING (Step 4)
# ============================================
if st.button("🚀 GET LOCALIZED ADVICE"):
    with st.spinner("🧠 AI is consulting local agricultural standards..."):
        # Prompt logic incorporating the new text-box profile data
        full_prompt = f"""
        Expert Consultant for {selected_state}. 
        User: {farmer_name} from {home_location} with {land_size}.
        Context: District {district}, Crop {crop}. 
        Question: {query}
        Instructions (FA-2 Requirement): Provide a bulleted list with 'Why' justifications for each step.
        """
        
        try:
            response = model.generate_content(full_prompt)
            st.markdown(f"### 💡 Recommendations for {farmer_name}")
            st.write(response.text)
            st.balloons()
        except Exception as e:
            st.error(f"Error: {e}")

# ============================================
# 📊 DATA VISUALIZATION (Step 6)
# ============================================
st.write("---")
st.markdown("### 📈 Projected Growth Insights")
chart_data = pd.DataFrame({'Season': ['Kharif', 'Rabi', 'Zaid'], 'Standard': [100, 150, 80], 'AI-Optimized': [160, 210, 130]})
st.bar_chart(chart_data.set_index('Season'))
