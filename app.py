import streamlit as st
import google.generativeai as genai

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="BiharKrishi AI",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------
# GEMINI SETUP
# -----------------------------
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("GOOGLE_API_KEY missing. Add it to secrets.toml")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

models/gemini-1.0-pro-vision

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.title("👤 Farmer Profile")
    farmer_name = st.text_input("Farmer Name", "Ram Kumar Baitha")
    farmer_location = st.text_input("Location", "Kishanganj, Bihar")
    land_size = st.number_input("Land Size (Hectares)", 0.01, 10.0, 0.25)

# -----------------------------
# MAIN UI
# -----------------------------
st.title("🌾 BiharKrishi AI")
st.subheader("Smart Farming Assistant for Bihar Farmers")

district = st.text_input("District", "Samastipur")

crop_stage = st.selectbox(
    "Crop Stage",
    ["Nursery", "Vegetative", "Flowering", "Maturity", "Harvest"]
)

category = st.selectbox(
    "Help Category",
    ["Diesel Cost Saving", "Irrigation", "Fertilizer", "Pest Control"]
)

question = st.text_input(
    "Ask your question",
    "How can I reduce diesel cost in irrigation?"
)

# -----------------------------
# GENERATE RESPONSE
# -----------------------------
if st.button("🌱 Get AI Advice"):
    if not question.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Generating advice..."):
            prompt = f"""
You are an agriculture expert for Bihar, India.

Farmer:
Name: {farmer_name}
Location: {farmer_location}
Land: {land_size} hectares

Context:
District: {district}
Crop Stage: {crop_stage}
Category: {category}

Question:
{question}

Give 3–5 practical bullet points.
Use simple English mixed with easy Hindi words.
Do not mention AI or technology.
"""

            try:
                response = model.generate_content(prompt)
                st.markdown("### 💡 Expert Advice")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

