if st.button("Get AI Advice"):
        # Validation: Check if all inputs are present
        if user_query and location and crop_stage:
            with st.spinner("Analyzing regional data..."):
                # Constructing the prompt carefully
                full_prompt = f"""
                You are an expert Bihar agricultural consultant. 
                Context: Farmer in {location}, Bihar. Crop Stage: {crop_stage}.
                Question: {user_query}
                
                Instructions: Provide a formatted response with:
                1. A bulleted list of actionable steps.
                2. A brief 'Why' or justification for each suggestion.
                3. Simple, non-technical language.
                """
                
                try:
                    response = model.generate_content(full_prompt)
                    
                    # Check if response has valid text to prevent further errors
                    if response.text:
                        st.markdown("### 💡 Expert Recommendations")
                        st.write(response.text)
                    else:
                        st.error("The model returned an empty response. Please try rephrasing.")
                        
                except Exception as e:
                    st.error(f"API Error: {e}. Please check if your API Key is active and has enough quota.")
        else:
            st.warning("Please ensure you have selected a District, Crop Stage, and entered a question.")
