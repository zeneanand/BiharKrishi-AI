import streamlit as st
import google.generativeai as genai

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Smart Farming Assistant",
    page_icon="🌱",
    layout="centered"
)

st.title("🌾 Smart Farming Assistant")
st.caption("AI-powered farming advice using Gemini 1.5")

# ---------------- API KEY ----------------
st.sidebar.header("🔑 API Configuration")
api_key = st.sidebar.text_input(
    "Enter your Gemini API Key",
    type="password"
)

if api_key:
    genai.configure(api_key=api_key)

# ---------------- USER INPUT ----------------
st.subheader("👨‍🌾 Farmer Details")

location = st.selectbox(
    "Select your region",
    ["Bihar (India)", "Punjab (India)", "Ghana", "Canada"]
)

crop = st.text_input("Crop / Farming topic (e.g. rice, vegetables, soil, pests)")

preference = st.radio(
    "Farming Preference",
    ["General", "Organic only", "Low water usage"]
)

question = st.text_area(
    "Ask your farming question",
    placeholder="e.g. What should I grow this month?"
)

# ---------------- PROMPT BUILDER ----------------
def build_prompt(location, crop, preference, question):
    return f"""
You are an agricultural expert helping a small or marginal farmer.

Location: {location}
Crop or Topic: {crop}
Farming Preference: {preference}

Question: {question}

Give:
1. Clear bullet-point advice
2. Simple language
3. Low-cost solutions where possible
4. A short explanation of WHY the advice works
"""

# ---------------- GEMINI CALL ----------------
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.4,
            "max_output_tokens": 600
        }
    )
    return response.text

# ---------------- BUTTON ACTION ----------------
if st.button("🌱 Get Farming Advice"):
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not question:
        st.warning("Please enter a farming question.")
    else:
        with st.spinner("Thinking like an agri expert..."):
            prompt = build_prompt(location, crop, preference, question)
            try:
                output = get_gemini_response(prompt)
                st.subheader("✅ AI Recommendation")
                st.markdown(output)

                with st.expander("ℹ️ Why this advice works"):
                    st.write(
                        "This advice is generated using region-specific context, "
                        "small-farmer constraints, and sustainable practices to ensure "
                        "practical and safe farming decisions."
                    )
            except Exception as e:
                st.error("Something went wrong. Please try again.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built for FA-2 | Generative AI – Smart Farming Assistant")
