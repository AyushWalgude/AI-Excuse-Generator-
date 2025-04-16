import streamlit as st
import google.generativeai as genai

# 🔑 Replace with your actual Gemini API Key
genai.configure(api_key="AIzaSyC9_mESxY4lOsqcOhWHLVbLNcALBgBg9UU")

# Initialize Gemini model correctly
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Streamlit UI setup
st.set_page_config(page_title="🧠 AI Excuse Generator", layout="centered")
st.title("🧠 AI Excuse Generator")
st.write("Let AI help you come up with the perfect excuse 😎")

# Inputs
situation = st.selectbox("Pick a situation", [
    "Late to class",
    "Missed assignment",
    "Missed exam",
    "Skipped meeting",
    "Forgot to reply"
])

tone = st.radio("Pick a tone:", ["Polite", "Funny", "Creative"])

if st.button("Generate Excuse"):
    with st.spinner("Crafting your excuse..."):
        prompt = f"Write a {tone.lower()} excuse for this situation: {situation}."
        try:
            response = model.generate_content(prompt)
            st.markdown("### 🙈 Here's your excuse:")
            st.success(response.text)
        except Exception as e:
            st.error(f"❌ Something went wrong:\n\n{e}")
