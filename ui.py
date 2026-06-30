import streamlit as st


def page_header(title, description):
    st.markdown(
        f"""
        <div class="main-title">{title}</div>
        <div class="subtitle">{description}</div>
        """,
        unsafe_allow_html=True
    )


def section_card(title, description):
    st.markdown(
        f"""
        <div class="section-card">
            <div class="module-title">{title}</div>
            <div class="module-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(title, items):
    list_items = "".join([f"<li>{item}</li>" for item in items])

    st.markdown(
        f"""
        <div class="section-card">
            <div class="module-title">{title}</div>
            <ul class="feature-list">
                {list_items}
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )