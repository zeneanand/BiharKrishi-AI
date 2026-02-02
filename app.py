import streamlit as st
import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# 🎨 PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="🌱 BiharKrishi AI: Dark Edition",
    page_icon="🌾",
    layout="wide"
)

# ============================================
# 🌑 DARK MODE CSS (Design & Implementation)
# ============================================
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    .main-header {
        background: linear-gradient(135deg, #1f4037 0%, #99f2c8 100%);
        color: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
    }
    .card-dark { 
        background-color: #1A1A1A; 
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
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# 🚀 SECURE API CONNECTION (Step 6)
# ============================================
# Corrected line 78 (No citation markers in actual code)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"]) 
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"temperature": 0.2, "max_output_tokens": 500}
    )
else:
    st.error("⚠️ API Key missing! Add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

# ============================================
# 🚀 HEADER & STATS
# ============================================
st.markdown("""
<div class="main-header">
    <h1 style="font-size: 3rem; margin: 0;">🌾 BiharKrishi AI</h1>
    <p style="font-size: 1.2rem; opacity: 0.9;">Precision Farming Assistant • Dark Edition</p>
</div>
""", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
with m1:
    st.markdown('<div class="card-dark"><h2>📍 38</h2><p>Districts Supported</p></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="card-dark"><h2>🌱 91%</h2><p>Marginal Farmer Focus</p></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="card-dark"><h2>⚡ 1.5</h2><p>Gemini Flash Engine</p></div>', unsafe_allow_html=True)

# ============================================
# 🎯 INPUT SECTION
# ============================================
with st.sidebar:
    st.title("👤 Farmer Persona")
    f_name = st.text_input("Name", "Ram Kumar Baitha")
    f_loc = st.text_input("Location", "Kishanganj, Bihar")
    f_land = st.text_input("Land Size (Ha)", "0.25")

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
        with st.spinner("🧠 Consulting Bihar's Agricultural Database..."):
            full_prompt = f"""
            Expert Bihar Agri-Consultant. Farmer: {f_name} from {location}. 
            Category: {category}. Stage: {crop_stage}. Query: {query}
            Instructions: Provide a formatted, bulleted list of actionable steps. 
            Include a brief 'Why' (justification) for each point. Use simple language.
            """
            try:
                response = model.generate_content(full_prompt)
                st.markdown('<div style="background: #111; border-left: 5px solid #00FF41; padding: 20px;">'
                            '<h2 style="color: #00FF41;">💡 AI Recommendations</h2></div>', unsafe_allow_html=True)
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")

# ============================================
# 📋 VALIDATION CHECKLIST (Step 5)
# ============================================
st.write("---")
with st.expander("📝 FA-2 Validation Checklist"):
    st.checkbox("🌍 Region-Specific Advice?", value=True)
    st.checkbox("💡 Logical Reasoning (The 'Why')?", value=True)
    st.checkbox("📝 Simple Language for Farmers?", value=True)
    st.checkbox("✅ Safe & Verified Advice?", value=True)
