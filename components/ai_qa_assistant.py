
import streamlit as st
import io
from openai import OpenAI

#model used: llama-3.3-nemotron-super-49b-v1
class AIQA:
    def __init__(self, api_key):
        self.api_key = api_key

    def ask(self):
        st.markdown("Model Used: llama-3.3-nemotron-super-49b-v1")
        user_input = st.text_area("Describe the feature or error:")
        if st.button("Ask AI"):
            if self.api_key and user_input:
                with st.spinner("Thinking..."):
                    client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=self.api_key)
                    stream = client.chat.completions.create(
                        model="nvidia/llama-3.3-nemotron-super-49b-v1",
                        messages=[
                            {"role": "system", "content": "You are a QA test automation expert. Provide only structured test cases."},
                            {"role": "user", "content": user_input}
                        ],
                        stream=True
                    )
                    full_response = ""
                    for chunk in stream:
                        delta = chunk.choices[0].delta
                        if delta.content:
                            full_response += delta.content
                    st.text_area("AI Full Response", value=full_response, height=1000)
                    file = io.BytesIO(full_response.encode("utf-8"))
                    st.download_button("💾 Download AI Response", file, "ai_qa_response.txt")
            else:
                st.warning("Please enter the API key and a prompt.")
