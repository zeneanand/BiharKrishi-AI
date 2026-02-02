import streamlit as st
import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# 🎨 PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="🌱 AgroNova: Multi-State Smart Assistant",
    page_icon="🌾",
    layout="wide"
)

# ============================================
# 🌑 VIBRANT DARK UI (Design & Implementation)
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
# 🚀 HEADER & STATE SELECTION
# ============================================
st.markdown("""
<div class="main-header">
    <h1 style="margin:0;">🌾 AgroNova Smart Assistant</h1>
    <p style="font-size:1.2rem;">Serving Farmers across Bihar and Gujarat (Saurashtra)</p>
</div>
""", unsafe_allow_html=True)

# State Selection determines the User Persona and Context
selected_state = st.selectbox("🌍 Select Your State:", ["Bihar", "Gujarat (Saurashtra)"])

# ============================================
# 👤 DYNAMIC PERSONA LOADER (Saurashtra & Bihar)
# ============================================
if selected_state == "Bihar":
    persona = {"name": "Ram Kumar Baitha", "loc": "Kishanganj", "size": "0.25 Ha", "focus": "Marginal Farming"}
    districts = ["Samastipur", "Kishanganj", "Gaya", "Saharsa", "Muzaffarpur"]
    crops = ["Rice", "Wheat", "Maize", "Litchi"]
else:
    # Data from Saurashtra Storyboard [cite: 95, 106, 107]
    persona = {"name": "Mansukhbhai Patel", "loc": "Gondal, Rajkot", "size": "4 Acres", "focus": "Medium-scale"}
    districts = ["Rajkot", "Jamnagar", "Amreli", "Junagadh", "Porbandar"]
    crops = ["Groundnut (Kharif)", "Cumin/Jeera (Rabi)", "Cotton"]

with st.sidebar:
    st.title("👤 Current Farmer Persona")
    st.success(f"**Name:** {persona['name']}")
    st.info(f"**Location:** {persona['loc']}\n\n**Land:** {persona['size']}")
    st.write(f"**Focus:** {persona['focus']}")
    st.divider()
    st.markdown("### 📋 Validation Checklist")
    st.checkbox("Region-Specific", value=True)
    st.checkbox("Logical Reasoning", value=True)
    st.checkbox("Simple Language", value=True)

# ============================================
# 🎯 INPUT INTERACTION
# ============================================
col1, col2 = st.columns(2)
with col1:
    district = st.selectbox(f"Select {selected_state} District:", districts)
    crop = st.selectbox("Select Crop:", crops)

with col2:
    category = st.selectbox("Help Category:", ["Pest Management", "Sowing & Weather", "Water/Subsidies", "Soil Health"])
    user_query = st.text_input("Ask a specific question:", placeholder="e.g., Treatment for White Grub?")

# ============================================
# ⚡ AI ADVICE & FORMATTING (Step 4)
# ============================================
if st.button("🚀 GET LOCALIZED ADVICE"):
    with st.spinner(f"🧠 Consulting {selected_state} Agricultural Data..."):
        # Combining persona data with state-specific research [cite: 104, 111, 122]
        context_prompt = f"""
        Role: Expert Agricultural Consultant for {selected_state}, India.
        Persona: {persona['name']} from {persona['loc']}. 
        Research Context for {selected_state}:
        - If Gujarat: Use JAU standards, White Grub/Pink Bollworm info, and GGRC subsidy details.
        - If Bihar: Use BAMETI and NABARD State Focus Paper data for floods/diesel costs.
        
        Current Query: {user_query} regarding {crop} at {district}.
        
        Instructions (FA-2 Requirement):
        1. Clean and format Gemini's output into a bulleted list[cite: 4, 10, 11].
        2. Provide a 'Why' justification for every suggestion to build trust[cite: 7, 12].
        3. Use simple, non-technical language[cite: 36].
        """
        
        try:
            response = model.generate_content(context_prompt)
            st.markdown(f"### 💡 Expert Advice for {selected_state}")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

# ============================================
# 📊 REGIONAL DATA VISUALIZATION
# ============================================
st.write("---")
st.markdown(f"### 📈 Productivity Growth: {selected_state}")

# Grouped bar chart showing yield potential with AI [cite: 60, 85]
impact_data = {
    'Crop': crops[:3],
    'Traditional Yield': [1200, 1500, 900],
    'AI-Smart Yield': [1800, 2100, 1400]
}
df = pd.DataFrame(impact_data)

fig, ax = plt.subplots(figsize=(10, 4), facecolor='#050a0e')
ax.set_facecolor('#050a0e')
x = range(len(df['Crop']))
ax.bar([i - 0.2 for i in x], df['Traditional Yield'], width=0.4, label='Traditional', color='#ff4b2b')
ax.bar([i + 0.2 for i in x], df['AI-Smart Yield'], width=0.4, label='AI-Smart', color='#00f260')

ax.set_xticks(x)
ax.set_xticklabels(df['Crop'], color='white')
ax.tick_params(colors='white')
ax.legend()
st.pyplot(fig)
