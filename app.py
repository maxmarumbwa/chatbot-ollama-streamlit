import streamlit as st

st.title("My First Streamlit App")

st.write("Hello, world!")

st.text("This is a simple text output.")
# Add an interactive slider

number = st.slider("Pick a number", 0, 100, 25)

st.write("You picked:", number)
