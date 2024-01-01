# My Doctor - Multiple Disease Prediction System
![_d05f62fa-0b0c-4fb6-8d91-9aa8dfdc4f2b](https://github.com/AkshayRamakrishnann/ML_For_Dummies/assets/111365771/1a680f3f-0548-4925-85ad-77684189a965)


Welcome to My Doctor, a comprehensive web application designed to predict multiple diseases, including diabetes, heart disease, and Parkinson's disease. My Doctor employs machine learning models to provide accurate predictions based on user-provided health metrics. This user-friendly system is equipped with dedicated sections for each disease, allowing users to input relevant details and receive instant predictions.


## Features

### Diabetes Prediction

Predict the likelihood of diabetes by entering key health metrics, including the number of pregnancies, glucose levels, blood pressure, skin thickness, insulin levels, BMI, diabetes pedigree function, and age.

### Heart Disease Prediction

Determine the probability of heart disease by inputting various health parameters such as age, sex, chest pain types, resting blood pressure, serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise-induced angina, ST depression induced by exercise, slope of the peak exercise ST segment, major vessels colored by fluoroscopy, and thalassemia type.

### Parkinson's Disease Prediction

Predict the presence of Parkinson's disease by providing voice-related features, including MDVP:Fo (Hz), MDVP:Fhi (Hz), MDVP:Flo (Hz), MDVP:Jitter (%), MDVP:Jitter (Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP, MDVP:Shimmer, MDVP:Shimmer (dB), Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, and PPE.

### Multiple Sclerosis Prediction

Predict the likelihood of Multiple Sclerosis by providing key features including age, gender, breastfeeding, varicella, initial symptom, mono or polysymptomatic status, oligoclonal bands, LLSSEP, ULSSEP, VEP, BAEP, periventricular MRI, cortical MRI, infratentorial MRI, and spinal cord MRI.


## Getting Started

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Run the Application:**
   ```bash
   streamlit run your_app_file.py

3. **Access the Application:**
   Open your web browser and visit the provided address.

### Usage
Click on the "Introduction" button to understand the application's purpose.
Navigate to specific prediction pages for diabetes, heart disease, and Parkinson's.
Input relevant health details and click on the prediction button to receive results.

### Project Structure
your_app_file.py: Main Python script containing Streamlit application code.
models/: Directory for saved machine learning models (e.g., diabetes_model.sav, heart_disease_model.sav, parkinsons_model.sav).
requirements.txt: List of required Python packages.

### Output Screenshots

![ml2](https://github.com/AkshayRamakrishnann/ML_For_Dummies/assets/111365771/41062430-e2f0-4460-be57-c4b347b4d07d)

![mld](https://github.com/AkshayRamakrishnann/ML_For_Dummies/assets/111365771/1f65666f-9f9e-404c-a3ae-9a721674e819)


### Contributing
Contributions, bug reports, and suggestions are welcome! Open an issue or create a pull request to contribute to the project.

### License
This project is licensed under the MIT License - see the LICENSE file for details.


