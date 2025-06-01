
import streamlit as st
import io
from openai import OpenAI

#model used: nvidia/llama-3.3-nemotron-super-49b-v1
class TestCodeGenerator:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate(self):
        st.markdown("Model Used: llama-3.3-nemotron-super-49b-v1")
        language = st.selectbox("Choose Framework:", ["PyTest (Python)", "TestNG (Java)"])
        scenario = st.text_area("Describe the test scenario:")
        if st.button("Generate Test Code") and scenario:
            lang_instruction = "Generate PyTest script." if "PyTest" in language else "Generate Java TestNG script."
            prompt = f"{lang_instruction}\nScenario: {scenario}"
            client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=self.api_key)
            stream = client.chat.completions.create(
                model="nvidia/llama-3.3-nemotron-super-49b-v1",
                messages=[{"role": "user", "content": prompt}],
                stream=True
            )
            result = "".join(chunk.choices[0].delta.content for chunk in stream if chunk.choices[0].delta.content)
            st.code(result, language="python" if "PyTest" in language else "java")
            st.download_button("📥 Download", io.BytesIO(result.encode("utf-8")), f"test.{ 'py' if 'PyTest' in language else 'java'}")
