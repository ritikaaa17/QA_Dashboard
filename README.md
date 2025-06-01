**🧪 Unified QA Automation Dashboard**


A powerful, AI-augmented dashboard for managing, visualizing, and accelerating the Quality Assurance (QA) process using NVIDIA’s Build API suite.

**🚀 Features**

1. 📊 QA Dashboard

 - Visualize test execution trends and status breakdown

 - Dynamic bar charts from test data

2. 🤖 QA Assistant
  - Ask test-related queries (like test ideas, edge cases, etc.)

  - Powered by llama-3.3-nemotron-super-49b-v1 from build.nvidia.com

3. 🧠 Test Code Generator
   
  - Converts test scenarios into ready-to-use Python or Java code

  - Powered by llama-3.3-nemotron-super-49b-v1 from build.nvidia.com

4. 📋 Test Plan Summarizer
   
  - Upload lengthy test plans and get concise summaries

  - Suggests missing edge cases

  - Powered by mistral-medium-3-instruc from build.nvidia.com


5. 📋 Log Summarizer
   
  - Paste or upload logs for AI-powered root cause analysis

  - Powered by microsoft/phi-4-multimodal-instruct from build.nvidia.com

7. 🔄 Manual to Automation Converter
   
 - Converts manual test case steps into PyTest or TestNG automation

  - Powered by llama-3.3-nemotron-super-49b-v1 from build.nvidia.com

8. 🧾 RTM Builder
   
  - Paste requirements to generate a full Requirement Traceability Matrix (RTM) 

  - Powered by falcon3-7b-instruct from build.nvidia.com

  - Downloadable in CSV format


9. 🔍 Root Cause Suggestion Engine
    
  - Analyzes failed test cases and provides debugging hints

  - Uses mistral-medium-3-instruct via build.nvidia.com

**🧰 Tech Stack**
 - Frontend: Streamlit

 - Backend: Python, REST

 - AI Models:

    * mistralai/mistral-medium-3-instruct

    * stable-diffusion-3-medium

- Visualization: Matplotlib, Seaborn

- Deployment: Localhost / Streamlit Cloud

**🗂️ Folder Structure**

```
qa_dashboard_project/
├── components/
│   ├── __init__.py
│   ├── ai_log_summarizer.py
│   ├── ai_qa_assistant.py
│   ├── manual_to_automation.py
│   ├── qa_dashboard.py
│   ├── rtm_matrix.py
│   ├── sample_data.py
│   ├── test_generator.py
│   ├── test_plan_summarizer.py
│   ├── root_cause_ai_helper.py
├── dashboard.py
├── requirements.txt
└── README.md
```
**🛠️ Setup**

```
# 1. Clone the repo
git clone https://github.com/ritikaaa17/qa_dashboard.git
cd qa_dashboard_project

# 2. Set up virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run Streamlit app
streamlit run dashboard.py

```
**🔐 API Keys**
```
api_key = "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"
```

