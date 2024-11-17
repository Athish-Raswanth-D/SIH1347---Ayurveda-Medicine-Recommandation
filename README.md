Ayurvedic Medicine Symptom-Based Medication Recommender

This project uses Streamlit to provide medication suggestions based on given symptoms. When a user inputs a symptom name, the app fetches the relevant medications from a CSV file and displays them.

Features

- Input a symptom name.
- Display medications related to the input symptom.
- CSV file-based data storage for symptoms and medications.

Requirements

- Python 3.x
- Streamlit
- Pandas

Installation

1. Clone the repository or download the project files.
   
   git clone <repository-link>

2. Install the required libraries:

   pip install -r requirements.txt

3. Make sure you have the CSV file containing symptom-medication data in the project directory.

Running the Project

To run the Streamlit app, open a terminal in the project directory and use the following command:

   streamlit run app.py

This will open the app in your default browser.

Demo

You can try out the live demo of the project at: [Demo Link](<your-demo-link>)

Usage

1. Open the app in your browser.
2. Type the name of a symptom (e.g., "headache") in the input box.
3. The app will display the medications associated with that symptom from the CSV file.

Example

Input:
Symptom: Headache

Output:
Recommended Medications: 
1. Paracetamol
2. Ibuprofen
3. Aspirin

Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are always welcome!

License

This project is open-source and available under the [MIT License](LICENSE).
