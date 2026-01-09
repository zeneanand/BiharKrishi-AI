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
        
        # Model parameters for factual agricultural advice (FA-2 Requirement)
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

        # CHANGED: Using st.text_input instead of st.selectbox for manual typing
        col1, col2 = st.columns(2)
        with col1:
            location = st.text_input("Enter your District:", value="Samastipur")
            crop_stage = st.text_input("Enter Current Crop Stage:", value="Vegetative")
        
        with col2:
            category = st.text_input("What do you need help with?", value="Diesel Cost Saving")

        user_query = st.text_input("Enter your specific farming question (e.g., How to save fuel?)")

        # --- OUTPUT FORMATTING & REASONING (Step 4) ---
        if st.button("Get AI Advice"):
            if user_query and location and crop_stage:
                with st.spinner("Analyzing regional data..."):
                    # Optimized System Prompt for Bihar context
                    full_prompt = f"""
                    You are an expert Bihar agricultural consultant. 
                    Context: Farmer in {location}, Bihar. Crop Stage: {crop_stage}.
                    Category: {category}.
                    Question: {user_query}
                    
                    Instructions: Provide a formatted response as per FA-2 standards:
                    1. Use a bulleted list for actionable instructions.
                    2. Include a brief 'Why' (reasoning) for each suggestion to build trust.
                    3. Use simple, non-technical language for a farmer.
                    """
                    
                    response = model.generate_content(full_prompt)
                    
                    # Displaying formatted Gemini output
                    st.markdown("### 💡 Expert Recommendations")
                    st.write(response.text)
            else:
                st.warning("Please fill in all the text fields and enter a question.")
                
    except Exception as e:
        st.error(f"Configuration Error: {e}")
else:
    st.warning("Please enter your Gemini API Key in the sidebar to begin.")
    
