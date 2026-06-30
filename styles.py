import streamlit as st


def load_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f5f7fa;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1400px;
        }

        .main-title {
            font-size: 40px;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 0.25rem;
        }

        .subtitle {
            font-size: 17px;
            color: #475569;
            margin-bottom: 2rem;
        }

        .section-card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            padding: 22px;
            box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
            margin-bottom: 18px;
        }

        .module-title {
            font-size: 24px;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.5rem;
        }

        .module-description {
            font-size: 15px;
            color: #475569;
            line-height: 1.6;
        }

        .small-label {
            font-size: 13px;
            color: #64748b;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 0.25rem;
        }

        .feature-list {
            color: #334155;
            font-size: 15px;
            line-height: 1.7;
        }

        .divider {
            height: 1px;
            background-color: #e2e8f0;
            margin: 1.5rem 0;
        }

        div[data-testid="stMetric"] {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            padding: 18px;
            border-radius: 14px;
            box-shadow: 0 3px 10px rgba(15, 23, 42, 0.05);
        }
        </style>
        """,
        unsafe_allow_html=True
    )