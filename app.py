import streamlit as st
import openai

st.set_page_config(page_title="BiharKrishi AI", page_icon="🌾", layout="wide")

# ------------------ Sidebar ------------------
with st.sidebar:
    st.title("👤 Farmer Profile")
    farmer_name = st.text_input("Farmer Name", "Ram Kumar Baitha")
    farmer_location = st.text_input("Location", "Kishanganj, Bihar")
    land_size = st.number_input("Land Size (Hectares)", 0.01, 10.0, 0.25)

# ------------------ Main UI ------------------
st.title("🌾 BiharKrishi AI")
district = st.text_input("District", "Samastipur")
crop_stage = st.selectbox("Crop Stage", ["Nursery", "Vegetative", "Flowering", "Maturity", "Harvest"])
category = st.selectbox("Help Category", ["Diesel Cost Saving", "Irrigation", "Fertilizer", "Pest Control"])
question = st.text_input("Ask your question", "How can I reduce diesel cost in irrigation?")

# ------------------ OpenAI API ------------------
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")

if st.button("🌱 Get AI Advice"):
    if not question.strip():
        st.warning("Please enter your question.")
    else:
        import openai
        openai.api_key = OPENAI_API_KEY
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

Give 3–5 practical bullet points.
Explain briefly why each helps.
Use simple English mixed with Hindi words.
Advice must suit small farmers.
"""

        with st.spinner("Generating advice..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2,
                    max_tokens=400
                )
                st.markdown("### 💡 Expert Advice")
                st.write(response['choices'][0]['message']['content'])
            except Exception as e:
                st.error(f"❌ Error: {e}")

