# Import standard libraries


# Import third party libraries
import streamlit as st


st.title("Getting Started")

with open("README.md", "r") as README:
    introduction = README.read()

st.write(introduction)
