import requests
import streamlit as st
import io
from openai import OpenAI


#Model used: microsoft/phi-4-multimodal-instruct
class LogSummarizer:
    def summarize(self):
        st.markdown("Model Used: microsoft/phi-4-multimodal-instruct")
        uploaded_file = st.file_uploader("Upload a log file (.log or .txt)", type=["log", "txt"], key="phi4")
        if uploaded_file and st.button("Summarize Logs with phi-4"):
            log_text = uploaded_file.read().decode("utf-8")
            prompt = (
                "You're a senior QA engineer reviewing logs from automated test executions. "
                "Summarize the log file clearly and professionally. Highlight the following:"
                "- ✅ Passed and skipped test cases"
                "- ❌ Categorized errors and warnings"
                "- 🧠 Likely root causes and their context"
                "- 🔧 Human-friendly suggestions for fixing issues"
                "Make the output clean, readable, and suitable for sharing with both QA and development teams."
            )
            payload = {
                "model": "microsoft/phi-4-multimodal-instruct",
                "messages": [
                    {"role": "system", "content": "You are a log analysis assistant."},
                    {"role": "user", "content": f"{prompt}{log_text}"}
                ],
                "max_tokens": 1000,
                "temperature": 0.10,
                "top_p": 0.70,
                "frequency_penalty": 0.00,
                "presence_penalty": 0.00,
                "stream": False
            }
            headers = {
                "Authorization": "Bearer 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",
                "Accept": "application/json"
            }
            try:
                response = requests.post("https://integrate.api.nvidia.com/v1/chat/completions", headers=headers, json=payload)
                if response.status_code == 200:
                    result = response.json()['choices'][0]['message']['content']
                    st.success("Human-Readable Summary Generated ✅")
                    st.text_area("🧠 AI Log Summary", value=result, height=600)
                    file = io.BytesIO(result.encode("utf-8"))
                    st.download_button("💾 Download Summary", file, "phi4_log_summary.txt")
                else:
                    st.error(f"❌ API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"❌ Exception: {e}")