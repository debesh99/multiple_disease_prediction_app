import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
# option menu(first install sstreamlit-option-menu)
from streamlit_option_menu import option_menu

# rad = st.sidebar.radio ("**Multiple Disease Prediction System**",["Diabetes Prediction","Heart Disease Prediction"])

with st.sidebar:
    rad = option_menu("Multiple Disease Prediction System",
                      ["Diabetes Prediction","Heart Disease Prediction"],
                      icons=['activity','heart'])
# For icons we just have to mention the icon names from bootstrap
# Loading the saved models
# diabetes_model = pickle.load(open('../trained_model/diabetes_trained_model.sav','rb'))
# diabetes_standard_scaler = pickle.load((open('../trained_model/diabetes_standard_scaler.sav','rb')))
# heart_disease_model = pickle.load(open('../trained_model/heart_disease_trained_model.sav','rb'))
# Diabetes
if rad=="Diabetes Prediction":
    st.title("Diabetes Prediction using ML")

    col1,col2,col3 = st.columns(3)
    # Line 1
    with col1:
        no_of_pregnancy = st.text_input("Number of Pregnancies")
    with col2:
        glucose = st.text_input("Glucode Level")
    with col3:
        blood_pressure = st.text_input("Blood Pressure Level")

    # Line 2
    with col1:
        skin_thickness = st.text_input("Skin Thickness Value")
    with col2:
        insulin = st.text_input("Insulin Level")
    with col3:
        bmi = st.text_input("BMI Value")

    # Line 3
    with col1:
        diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        age = st.text_input("Age of the Person")
    

    if st.button("Diabetes test result"):
        # input data
        input_data = np.array([no_of_pregnancy, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age])

        input_data_reshaped = input_data.reshape(1,-1)
        df = diabetes_standard_scaler.transform(input_data_reshaped)

        # prediction
        diabetes_prediction = diabetes_model.predict(df)

        if diabetes_prediction[0]==0:
            st.success("Not diabetic")
        else:
            st.success("Diabetic")


# Heart
if rad=="Heart Disease Prediction":
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    

    if st.button("Heart Disease Test Results"):
        input_data_heart = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        input_data_heart_reshaped = input_data_heart.reshape(1,-1)
        
        # prediction
        heart_prediction = heart_disease_model.predict(input_data_heart_reshaped)

        if heart_prediction[0]==0:
            st.success("No heart disease")
        else:
            st.success("Heart disease detected")
