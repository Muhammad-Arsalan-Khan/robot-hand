import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Robot Hand Writer", layout="wide")
html = open("robot-hand.html", encoding="utf-8").read()
components.html(html, height=700, scrolling=False)