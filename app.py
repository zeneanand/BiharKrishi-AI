import streamlit as st
import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# 🎨 PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="🌱 BiharKrishi AI: Vibrant Edition",
    page_icon="🌾",
    layout="wide"
)

# ============================================
# 🌈 VIBRANT DARK CSS (Design & Implementation)
# ============================================
st.markdown("""
<style>
    /* Dark Background with deep blue tint */
    .stApp {
        background-color: #050a0e;
        color: #e0e0e0;
    }
    
    /* Vibrant Gradient Header with Animation effect */
    .main-header {
        background: linear-gradient(90deg, #00f260 0%, #0575E6 100%);
        color: white;
        padding: 45px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(0, 242, 96, 0.3);
    }

    /* Colorful Neon Stat Cards */
    .card-neon-green { 
        background-color: #0f1c14; 
        border: 2px solid #00f260;
        color: #00f260; 
        padding: 20px; 
        border-radius: 15px; 
        text-align: center; 
    }
    .card-neon-blue { 
        background-color: #0a1622; 
        border: 2px solid #0575E6;
        color: #0575E6; 
        padding: 20px; 
        border-radius: 15px; 
        text-align: center; 
    }
    .card-neon-orange { 
        background-color: #1c140f; 
        border: 2px solid #f7971e;
        color: #ffd200; 
        padding: 20px; 
        border-radius: 15px; 
        text-align: center; 
    }

    /* Vibrant Action Button */
    .stButton>button {
        background: linear-gradient(45deg, #f7971e 0%, #ffd200 100%);
        color: #000;
        border: none;
        padding: 18px 30px;
        border-radius: 50px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.4s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(255, 210, 0, 0.5);
    }

    /* Justified Response Styling */
    .response-container {
        background: #111;
        border-left: 8px solid #00f260;
        padding: 25px;
        border-radius: 12px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# 🚀 SECURE API CONNECTION (Step 6)
# ============================================
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["AIzaSyDmoY3_mBl00-KYhxLYTzNwNpsO6if0GxA"]) 
    model = genai.GenerativeModel(
        model_name="gemini-3-flash-preview",
        generation_config={"temperature": 0.2, "max_output_tokens": 500}
    )
else:
    st.error("AIzaSyDmoY3_mBl00-KYhxLYTzNwNpsO6if0GxA")
    st.stop()

# ============================================
# 🚀 HEADER & VIBRANT STATS
# ============================================
st.markdown("""
<div class="main-header">
    <h1 style="font-size: 3.5rem; margin: 0; text-shadow: 2px 2px 10px rgba(0,0,0,0.5);">🌾 BiharKrishi AI</h1>
    <p style="font-size: 1.4rem; font-weight: 300;">Advanced Generative Intelligence for Modern Farming</p>
</div>
""", unsafe_allow_html=True)

# Rainbow Metric Cards
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown('<div class="card-neon-green"><h2>📍 38</h2><p>Districts Covered</p></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="card-neon-blue"><h2>🤖 1.5</h2><p>Gemini Engine</p></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="card-neon-orange"><h2>📈 +40%</h2><p>Yield Potential</p></div>', unsafe_allow_html=True)

# ============================================
# 📊 DATA VISUALIZATION (Grouped Bar Chart)
# ============================================
st.write("---")
st.markdown("### 📊 Crop Yield Analysis (Traditional vs AI-Smart)")

# 
impact_data = {
    'Crop Type': ['Rice', 'Wheat', 'Maize', 'Pulses'],
    'Traditional': [1400, 1600, 1000, 700],
    'AI-Optimized': [1950, 2200, 1450, 1100]
}
df = pd.DataFrame(impact_data)

fig, ax = plt.subplots(figsize=(12, 5), facecolor='#050a0e')
ax.set_facecolor('#050a0e')

x = range(len(df['Crop Type']))
ax.bar([i - 0.2 for i in x], df['Traditional'], width=0.4, label='Traditional', color='#ff4b2b', alpha=0.8)
ax.bar([i + 0.2 for i in x], df['AI-Optimized'], width=0.4, label='AI-Smart', color='#00f260', alpha=0.9)

# Neon Styling for Chart
ax.set_xticks(x)
ax.set_xticklabels(df['Crop Type'], color='white', fontweight='bold')
ax.tick_params(axis='y', colors='#888')
ax.spines['bottom'].set_color('#333')
ax.spines['left'].set_color('#333')
ax.legend(facecolor='#111', edgecolor='#00f260', labelcolor='white')
ax.set_title("Expected Production Growth in Bihar", color='#00f260', size=16, pad=15)

st.pyplot(fig)

# ============================================
# 🎯 INPUT INTERACTION (Step 6)
# ============================================
st.write("---")
with st.sidebar:
    st.title("👨‍🌾 Farmer Persona")
    f_name = st.text_input("Name", "Ram Kumar Baitha")
    f_loc = st.text_input("Location", "Kishanganj, Bihar")
    f_land = st.text_input("Land Size (Ha)", "0.25")
    st.divider()
    st.info("Input your details to personalize the AI model.")

col1, col2 = st.columns(2)
with col1:
    location = st.text_input("Current District", "Samastipur")
    crop_stage = st.text_input("Crop Stage", "Vegetative")
with col2:
    category = st.text_input("Help Category", "Diesel Cost Saving")
    query = st.text_input("Your Question", "How to save fuel during irrigation?")

# ============================================
# ⚡ AI ADVICE & FORMATTING (Step 4)
# ============================================
if st.button("🚀 ACTIVATE FARMGENIUS AI"):
    if query:
        with st.spinner("🧠 Consulting AI Agricultural Repositories..."):
            full_prompt = f"""
            Role: Expert Bihar Agri-Consultant. 
            Persona: {f_name} from {location} ({f_land} ha). 
            Query: {query}.
            Instructions: Provide a bulleted list of actionable steps with 'Why' justifications. 
            Ensure formatting is clean and language is simple.
            """
            try:
                response = model.generate_content(full_prompt)
                st.markdown('<div class="response-container"><h2 style="color: #00f260;">💡 AI Strategic Advice</h2></div>', unsafe_allow_html=True)
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
