import streamlit as st
import google.generativeai as genai

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="BiharKrishi AI", page_icon="🌾", layout="wide")

# --- 2. SECURE API CONNECTION (FA-2 Requirement) ---
# We retrieve the key from Streamlit Secrets for security and deployment
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Step 5: Model Optimization (Temperature 0.2 prevents hallucination)
    generation_config = {
        "temperature": 0.2, 
        "max_output_tokens": 400,
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-3-flasg-preview",
        generation_config=generation_config
    )
else:
    st.error("⚠️ API Key missing! Please add your key to Streamlit Secrets.")
    st.stop()

# --- 3. SIDEBAR: EDITABLE USER PROFILE ---
with st.sidebar:
    st.title("👤 User Profile")
    farmer_name = st.text_input("Farmer Name:", value="Ram Kumar Baitha")
    farmer_location = st.text_input("Home Location:", value="Kishanganj, Bihar")
    land_size = st.text_input("Land Size (Hectares):", value="0.25")
    st.divider()
    st.info("Personalized profile for site-specific advice.")

# --- 4. MAIN INTERFACE (Design & Implementation) ---
st.title("🌾 BiharKrishi AI: Smart Farming Assistant")
st.subheader("Solving Bihar's Flood-Drought Paradox with Generative AI")

# Text inputs for Location, Stage, and Category as requested
col1, col2 = st.columns(2)
with col1:
    location = st.text_input("Enter your District:", value="Samastipur")
    crop_stage = st.text_input("Current Crop Stage:", value="Vegetative")

with col2:
    category = st.text_input("What do you need help with?", value="Diesel Cost Saving")

user_query = st.text_input("Enter your specific farming question:")

# --- 5. FORMATTED OUTPUT & JUSTIFICATION (Step 4) ---
if st.button("Get AI Advice"):
    if user_query and location:
        with st.spinner("Analyzing regional agricultural data..."):
            # System prompt ensures outputs are actionable and justified (Step 4)
            full_prompt = f"""
            You are an expert Bihar agricultural consultant. 
            User Profile: {farmer_name} from {farmer_location} with {land_size} hectares.
            Current Query Context: District {location}, Crop Stage {crop_stage}.
            Question: {user_query}
            
            Instructions: Provide a formatted response as per FA-2 standards:
            1. Use a bulleted list for actionable steps.
            2. Include a brief 'Why' (justification) for each suggestion to build trust.
            3. Use simple, non-technical language for a layperson.
            """
            
            try:
                response = model.generate_content(full_prompt)
                st.markdown("### 💡 Expert Recommendations")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ API Error: {e}")
    else:
        st.warning("Please enter your district and a question.")
