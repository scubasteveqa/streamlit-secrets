import streamlit as st
import os

# Fetch environment variables
short_value = os.environ.get('Short', 'not found')
normal_value = os.environ.get('Normal', 'not found')
long_value = os.environ.get('Long', 'not found')
QUARTO_PROFILE = os.environ.get('QUARTO_PROFILE', 'not found')
R_CONFIG_ACTIVE = os.environ.get('R_CONFIG_ACTIVE', 'not found')

# Display text with labels
st.text(f"Short: {short_value}")
st.text(f"Normal: {normal_value}")
st.text(f"Long: {long_value}")
st.text(f"QUARTO_PROFILE: {QUARTO_PROFILE}")
st.text(f"R_CONFIG_ACTIVE : {R_CONFIG_ACTIVE}")
