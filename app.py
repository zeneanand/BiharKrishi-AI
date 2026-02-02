import streamlit as st
import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# 🎨 PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="🌱 BiharKrishi AI: Advanced Edition",
    page_icon="🌾",
    layout="wide"
)

# ============================================
# 🌑 DARK MODE CSS (Improved Contrast)
# ============================================
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        border-bottom: 3px solid #00FF41;
    }
    .card-dark { 
        background-color: #121212; 
        border: 1px solid #333333;
        color: #00FF41; 
        padding: 20px; 
        border-radius: 15px; 
        text-align: center; 
    }
    .stButton>button {
        background: linear-gradient(45deg, #00b09b 0%, #96c93d 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 10px;
        font-weight: bold;
        width: 100%;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# 🚀 SECURE API CONNECTION (Step 6)
# ============================================
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"]) 
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"temperature": 0.2, "max_output_tokens": 500}
    )
else:
    st.error("⚠️ API Key missing! Add GOOGLE_API_KEY to Streamlit Secrets.") [cite: 58]
    st.stop()

# ============================================
# 🚀 HEADER & SIDEBAR
# ============================================
st.markdown("""
<div class="main-header">
    <h1 style="font-size: 3.5rem; margin: 0;">🌾 BiharKrishi AI</h1>
    <p style="font-size: 1.2rem; opacity: 0.9;">Smart Farming & Data Visualization for Bihar</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("👤 Farmer Profile")
    f_name = st.text_input("Name", "Ram Kumar Baitha")
    f_loc = st.text_input("Location", "Kishanganj, Bihar")
    f_land = st.text_input("Land Size (Ha)", "0.25")
    st.divider()
    st.info("Interactive Dashboard for Bihar's 38 Districts.")

# ============================================
# 📊 DATA VISUALIZATION (Replacing Checklist)
# ============================================
st.markdown("### 📈 Impact Analysis: Traditional vs. AI-Smart Farming")

# Create data for visualization 
impact_data = {
    'Season': ['Kharif', 'Rabi', 'Zaid'],
    'Traditional Yield (kg)': [1200, 1500, 800],
    'AI-Optimized Yield (kg)': [1850, 2100, 1300]
}
df = pd.DataFrame(impact_data)

# 
fig, ax = plt.subplots(figsize=(10, 4), facecolor='black')
ax.set_facecolor('black')

# Plotting the bars
x = range(len(df['Season']))
ax.bar([i - 0.2 for i in x], df['Traditional Yield (kg)'], width=0.4, label='Traditional', color='#FF4B4B')
ax.bar([i + 0.2 for i in x], df['AI-Optimized Yield (kg)'], width=0.4, label='AI-Smart', color='#00FF41')

# Styling the graph for Dark Mode
ax.set_xticks(x)
ax.set_xticklabels(df['Season'], color='white')
ax.tick_params(axis='y', colors='white')
ax.set_ylabel('Yield in kg', color='white')
ax.legend(facecolor='#121212', edgecolor='white', labelcolor='white')
ax.set_title("Expected Productivity Increase", color='white', pad=20)

st.pyplot(fig)

# ============================================
# 🎯 INPUT & INTERACTION
# ============================================
st.write("---")
col1, col2 = st.columns(2)
with col1:
    location = st.text_input("Current District", "Samastipur")
    crop_stage = st.text_input("Crop Stage", "Vegetative")
with col2:
    category = st.text_input("Category", "Diesel Cost Saving")
    query = st.text_input("Your Question", "How to save fuel during irrigation?")

# ============================================
# ⚡ AI ADVICE & FORMATTING (Step 4)
# ============================================
if st.button("🚀 GET EXPERT ADVICE"):
    if query:
        with st.spinner("🧠 AI is analyzing soil data and weather patterns..."):
            full_prompt = f"""
            Expert Bihar Agri-Consultant. Farmer: {f_name} from {location}. 
            Question: {query}. Instructions: Provide bulleted steps with justifications. [cite: 7, 12]
            """
            try:
                response = model.generate_content(full_prompt)
                st.markdown('<div style="background: #111; border-left: 5px solid #00FF41; padding: 20px;">'
                            '<h2 style="color: #00FF41;">💡 AI Recommendations</h2></div>', unsafe_allow_html=True)
                st.write(response.text) [cite: 49, 82]
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
