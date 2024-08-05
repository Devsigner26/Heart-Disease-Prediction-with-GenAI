
import os
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.google_gemini import GoogleGemini
from fpdf import FPDF

# Initialize the LLM with API key
llm = GoogleGemini(api_key=os.environ.get("API_KEY", "AIzaSyDAfgAOBDfss-NdZ2srBmvm2Hek40KemO4"))

# Set the title of the Streamlit app
st.title("Heart Disease Prediction with GenerativeAI")

# CSS styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        color: #333;
    }
    .stApp {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #ddd;
        padding: 10px;
        width: 100%;
    }
    .stMarkdown>div>div {
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the static CSV file
data = pd.read_csv("heart.csv") 
#st.write(data.head(3))

# Create a SmartDataframe
df = SmartDataframe(data, config={"llm": llm})

# Input fields for patient data
name = st.text_input("Name:")
age = st.text_input("Age:")
sex = st.text_input("Sex:")
cp = st.text_input("Chest Pain Type (cp):")
trestbps = st.text_input("Resting Blood Pressure (trestbps):")
chol = st.text_input("Serum Cholesterol (chol):")
fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (fbs):")
restecg = st.text_input("Resting Electrocardiographic Results (restecg):")
thalach = st.text_input("Maximum Heart Rate Achieved (thalach):")
exang = st.text_input("Exercise Induced Angina (exang):")
oldpeak = st.text_input("ST Depression Induced by Exercise (oldpeak):")
slope = st.text_input("Slope of the Peak Exercise ST Segment (slope):")
ca = st.text_input("Number of Major Vessels Colored by Fluoroscopy (ca):")
thal = st.text_input("Thalassemia (thal):")

# Function to generate PDF
def generate_pdf(name, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Heart Disease Prediction Report for {name}", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=result, ln=True, align='C')
    pdf.output(f"{name}_heart_disease_report.pdf")
    return f"{name}_heart_disease_report.pdf"

# Button to check for heart disease
if st.button("Check Heart Disease"):
    if all([name, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
        try:
            age = int(age)
            trestbps = int(trestbps)
            chol = int(chol)
            fbs = int(fbs)
            thalach = int(thalach)
            oldpeak = float(oldpeak)
            slope = int(slope)
            ca = int(ca)
            thal = int(thal)
            
            patient_data = f"age: {age}, sex: {sex}, cp: {cp}, trestbps: {trestbps}, chol: {chol}, fbs: {fbs}, restecg: {restecg}, thalach: {thalach}, exang: {exang}, oldpeak: {oldpeak}, slope: {slope}, ca: {ca}, thal: {thal}"
            prompt = f"Does the patient named {name} with the following data have heart disease? {patient_data} Answer with 'Yes' or 'No'."
            
            with st.spinner("Generating response..."):
                response = df.chat(prompt)
                # Display only 'Yes' or 'No' in response
                if 'yes' in response.lower():
                    result = f"Yes, {name} has heart disease."
                    st.success(result)
                elif 'no' in response.lower():
                    result = f"No, {name} does not have heart disease."
                    st.success(result)
                else:
                    result = "Unable to determine from the provided data."
                    st.warning(result)

                # Generate PDF with the result
                pdf_file = generate_pdf(name, result)
                st.download_button(
                    label="Download Report",
                    data=open(pdf_file, "rb").read(),
                    file_name=f"{name}_heart_disease_report.pdf",
                    mime="application/pdf"
                )
        except ValueError:
            st.warning("Please enter valid numeric values for age, blood pressure, cholesterol, fasting blood sugar, maximum heart rate, oldpeak, slope, ca, and thal.")
    else:
        st.warning("Please fill in all the fields!")


