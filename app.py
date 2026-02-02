import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Smart Farming Assistant",
    page_icon="🌱",
    layout="centered"
)

st.title("🌾 Smart Farming Assistant")
st.caption("FA-2 | Powered by Gemini 1.5")

# ---------- API KEY ----------
st.sidebar.header("🔑 Gemini API Key")
api_key = st.sidebar.text_input("Paste your API key", type="password")

if api_key:
    genai.configure(api_key=api_key)

# ---------- USER INPUT ----------
st.subheader("👨‍🌾 Farmer Details")

location = st.selectbox(
    "Select your region",
    ["Bihar (India)", "Punjab (India)", "Ghana", "Canada"]
)

crop = st.text_input("Crop / Topic", placeholder="e.g. rice, pests, soil")

preference = st.radio(
    "Farming Preference",
    ["General", "Organic only", "Low water usage"]
)

question = st.text_area(
    "Ask your farming question",
    placeholder="e.g. What should I grow this month?"
)

# ---------- PROMPT ----------
def build_prompt(location, crop, preference, question):
    return f"""
You are an agricultural expert helping small and marginal farmers.

Location: {location}
Crop or Topic: {crop}
Preference: {preference}

Question: {question}

Give:
- Bullet-point advice
- Simple language
- Low-cost solutions
- Short explanation why it works
"""

# ---------- GEMINI ----------
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text if response.text else "No response generated."

# ---------- BUTTON ----------
if st.button("🌱 Get Farming Advice"):
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not question.strip():
        st.warning("Please type a question.")
    else:
        with st.spinner("Thinking like an agri expert…"):
            try:
                output = get_gemini_response(
                    build_prompt(location, crop, preference, question)
                )
                st.subheader("✅ AI Recommendation")
                st.markdown(output)
            except Exception as e:
                st.error("API Error")
                st.code(str(e))

st.markdown("---")
st.caption("FA-2 | Smart Farming Assistant")
