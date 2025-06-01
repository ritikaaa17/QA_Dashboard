
import pandas as pd

class SampleData:
    @staticmethod
    def load():
        return pd.DataFrame({
            "TestCaseID": [f"TC{i:03}" for i in range(1, 21)],
            "Module": ["Login", "Search", "Checkout", "Profile", "Login"] * 4,
            "Status": ["Pass", "Fail", "Pass", "Pass", "Fail"] * 4,
            "ExecutionTime": [5, 8, 4, 6, 10, 7, 3, 4, 6, 11, 9, 5, 4, 6, 12, 3, 5, 6, 10, 7],
            "ExecutedOn": pd.date_range(start="2024-01-01", periods=20, freq="D"),
            "DefectSeverity": ["Low", "High", "Medium", "Low", "Critical"] * 4
        })
