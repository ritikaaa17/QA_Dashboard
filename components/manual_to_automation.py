import streamlit as st
import io
from openai import OpenAI

#Model used: llama-3.3-nemotron-super-49b-v1
class ManualToAutomation:
    def __init__(self, api_key):
        self.api_key = api_key

    def convert(self):
        st.markdown("Model Used: llama-3.3-nemotron-super-49b-v1")
        manual_description = st.text_area(
            "Enter a manual test case description (e.g., steps, inputs, expected behavior):",
            placeholder="e.g., Go to login page → Enter valid credentials → Click login → Verify dashboard is displayed"
        )
        language = st.selectbox("Preferred Automation Language", ["Python (PyTest)", "Java (TestNG)"])
        if st.button("Convert to Automation Script") and manual_description:
            lang_prompt = (
                "Convert the following manual test case into an automated script using "
                + ("PyTest in Python" if language.startswith("Python") else "TestNG in Java")
                + ". Include setup, actions, assertions, and comments. Provide only the code output without explanations."
            )

            client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=self.api_key)
            try:
                stream = client.chat.completions.create(
                    model="nvidia/llama-3.3-nemotron-super-49b-v1",
                    messages=[
                        {"role": "system", "content": "You are a senior QA automation engineer."},
                        {"role": "user", "content": f"{lang_prompt}\n\nManual Steps: {manual_description}"}
                    ],
                    temperature=0.2,
                    top_p=0.9,
                    max_tokens=1500,
                    stream=True
                )
                code_output = ""
                for chunk in stream:
                    delta = chunk.choices[0].delta
                    if delta.content:
                        code_output += delta.content
                st.success("Generated Automation Code")
                st.code(code_output, language="python" if "Python" in language else "java")
                st.download_button("💾 Download Script", io.BytesIO(code_output.encode("utf-8")), "automated_test_script.txt")
            except Exception as e:
                st.error(f"❌ Error: {e}")
