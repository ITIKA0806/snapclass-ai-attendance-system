import streamlit as st


def footer_home():
    
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown("""
    <div style="
        margin-top:2rem;
        display:flex;
        gap:6px;
        justify-content:center;
        align-items:center;
        color:white;
        font-size:16px;
        font-weight:bold;
    ">
        Created with ❤️ by Itika Singh
    </div>
""", unsafe_allow_html=True)