import streamlit as st
import numpy as np
import pandas as pd
import pickle

classifier = pickle.load(open('Model.pkl' , 'rb'))

def diab_pred(input_data):
    input_data_as_nparray = np.asarray(input_data)
    input_data_reshaped = input_data_as_nparray.reshape(1,-1)


    pred = classifier.predict(input_data_reshaped)
    print(pred)
    if (pred[0] == 0):
        return " You dont have diabates"
    else:
        return  " You have diabates "

def main():
     st.title('Diabates Prediction')
     options = [" Male ", "Female"]
     gender = st.selectbox("Enter your gender ", options)
     if gender == "Female":
         Pregnancies = st.number_input(" Enter your pregnancies", key = "demo")
     else:
         Pregnancies = 0

     Glucose = st.number_input(" Enter your Glucose" , key="input1" )
     BloodPressure = st.number_input(" Enter your BloodPressure" , key="input2")
     SkinThickness = st.number_input(" Enter your SkinThickness" , key="input3")
     Insulin = st.number_input(" Enter your Insulin" , key="input4")
     BMI = st.number_input(" Enter your BMI " , key="input10" , min_value=0.1 )



     DiabetesPedigreeFunction = st.number_input(" Enter your Diabetes Pedigree Function" , key="input7" )
     Age = st.number_input(" Enter your Age" , key="input8")


     diagnosis = ''

     if st.button('Diabates Prediction Test'):
         input_data = [[Pregnancies , Glucose , BloodPressure , SkinThickness , Insulin , BMI , DiabetesPedigreeFunction , Age]]
         diagnosis = diab_pred(input_data)
         st.success(diagnosis)

if __name__ == '__main__':
    main()
