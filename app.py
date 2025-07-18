import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1624454002429-40ed87a5ec04?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

 
from pickle import load

#Load the model
f= open("diabetes.pkl","rb")
model= load(f)
f.close

#App title
st.title("Diabetes Prediction App")
st.write("Enter details below to check diabetes prediction.")

#Input Details
Pregnancies=st.number_input("Pregnancies",placeholder="Enter Number")
Glucose=st.number_input("Glucose",placeholder="Enter Number")
BloodPressure=st.number_input("BloodPressure",placeholder="Enter Number")
SkinThickness=st.number_input("SkinThickness",placeholder="Enter Number")
Insulin=st.number_input("Insulin",placeholder="Enter Number")
BMI=st.number_input("BMI",placeholder="Enter Number")
DiabetesPedigreeFunction=st.number_input("DPF",placeholder="Enter Number")
Age= st.number_input("Age",placeholder="Enter Number")

#Predict Button
if st.button("Predict"):
	data=[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI , DiabetesPedigreeFunction,Age]]
	result= model.predict(data)[0]

	if result==1:
		st.error("You are likely to have diabetes")
	else:
		st.success("You are unlikely to have diabetes")

