 import streamlit as st
import google.generativeai as genai
# --- APP CONFIGURATION ---
st.set_page_config(page_title="BiharKrishi AI", page_icon="🌾", layout="wide")

# --- SIDEBAR: EDITABLE USER PROFILE (Requirement for User Interaction Monitoring) ---
with st.sidebar:
    st.title("👤 User Profile")
    # CHANGED: Static text replaced with st.text_input as requested
    farmer_name = st.text_input("Farmer Name:", value="Ram Kumar Baitha")
    farmer_location = st.text_input("Home Location:", value="Kishanganj, Bihar")
    land_size = st.text_input("Land Size (Hectares):", value="0.25")
    
    st.divider()
    api_key = st.text_input("Enter Gemini API Key", type="password")

# --- GEMINI API SETUP ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Step 5: Optimized Model Parameters (Temperature 0.2 for factual accuracy)
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

        # Inputs for specific query context
        col1, col2 = st.columns(2)
        with col1:
            # Using text_input for District as requested in previous turn
            location = st.text_input("Select your District:", value="Samastipur")
            crop_stage = st.text_input("Current Crop Stage:", value="Vegetative")
        
        with col2:
            category = st.text_input("What do you need help with?", value="Diesel Cost Saving")

        user_query = st.text_input("Enter your specific farming question:")

        # --- OUTPUT FORMATTING & REASONING (Step 4) ---
        if st.button("Get AI Advice"):
            if user_query and location:
                with st.spinner("Analyzing regional data..."):
                    # The prompt now includes the profile info from the sidebar text boxes
                    full_prompt = f"""
                    You are an expert Bihar agricultural consultant. 
                    User Profile: {farmer_name} from {farmer_location} with {land_size} hectares.
                    Current Query Context: District {location}, Crop Stage {crop_stage}.
                    Question: {user_query}
                    
                    Instructions: Provide a formatted response as per FA-2 standards:
                    1. A bulleted list of actionable steps.
                    2. A brief 'Why' (justification) for each suggestion to build trust.
                    3. Simple, non-technical language for a layperson.
                    """
                    
                    response = model.generate_content(full_prompt)
                    
                    st.markdown("### 💡 Expert Recommendations")
                    st.write(response.text)
            else:
                st.warning("Please ensure you have entered your district and a question.")
                
    except Exception as e:
        st.error(f"Configuration Error: {e}")
else:
    st.warning("Please enter your Gemini API Key in the sidebar to begin.")
