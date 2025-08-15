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

#Sidebar Content

st.sidebar.title("🩺Diabetes Prediction App")

#About this App
st.sidebar.subheader("ℹ️About This App")
st.sidebar.write(
		"""
		This app predicts whether the user have diabetes or not
		using machine learning based on health parameters.
		Built with **Python, Streamlit, and scikit-learn**.
		"""
)

#About Diabetes
st.sidebar.subheader("🤔About Diabetes")
st.sidebar.write(
	"""
	Diabetes is a condition that occurs when blood glucose is too high.
	Healthy diet,regular exercise and timely checkups can help prevent
	or manage diabetes.
	"""
)

#How To Use
st.sidebar.subheader("🛠️How To Use")
st.sidebar.write(
	"""
	1. Fill in the health details in the form.
	2. Click **Predict** to get your results
	3. Use the results for awareness only.
	4. Always consult a doctor for medical advice👨‍⚕️.
	"""
)

#Contact
st.sidebar.subheader("💌Contact & Links")
st.sidebar.markdown("https://github.com/Mihir-swain3096/diabetes-prediction-app")
st.sidebar.write("**Email**:mihirswain38@gmail.com")


	
 
from pickle import load

#Load the model
f= open("diabetes.pkl","rb")
model= load(f)
f.close()

#App title
st.title("Diabetes Prediction App")
st.write("Enter details below to check diabetes prediction.")

#Input Details
Pregnancies=st.number_input("Pregnancies",value=None,step=1,placeholder="E.g. 2",help="Number of times the patient has been pregnant (only for females).")
Glucose=st.number_input("Glucose",value=None,step=1,placeholder="E.g. 120",help="Plasma glucose concentration in mg/dL after fasting.")
BloodPressure=st.number_input("BloodPressure",value=None,step=1,placeholder="E.g. 80",help="Diastolic blood pressure in mm Hg.")
SkinThickness=st.number_input("SkinThickness",value=None,step=0.1,placeholder="E.g. 35",help="Triceps skin fold thickness in mm.")
Insulin=st.number_input("Insulin",value=None,step=0.1,placeholder="E.g. 85",help="2-hour serum insulin level in μU/mL.")
BMI=st.number_input("BMI",value=None,step=0.1,placeholder="Enter BMI",help="Body Mass Index = weight(kg) / height(m)^2.")
DiabetesPedigreeFunction=st.number_input("DiabetesPedigreeFunction",value=None,step=0.01,placeholder="Enter pedigree function value",help="Indicates the likelihood of diabetes based on family history.Higher value= more risk.")
Age= st.number_input("Age",value=None,placeholder="Enter Age")

#Predict Button
if st.button("Predict"):
	data=[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI , DiabetesPedigreeFunction,Age]]
	result= model.predict(data)[0]
	probability = model.predict_proba(data)[0][1]*100
	if result==1:
		st.error(f"You are likely to have diabetes.\n\n**Risk Level:**{probability:.2f}%")
	else:
		st.success(f"You are unlikely to have diabetes.\n\n**Risk Level:**{probability:.2f}%")
		st.balloons()
