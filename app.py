import streamlit as st
import google.generativeai as genai

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="BiharKrishi AI",
    page_icon="🌾",
    layout="wide"
)

# --------------------------------------------------
# GEMINI SETUP (WORKING MODEL)
# --------------------------------------------------
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("❌ GOOGLE_API_KEY missing. Add it in Streamlit Secrets.")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel(
    model_name="models/gemini-1.0-pro",
    generation_config={
        "temperature": 0.2,
        "max_output_tokens": 400,
    }
)

# --------------------------------------------------
# SIDEBAR – FARMER PROFILE
# --------------------------------------------------
with st.sidebar:
    st.title("👤 Farmer Profile")

    farmer_name = st.text_input("Farmer Name", "Ram Kumar Baitha")
    farmer_location = st.text_input("Location", "Kishanganj, Bihar")
    land_size = st.number_input(
        "Land Size (Hectares)",
        min_value=0.01,
        max_value=10.0,
        value=0.25,
        step=0.05
    )

    st.info("Region-specific agricultural guidance for Bihar farmers")

# --------------------------------------------------
# MAIN UI
# --------------------------------------------------
st.title("🌾 BiharKrishi AI")
st.subheader("Smart Farming Assistant for Bihar Farmers")

col1, col2 = st.columns(2)

with col1:
    district = st.text_input("District", "Samastipur")
    crop_stage = st.selectbox(
        "Crop Stage",
        ["Nursery", "Vegetative", "Flowering", "Maturity", "Harvest"]
    )

with col2:
    category = st.selectbox(
        "Help Category",
        [
            "Diesel Cost Saving",
            "Irrigation",
            "Fertilizer",
            "Pest Control",
            "Government Schemes"
        ]
    )

question = st.text_input(
    "Ask your farming question",
    placeholder="How can I reduce diesel cost in irrigation?"
)

# --------------------------------------------------
# GENERATE RESPONSE
# --------------------------------------------------
if st.button("🌱 Get AI Advice"):
    if not question.strip():
        st.warning("Please enter your question.")
    else:
        with st.spinner("Generating Bihar-specific advice..."):
            prompt = f"""
You are an expert agricultural advisor for Bihar, India.

Farmer Profile:
- Name: {farmer_name}
- Location: {farmer_location}
- Land Size: {land_size} hectares

Context:
- District: {district}
- Crop Stage: {crop_stage}
- Category: {category}

Question:
{question}

Instructions:
1. Give 3–5 actionable bullet points.
2. Explain briefly why each point helps.
3. Use simple English mixed with easy Hindi words.
4. Advice must suit small farmers.
5. Do NOT mention AI, model, or technology.
"""

            try:
                response = model.generate_content(prompt)

                if response and response.text:
                    st.markdown("### 💡 Expert Advice")
                    st.write(response.text)
                else:
                    st.warning("No response generated. Please try again.")

            except Exception as e:
                st.error(f"❌ Error generating advice: {e}")
