import streamlit as st
import pandas as pd
import requests

class RootCauseSuggestion:
    def __init__(self, api_key):
        self.api_key = api_key
        self.sample_failures = pd.DataFrame({
            "TestCaseID": ["TC_101", "TC_203", "TC_305"],
            "Module": ["Login", "Checkout", "Profile"],
            "ErrorLog": [
                "Traceback: ElementNotFoundException at line 54 in login_test.py",
                "TimeoutError: Payment gateway response exceeded 30s",
                "AssertionError: Profile picture upload failed with 500 response"
            ]
        })

    def call_ai_model(self, error_log):
        url = "https://integrate.api.nvidia.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }
        prompt = (
            "Given this error log from an automated test, summarize the issue, identify the root cause, and suggest a fix."
        )

        payload = {
            "model": "mistralai/mistral-medium-3-instruct",
            "messages": [
                {"role": "user", "content": prompt + "\n\n" + error_log}
            ],
            "max_tokens": 800,
            "temperature": 0.4
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"❌ Failed to get AI suggestion: {e}"

    def display(self):
        st.markdown("Model used: mistralai/mistral-medium-3-instruct via build.nvidia.com")

        st.markdown("Select a failed test case to view AI-generated analysis")
        df = self.sample_failures
        st.dataframe(df)

        selected = st.selectbox("Choose a TestCaseID", df["TestCaseID"].tolist())
        error_log = df[df["TestCaseID"] == selected]["ErrorLog"].values[0]

        if st.button("🔍 Analyze Root Cause"):
            with st.spinner("Analyzing log with AI model..."):
                suggestion = self.call_ai_model(error_log)
                st.subheader("🔎 Suggested Root Cause & Fix")
                st.markdown(suggestion)

        st.caption("Model used: mistralai/mistral-medium-3-instruct via build.nvidia.com")
