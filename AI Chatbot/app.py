import streamlit as st
import os
import sys

# Set page config at the very beginning
st.set_page_config(page_title='Ayurvedic Health Assistant', layout="wide", initial_sidebar_state="expanded")

# Import after setting page config
from Doshas_prediction import show_predict_page

def show_symptom_page():
    # Add the streamlit directory to the path
    streamlit_dir = os.path.join(os.path.dirname(__file__), 'streamlit')
    sys.path.append(streamlit_dir)
    
    # Import the main function from the streamlit app
    # We need to import the module directly, not from streamlit.app
    import importlib.util
    
    # Get the path to the streamlit app.py file
    app_path = os.path.join(streamlit_dir, 'app.py')
    
    # Load the module
    spec = importlib.util.spec_from_file_location("streamlit_app", app_path)
    streamlit_app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(streamlit_app)
    
    # Run the main function
    streamlit_app.main()

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dosha Prediction", "Disease Identification"])

# Display the selected page
if page == "Dosha Prediction":
    show_predict_page()
else:
    show_symptom_page()
