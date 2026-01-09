import streamlit as st
import google.generativeai as genai

# --- APP CONFIGURATION ---
st.set_page_config(page_title="BiharKrishi AI", page_icon="🌾", layout="wide")

# --- SIDEBAR: EDITABLE USER PROFILE ---
with st.sidebar:
    st.title("👤 User Profile")
    farmer_name = st.text_input("Farmer Name:", value="Ram Kumar Baitha")
    farmer_location = st.text_input("Home Location:", value="Kishanganj, Bihar")
    land_size = st.text_input("Land Size (Hectares):", value="0.25")
    st.divider()
    st.info("API Key is managed via Streamlit Secrets for security.")

# --- SECURE API KEY RETRIEVAL ---
# This pulls the key from Streamlit's cloud environment instead of your code
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Step 5: Optimized Model Parameters (Temperature 0.2 for accuracy)
    generation_config = {
        "temperature": 0.2, 
        "max_output_tokens": 400,
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )

    # --- MAIN UI ---
    st.title("🌾 BiharKrishi AI: Smart Farming Assistant")
    st.subheader("Solving Bihar's Flood-Drought Paradox with Generative AI")

    col1, col2 = st.columns(2)
    with col1:
        location = st.text_input("Enter your District:", value="Samastipur")
        crop_stage = st.text_input("Enter Current Crop Stage:", value="Vegetative")
    
    with col2:
        category = st.text_input("What do you need help with?", value="Diesel Cost Saving")

    user_query = st.text_input("Enter your specific farming question:")

    # Step 4: Logic for Actionable & Justified Output
    if st.button("Get AI Advice"):
        if user_query and location:
            with st.spinner("Analyzing regional data..."):
                full_prompt = f"""
                You are an expert Bihar agricultural consultant. 
                User Profile: {farmer_name} from {farmer_location} with {land_size} hectares.
                Context: District {location}, Crop Stage {crop_stage}.
                Question: {user_query}
                
                Instructions: Provide a formatted response as per FA-2 standards:
                1. A bulleted list of actionable steps.
                2. A brief 'Why' (justification) for each suggestion.
                3. Simple language for a layperson.
                """
                response = model.generate_content(full_prompt)
                st.markdown("### 💡 Expert Recommendations")
                st.write(response.text)
        else:
            st.warning("Please enter your district and a question.")
else:
    st.error("Missing API Key! Please add 'GOOGLE_API_KEY' to your Streamlit Secrets.")
    
