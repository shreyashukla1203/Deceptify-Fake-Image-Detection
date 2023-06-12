import streamlit as st
import dashboard
import classifyPage

st.set_page_config(
    page_title="Deceptify",
    page_icon="🤖",
    layout="wide")

PAGES = {
    "Dashboard": dashboard,
    
}

st.sidebar.title("DECEPTIFY")

st.sidebar.write("Deceptify is a tool that utilizes the power of Deep Learning to distinguish Real images from the Fake ones.")

st.sidebar.subheader('Navigation:')
selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()