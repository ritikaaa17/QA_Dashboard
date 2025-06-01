import streamlit as st
import pandas as pd
from openai import OpenAI

#Model used: falcon3-7b-instruct
class RTMBuilder:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=self.api_key
        )

    def generate_rtm(self, requirements_text):
        prompt = (
            "You are an expert QA engineer. Given the following requirements, "
            "generate a Requirement Traceability Matrix (RTM) mapping each requirement to corresponding test cases."
            " Format the output in a table with columns: Requirement ID, Description, Test Case ID, Test Case Description."
        )

        try:
            completion = self.client.chat.completions.create(
                model="tiiuae/falcon3-7b-instruct",
                messages=[{"role": "user", "content": prompt + "\n\n" + requirements_text}],
                temperature=0.2,
                top_p=0.7,
                max_tokens=1024,
                stream=False
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"❌ Error while generating RTM: {e}"

    def display(self):
        st.markdown("Model used: falcon3-7b-instruct")
        st.markdown("#### Paste your product requirements below to generate a traceability matrix")

        requirements_text = st.text_area("📄 Requirements Input", height=300, key="rtm_input")

        if st.button("Generate RTM", key="generate_rtm_btn"):
            with st.spinner("Generating RTM using Falcon model..."):
                rtm_result = self.generate_rtm(requirements_text)

                # Display raw text for reference
                st.text_area("🧠 Raw RTM Output", value=rtm_result, height=250)

                # Attempt to parse as a table
                try:
                    # Extract table lines
                    lines = [line.strip() for line in rtm_result.strip().split('\n') if '|' in line and not line.startswith('|---')]
                    cleaned = [line.strip('|').split('|') for line in lines]

                    # Remove empty cells and strip whitespace
                    cleaned = [[cell.strip() for cell in row] for row in cleaned if len(row) > 1]

                    # Create DataFrame
                    df = pd.DataFrame(cleaned[1:], columns=cleaned[0])
                    st.subheader("📊 Parsed RTM Table")
                    st.dataframe(df)

                    # Allow download
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="💾 Download RTM as CSV",
                        data=csv,
                        file_name="requirement_traceability_matrix.csv",
                        mime="text/csv"
                    )
                except Exception as e:
                    st.error(f"⚠️ Failed to parse RTM into table format: {e}")
