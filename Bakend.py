# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open("C:\\Users\\aksha\\.spyder-py3\\Mul disease\\diabetes_model.sav", 'rb'), encoding='utf-8')
heart_disease_model = pickle.load(open("C:\\Users\\aksha\\.spyder-py3\\Mul disease\\heart_disease_model.sav", 'rb'), encoding='utf-8')
parkinsons_model = pickle.load(open("C:\\Users\\aksha\\.spyder-py3\\Mul disease\\parkinsons_model.sav", 'rb'), encoding='utf-8')
msc_model = pickle.load(open("C:\\Users\\aksha\\.spyder-py3\\Mul disease\\Msc.sav", 'rb'), encoding='utf-8')

# Custom dark theme
st.markdown(
    """
    <style>
        body {
            color: white;
            background-color: #1e1e1e;
        }
        .css-1aumxhk {
            color: #d1d1d1;
        }
        .css-17eq0hr {
            background-color: #333333;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# sidebar for navigation
with st.sidebar:
    selected = option_menu('My Doctor',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Multiple Sclerosis Prediction',
                           'Introduction'],
                          icons=['activity', 'heart', 'person','gear', 'file-richtext'],
                          default_index=0)
    
# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
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

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict(
            [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
              RPDE, DFA, spread1, spread2, D2, PPE]])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    # Multiple Sclerosis Prediction Page
    if selected == "Multiple Sclerosis Prediction":
        # page title
        st.title("Multiple Sclerosis Disease Prediction using ML")

        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(16)

        with col1:
            gender = st.text_input('Gender')

        with col2:
            age = st.text_input('Age')

        with col3:
            breastfeeding = st.text_input('Breastfeeding')

        with col4:
            varicella = st.text_input('Varicella')

        with col5:
            initial_symptom = st.text_input('Initial Symptom')

        with col6:
            mono_or_polysymptomatic = st.text_input('Mono or Polysymptomatic')

        with col7:
            oligoclonal_bands = st.text_input('Oligoclonal Bands')

        with col8:
            llsep = st.text_input('LLSSEP')

        with col9:
            ulssep = st.text_input('ULSSEP')

        with col10:
            vep = st.text_input('VEP')

        with col11:
            baep = st.text_input('BAEP')

        with col12:
            periventricular_mri = st.text_input('Periventricular MRI')

        with col13:
            cortical_mri = st.text_input('Cortical MRI')

        with col14:
            infratentorial_mri = st.text_input('Infratentorial MRI')

        with col15:
            spinal_cord_mri = st.text_input('Spinal Cord MRI')

        # Perform one-hot encoding for 'gender'
        gender_encoded = 1 if gender.lower() == 'female' else 0

        # code for Prediction
        msc_diagnosis = ''

        # creating a button for Prediction
        if st.button("Multiple Sclerosis Test Result"):
            # Modify this line to match your model's feature order and structure
            msc_prediction = msc_model.predict([[gender_encoded, age, breastfeeding, varicella, initial_symptom,
                                                 mono_or_polysymptomatic, oligoclonal_bands, llsep, ulssep,
                                                 vep, baep, periventricular_mri, cortical_mri, infratentorial_mri,
                                                 spinal_cord_mri]])

            if msc_prediction[0] == 1:
                msc_diagnosis = "The person has Multiple Sclerosis Disease"
            else:
                msc_diagnosis = "The person does not have Multiple Sclerosis Disease"

        st.success(msc_diagnosis)
    
    # Introduction Page
if selected == 'Introduction':
    st.title('My Doctor - Multiple Disease Prediction System')
    st.write(
        """
        Welcome to My Doctor, a Multiple Disease Prediction System. This application helps predict various diseases 
        such as diabetes, heart disease, and Parkinson's. Please navigate through the sidebar to access different 
        prediction pages. After making predictions, you can provide personal details for a final comprehensive report. 
        Let's get started!
        """
    )



