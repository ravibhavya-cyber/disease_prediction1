import os
import pickle  # Pre-trained model loading
import streamlit as st  # Web app
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")



st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .main-title {
            color: #0e76a8;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            padding: 10px;
        }
        .sub-title {
            color: #555;
            text-align: center;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .stButton button {
            background-color: #0e76a8 !important;
            color: white !important;
            font-size: 16px !important;
            border-radius: 5px !important;
            padding: 10px 15px;
        }
        .stTextInput > div > div > input {
            border-radius: 5px;
            border: 1px solid #0e76a8;
        }
        .result-box {
            background-color: #dff0d8;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            color: #3c763d;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">Disease Prediction System</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Use AI to predict health conditions based on your input.</p>', unsafe_allow_html=True)


# Check if file exists

diabetes_model = pickle.load(open("./models/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("./models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("./models/parkinsons_model.sav", 'rb'))
   


# Sidebar menu
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill', 
                           icons=['activity', 'heart', 'person'], 
                           default_index=0)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    
    # Input fields
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')

    # Prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic.'
        else:
            diab_diagnosis = 'The person is not diabetic.'
    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    # Input fields
    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        ChestPain = st.text_input('Chest Pain Type (0-3)')
    with col1:
        RestingBP = st.text_input('Resting Blood Pressure')
    with col2:
        Cholesterol = st.text_input('Cholesterol Level')
    with col3:
        FastingBS = st.text_input('Fasting Blood Sugar (1 = True, 0 = False)')
    with col1:
        RestingECG = st.text_input('Resting ECG (0-2)')
    with col2:
        MaxHR = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        ExerciseAngina = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')
    with col1:
        Oldpeak = st.text_input('Oldpeak (ST Depression)')
    with col2:
        ST_Slope = st.text_input('ST Slope (0-2)')
    with col3:
        Slope = st.text_input('Slope (e.g., 1 = upsloping, 2 = flat, 3 = downsloping)')
    with col1:
        Thal = st.text_input('Thal (e.g., 3 = normal, 6 = fixed defect, 7 = reversible defect)')

    # Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [Age, Sex, ChestPain, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, 
                      Oldpeak, ST_Slope, Slope, Thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease.'
        else:
            heart_diagnosis = 'The person does not have heart disease.'
    st.success(heart_diagnosis)

# Parkinson's Prediction
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Prediction using ML")
    col1, col2, col3 = st.columns(3)

    # Input fields
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        MDVP_RAP = st.text_input('MDVP:RAP')
        MDVP_PPQ = st.text_input('MDVP:PPQ')
        D2=st.text_input('D2')
    
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
        MDVP_APQ = st.text_input('MDVP:APQ')
        Shimmer_DDA = st.text_input('Shimmer:DDA')

    with col3:
        NHR = st.text_input('NHR')
        HNR = st.text_input('HNR')
        RPDE = st.text_input('RPDE')
        DFA = st.text_input('DFA')
        spread1 = st.text_input('Spread1')
        spread2 = st.text_input('Spread2')
        PPE = st.text_input('PPE')
    
    # Prediction
    park_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                      MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA,
                      NHR, HNR, RPDE, DFA, spread1, spread2, PPE,D2]
        user_input = [float(x) for x in user_input]
        park_prediction = parkinsons_model.predict([user_input])
        if park_prediction[0] == 1:
            park_diagnosis = "The person has Parkinson's disease."
        else:
            park_diagnosis = "The person does not have Parkinson's disease."
    st.success(park_diagnosis)