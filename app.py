import streamlit as st
import google.generativeai as genai

# =========================================================
# SMART FARMING ASSISTANT – GEMINI 1.5 ONLY
# =========================================================

st.set_page_config(
    page_title="Smart Farming Assistant",
    page_icon="🌱",
    layout="centered"
)

st.title("🌾 Smart Farming Assistant")
st.caption("Powered by Google Gemini 1.5")

# ---------------- API KEY ----------------
st.sidebar.header("🔑 Gemini API Key")
api_key = st.sidebar.text_input(
    "Paste your Gemini API key",
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

crop = st.text_input(
    "Crop / Topic",
    placeholder="e.g. rice, pests, soil"
)

preference = st.radio(
    "Farming Preference",
    ["General", "Organic only", "Low water usage"]
)

question = st.text_area(
    "Ask your farming question",
    placeholder="e.g. What crops should I grow this month?"
)

# ---------------- PROMPT BUILDER ----------------
def build_prompt(location, crop, preference, question):
    return f"""
You are an agricultural expert assisting a small or marginal farmer.

Location: {location}
Crop or Topic: {crop}
Farming Preference: {preference}

Question:
{question}

Respond with:
- Clear bullet points
- Simple, non-technical language
- Low-cost and sustainable solutions
- A short explanation of why the advice works
"""

# ---------------- GEMINI 1.5 CALL ----------------
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.4,
                "max_output_tokens": 600
            }
        )

        if response and hasattr(response, "text") and response.text:
            return response.text
        else:
            return "⚠️ Gemini 1.5 returned no response."

    except Exception as e:
        return f"❌ Gemini 1.5 API Error:\n{str(e)}"

# ---------------- BUTTON ----------------
if st.button("🌱 Get Farming Advice"):
    if not api_key:
        st.error("❌ Please enter your Gemini API key.")
    elif not question.strip():
        st.warning("⚠️ Please type a farming question.")
    else:
        with st.spinner("Thinking like an agri expert..."):
            output = get_gemini_response(
                build_prompt(location, crop, preference, question)
            )

        st.subheader("✅ AI Recommendation")
        st.markdown(output)

        with st.expander("ℹ️ Why this advice works"):
            st.write(
                "This advice is generated using region-specific context, "
                "small-farmer constraints, and sustainable agricultural practices."
            )

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("FA-2 | Smart Farming Assistant | Gemini 1.5")
