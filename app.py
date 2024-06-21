import streamlit as st
import os

# Fetch environment variables
short_value = os.environ.get('Short', 'not found')
normal_value = os.environ.get('Normal', 'not found')
long_value = os.environ.get('Long', 'not found')

# Display text with labels
st.text(f"Short: {short_value}")
st.text(f"Normal: {normal_value}")
st.text(f"Long: {long_value}")
