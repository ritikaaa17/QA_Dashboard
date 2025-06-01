
import streamlit as st
import io
import requests

#model used: mistral-medium-3-instruct
class TestPlanSummarizer:
    def summarize_test_plan(test_plan_text):

        invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
        headers = {
            "Authorization": "Bearer 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",
            "Accept": "application/json"
        }

        prompt = (
            "You are an expert QA test strategist. Summarize the following test plan clearly. "
            "List key areas covered, identify any missing coverage, highlight risks or blockers, "
            "and give a go/no-go recommendation with reasoning.\n\n"
            f"{test_plan_text}"
        )

        payload = {
            "model": "mistralai/mistral-medium-3-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000,
            "temperature": 0.7,
            "top_p": 0.95,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
            "stream": False
        }

        try:
            response = requests.post(invoke_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"❌ Error while summarizing test plan: {e}"

    def handle_uploaded_test_plan(container):
        with container:
            st.markdown("### <span style='color:#76B900'>📋 Test Plan Summarizer</span>", unsafe_allow_html=True)
            st.markdown("Model Used: mistral-medium-3-instruct")
            test_plan_text = st.text_area("Paste your test plan here:", height=300, key="plan_input_area")

            if st.button("Summarize Test Plan", key="btn_summarize_text"):
                with st.spinner("Summarizing..."):
                    result = TestPlanSummarizer.summarize_test_plan(test_plan_text)
                    st.success("Summary Generated:")
                    st.text_area("Summary Output", value=result, height=500, key="summary_output_text")
                    st.download_button("💾 Download Summary", data=result, file_name="test_plan_summary.txt")

            uploaded_file = st.file_uploader("📤 Upload Test Plan File (TXT)", type="txt", key="upload_file_tab")
            if uploaded_file is not None:
                test_plan_text = uploaded_file.read().decode("utf-8")

                if st.button("Summarize Uploaded Test Plan", key="btn_summarize_upload"):
                    with st.spinner("Summarizing..."):
                        result = TestPlanSummarizer.summarize_test_plan(test_plan_text)
                        st.success("Summary Generated:")
                        st.text_area("Summary Output", value=result, height=500, key="summary_uploaded_text")
                        st.download_button("💾 Download Summary", data=result, file_name="uploaded_test_plan_summary.txt")

                st.subheader("📈 Key Metrics from Uploaded Test Plan")
                lines = test_plan_text.strip().split("\n")
                total_lines = len(lines)
                scenario_lines = [line for line in lines if line.strip().startswith("1.") or line.strip().startswith("-")]
                risks = [line for line in lines if "risk" in line.lower()]
                out_of_scope = [line for line in lines if "out of scope" in line.lower()]
                dependencies = [line for line in lines if "dependency" in line.lower() or "dependent" in line.lower()]

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("📄 Total Lines", total_lines)
                col2.metric("🧪 Test Scenarios", len(scenario_lines))
                col3.metric("⚠️ Risks", len(risks))
                col4.metric("🔗 Dependencies", len(dependencies))

                st.divider()
                st.subheader("🧠 AI-Based Validation of Test Plan Quality")
                validate_prompt = (
                    "You're a senior QA architect. Evaluate the following test plan for completeness, risks, and test coverage. "
                    "Highlight any missing critical areas. Only include your analysis and suggestions.\n\n"
                    + test_plan_text
                )
                if st.button("Run QA Validation", key="btn_validation"):
                    with st.spinner("Reviewing with AI..."):
                        validation_result = TestPlanSummarizer.summarize_test_plan(validate_prompt)
                        st.success("Validation Feedback:")
                        st.text_area("AI Review Output", value=validation_result, height=500, key="validation_result_text")
