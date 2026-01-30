import streamlit as st
import google.generativeai as genai

# --------------------------------------------------
# 1. APP CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="BiharKrishi AI",
    page_icon="🌾",
    layout="wide"
)

# --------------------------------------------------
# 2. GEMINI API SETUP (SECURE)
# --------------------------------------------------
try:
    if "GOOGLE_API_KEY" not in st.secrets:
        st.error("⚠️ GOOGLE_API_KEY not found in Streamlit Secrets.")
        st.stop()

    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

    generation_config = {
        "temperature": 0.2,
        "max_output_tokens": 400,
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )

except Exception as e:
    st.error(f"❌ Failed to initialize Gemini API: {e}")
    st.stop()

# --------------------------------------------------
# 3. SIDEBAR: USER PROFILE
# --------------------------------------------------
with st.sidebar:
    st.title("👤 Farmer Profile")

    farmer_name = st.text_input("Farmer Name", "Ram Kumar Baitha")
    farmer_location = st.text_input("Home Location", "Kishanganj, Bihar")
    land_size = st.text_input("Land Size (Hectares)", "0.25")

    st.divider()
    st.info("Region-specific agricultural guidance for Bihar farmers.")

# --------------------------------------------------
# 4. MAIN UI
# --------------------------------------------------
st.title("🌾 BiharKrishi AI")
st.subheader("Smart Farming Assistant for Bihar")

col1, col2 = st.columns(2)

with col1:
    district = st.text_input("District", "Samastipur")
    crop_stage = st.text_input("Crop Stage", "Vegetative")

with col2:
    category = st.text_input("Help Category", "Diesel Cost Saving")

user_query = st.text_input(
    "Ask your farming question",
    placeholder="e.g., How can I reduce diesel usage in irrigation?"
)

# --------------------------------------------------
# 5. AI RESPONSE
# --------------------------------------------------
if st.button("🌱 Get AI Advice"):
    if not user_query or not district:
        st.warning("Please fill in all required fields.")
    else:
        with st.spinner("Analyzing Bihar-specific agricultural data..."):
            prompt = f"""
You are an expert agricultural consultant for Bihar, India.

Farmer Profile:
- Name: {farmer_name}
- Location: {farmer_location}
- Land Size: {land_size} hectares

Context:
- District: {district}
- Crop Stage: {crop_stage}
- Category: {category}

Question:
{user_query}

Instructions:
1. Give 3–5 actionable bullet points.
2. After each point, explain briefly *why* it helps.
3. Use simple Hindi-friendly English.
4. Keep advice practical and suitable for small farmers.
"""

            try:
                response = model.generate_content(prompt)

                st.markdown("### 💡 Expert Recommendations")
                st.write(response.text)

                st.divider()
                st.caption("Was this advice helpful?")

                col_yes, col_no = st.columns(2)
                with col_yes:
                    if st.button("👍 Yes"):
                        st.success("Thanks! This helps improve BiharKrishi AI.")

                with col_no:
                    if st.button("👎 No"):
                        st.info("Thanks for the feedback. We’ll improve.")

            except Exception as e:
                st.error(f"❌ Error generating advice: {e}")
