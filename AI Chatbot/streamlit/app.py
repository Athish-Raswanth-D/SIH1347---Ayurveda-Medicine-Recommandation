import streamlit as st
import pandas as pd
import os

# Load the dataset
@st.cache
def load_data():
    # Get the absolute path to the medicines.csv file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'medicines.csv')
    data = pd.read_csv(data_path)
    return data

# Extract unique symptoms
@st.cache
def get_unique_symptoms(data):
    symptoms = data['Symptom'].dropna().unique()
    return sorted(symptoms)

# Streamlit app
def main():
    # Add a header with styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #1E88E5;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
    <div class="main-header">Disease and Medicine Finder</div>
    <div class="sub-header">Identify diseases and recommended medicines based on symptoms</div>
    """, unsafe_allow_html=True)
    
    # Load data
    data = load_data()
    
    # Get unique symptoms
    symptoms = get_unique_symptoms(data)
    
    # Create two columns for search and filter
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # User input for symptom
        user_input = st.text_input("Enter a symptom:", "")
    
    with col2:
        # Add a button to clear the search
        if st.button("Clear Search"):
            user_input = ""
    
    # Filter symptoms based on user input
    filtered_symptoms = sorted([symptom for symptom in symptoms if user_input.lower() in symptom.lower()])
    
    # Show the number of matching symptoms
    if user_input:
        st.write(f"Found {len(filtered_symptoms)} matching symptoms")
    
    # Dropdown for symptoms with a descriptive label
    selected_symptom = st.selectbox("Select a symptom from the list:", options=filtered_symptoms)
        
    if selected_symptom:
        # Filter the dataset based on the selected symptom
        filtered_data = data[data['Symptom'].str.contains(selected_symptom, case=False, na=False)]
        
        if not filtered_data.empty:
            # Get unique diseases for the selected symptom
            unique_diseases = filtered_data['disease'].unique()
            
            # Display disease information
            st.subheader("Diseases associated with this symptom:")
            for disease in unique_diseases:
                with st.expander(f"🔍 {disease}"):
                    disease_info = filtered_data[filtered_data['disease'] == disease]
                    st.write(f"**Description:** {disease_info['Symptom'].iloc[0]}")
                    
                    # Display medicines for this disease
                    st.write("**Recommended Medicines:**")
                    medicines_data = disease_info[['Name of Medicine', 'Main Indications', 'Dose', 'Precaution/ Contraindication']]
                    st.dataframe(medicines_data)
        else:
            st.write("No medicines or diseases found for the selected symptom.")
    
if __name__ == '__main__':
    main()
