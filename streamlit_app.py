import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('Liver2.pkl', 'rb'))

# Set page title and background
st.title("Liver Disease Prediction")

# Add custom CSS for background and styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/SagarDhandare/Liver-Disease-Prediction-Project/main/Images/Liver.jpg");
        background-size: cover;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create input form
with st.form("prediction_form"):
    st.header("Patient Details")
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age (Years)", min_value=0, max_value=120, step=1)
        total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, format="%.1f")
        alkaline_phosphotase = st.number_input("Alkaline Phosphotase", min_value=0, step=1)
        aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0, step=1)
        
    with col2:
        gender = st.number_input("Gender (Male=1, Female=0)", min_value=0, max_value=1, step=1)
        alamine_aminotransferase = st.number_input("Alamine Aminotransferase", min_value=0, step=1)
        total_protiens = st.number_input("Total Protiens", min_value=0.0, format="%.1f")
        albumin = st.number_input("Albumin", min_value=0.0, format="%.1f")
    
    albumin_globulin_ratio = st.number_input("Albumin and Globulin Ratio", min_value=0.0, format="%.1f")
    
    submitted = st.form_submit_button("Predict")

# Handle form submission
if submitted:
    # Create feature array
    input_data = np.array([[age, gender, total_bilirubin, alkaline_phosphotase,
                          alamine_aminotransferase, aspartate_aminotransferase,
                          total_protiens, albumin, albumin_globulin_ratio]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display results
    if prediction == 2:
        st.error("""
        Oops! 🙁
        \nYou have LIVER DISEASE
        \nPlease Consult a Doctor.
        """)
        st.image("https://raw.githubusercontent.com/SagarDhandare/Liver-Disease-Prediction-Project/main/static/dr.gif")
    elif prediction == 1:
        st.success("""
        🤩 Congratulations! 🤩
        \nYou DON'T have LIVER DISEASE.
        """)
        st.image("https://raw.githubusercontent.com/SagarDhandare/Liver-Disease-Prediction-Project/main/static/yes.webp")

# Footer
st.markdown(
    '<div class="footer">©2021 Sagar Dhandare</div>',
    unsafe_allow_html=True
)