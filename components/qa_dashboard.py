import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from components.sample_data import SampleData

class QADashboard:
    def __init__(self):
        self.df = SampleData.load()

    def display(self, api_key):

        df = self.df
        st.subheader("🔍 Data Preview")
        st.dataframe(df)

        st.subheader("📈 Select Columns for Bar Chart")
        categorical_col = st.selectbox("Select X-axis (categorical column)", df.columns, key="cat_col")
        numerical_col = st.selectbox("Select Y-axis (numerical column)", df.select_dtypes(include=["number"]).columns, key="num_col")

        if st.button("Generate Bar Chart", key="generate_chart"):
            fig, ax = plt.subplots()
            sns.barplot(x=df[categorical_col], y=df[numerical_col], ax=ax)
            ax.set_title(f"{numerical_col} by {categorical_col}")
            ax.set_xlabel(categorical_col)
            ax.set_ylabel(numerical_col)

            # ✅ Rotate x-axis labels for better readability
            plt.xticks(rotation=45, ha='right')

            # ✅ Improve layout
            fig.tight_layout()

            st.pyplot(fig)
