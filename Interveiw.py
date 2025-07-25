import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Interview Question Generator", page_icon="🎯")
st.title("🎯 AI Interview Question Generator")
st.markdown("Generate job-specific **technical interview questions** using GPT-3.5!")

job_title = st.text_input("Enter a job title (e.g., AI Engineer, Frontend Developer)")

if st.button("Generate Questions"):
    if job_title:
        with st.spinner("Thinking... 🤖"):
            try:
                prompt = f"Generate 5 technical interview questions for a {job_title} role. Return them as a numbered list."

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )

                output = response.choices[0].message.content
                st.success("Here are your questions:")
                st.markdown(output)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a job title.")
