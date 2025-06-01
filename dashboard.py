from components.root_cause_ai_helper import RootCauseSuggestion
import streamlit as st
from components.ai_log_summarizer import LogSummarizer
from components.manual_to_automation import ManualToAutomation
from components.sample_data import SampleData
from components.qa_dashboard import QADashboard
from components.ai_qa_assistant import AIQA
from components.test_generator import TestCodeGenerator
from components.test_plan_summarizer import TestPlanSummarizer
from components.rtm_matrix import RTMBuilder


def main():
    st.set_page_config(layout="wide")
    st.markdown("""
    <h1 style='color:#76B900; font-size: 2.5em; font-weight:700; margin-bottom: 0;'>
        🧪 Unified QA Automation Dashboard
    </h1>
    <p style='color:#BBBBBB; font-size:1.1em; margin-top: 0.2em;'>
        Powered by NVIDIA AI APIs for smarter testing and visualization
    </p>
""", unsafe_allow_html=True)

    api_key = "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"
    df = SampleData.load()

    tabs = st.tabs([
        "📊 Dashboard Overview",
        "🤖 QA Assistant",
        "🧠 Test Code Generator",
        "📋 Test Plan Summarizer",
        "📋 Log Summarizer",
        "🔄 Manual testcase to Automated script Converter",
        "🧾 RTM Builder",
        "🧠 Root Cause Suggestion"
    ])

    with tabs[0]:
        st.markdown("### <span style='color:#76B900'>📊 Dashboard Overview</span>", unsafe_allow_html=True)
        QADashboard().display(api_key)

    with tabs[1]:
        st.markdown("### <span style='color:#76B900'>🤖 AI-Powered QA Assistant (Testcase generator)</span>", unsafe_allow_html=True)
        AIQA(api_key).ask()

    with tabs[2]:
        st.markdown("### <span style='color:#76B900'>🧠 Test Case Code Generator</span>", unsafe_allow_html=True)
        TestCodeGenerator(api_key).generate()

    TestPlanSummarizer.handle_uploaded_test_plan(tabs[3])
    
    with tabs[4]:
        st.markdown("### <span style='color:#76B900'>📋 AI Log Summarizer</span>", unsafe_allow_html=True)
        LogSummarizer().summarize()
    
    with tabs[5]:
        st.markdown("### <span style='color:#76B900'>🔄 Manual testcase to Automated script Convertert</span>", unsafe_allow_html=True)
        ManualToAutomation(api_key).convert()
    
    with tabs[6]:  
        st.markdown("### <span style='color:#76B900'>📋 Requirement Traceability Matrix (RTM) Builder</span>", unsafe_allow_html=True)
        RTMBuilder(api_key).display()
    
    with tabs[7]:
        st.markdown("### <span style='color:#76B900'>🧠 Root Cause Suggestion Engine</span>", unsafe_allow_html=True)
        RootCauseSuggestion(api_key).display()


if __name__ == "__main__":
    main()
