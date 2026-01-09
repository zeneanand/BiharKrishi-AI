import streamlit as st
import google.generativeai as genai

# --- APP CONFIGURATION ---
st.set_page_config(page_title="BiharKrishi AI", page_icon="🌾", layout="wide")

# --- SIDEBAR: API KEY & PERSONA ---
with st.sidebar:
    st.title("👤 User Profile")
    st.success("**Farmer:** Ram Kumar Baitha")
    st.info("**Location:** Kishanganj, Bihar\n\n**Land Size:** 0.25 Hectares")
    api_key = st.text_input("Enter Gemini API Key", type="password")

# --- GEMINI API SETUP ---
if api_key:
    try:
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

        # Step 6: Inputs for Location and Crop Stage
        col1, col2 = st.columns(2)
        with col1:
            location = st.selectbox("Select your District:", ["Kishanganj", "Gaya", "Saharsa", "Samastipur", "Muzaffarpur", "Purnea"])
            crop_stage = st.selectbox("Current Crop Stage:", ["Sowing", "Vegetative", "Flowering", "Harvesting"])
        
        with col2:
            category = st.selectbox("What do you need help with?", [
                "Flood-Ready Crops", "Diesel Cost Saving", "Seed Selection", 
                "Pest Management", "Soil & Fertilizer", "Sustainable Tips"
            ])

        user_query = st.text_input("Enter your specific farming question:")

        # Step 4: Logic for Actionable & Justified Output
        if st.button("Get AI Advice"):
            if user_query:
                with st.spinner("Analyzing regional data..."):
                    # Optimized System Prompt for Bihar context
                    full_prompt = f"""
                    You are an expert Bihar agricultural consultant. 
                    Context: Farmer in {location}, Bihar. Crop Stage: {crop_stage}.
                    Question: {user_query}
                    
                    Instructions: Provide a formatted response with:
                    1. A bulleted list of actionable steps.
                    2. A brief 'Why' (justification) for each suggestion to build trust.
                    3. Simple, non-technical language for a layperson.
                    """
                    
                    response = model.generate_content(full_prompt)
                    
                    st.markdown("### 💡 Expert Recommendations")
                    st.write(response.text)
            else:
                st.warning("Please enter a question.")
                
    except Exception as e:
        st.error(f"Configuration Error: {e}")
else:
    st.warning("Please enter your Gemini API Key in the sidebar to begin.")
        
