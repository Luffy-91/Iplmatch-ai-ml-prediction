🏏 IPL AI/ML Prediction System

📌 Project Overview

This project is an AI/ML-based IPL Prediction System developed as part of an academic project.
The system uses Machine Learning models to predict:

1. Pre-Match Winner Prediction


2. Player Runs Prediction


3. Player Wickets Prediction



The application is deployed using Streamlit Cloud and provides an interactive web interface for real-time predictions.


---

🎯 Objectives

To analyze IPL data using Machine Learning

To predict match outcomes before the match starts

To predict individual player performance

To deploy a complete AI/ML system using Streamlit



---

🔮 Predictions Implemented

1️⃣ Pre-Match Winner Prediction

Inputs:

Venue

Team 1

Team 2

Toss Winner

Toss Decision


Model Used:
Random Forest Classifier (Binary Classification)

Output:

Predicted Match Winner (Team 1 or Team 2)



---

2️⃣ Player Runs Prediction

Inputs:

Season

Venue

Batting Team

Opposition Team

Balls Faced

Strike Rate


Model Used:
Random Forest Regressor

Output:

Predicted number of runs scored by the player



---

3️⃣ Player Wickets Prediction

Inputs:

Overs Bowled

Economy


Model Used:
Random Forest Classifier

Output:

Wicket Category (High / Low)



---

🗂️ Datasets Used

ipl_match_winner_dataset_dirty.csv

alt_player_runs_wickets_dataset.csv


These datasets were cleaned and preprocessed before training the models.


---

🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Joblib

Streamlit

Streamlit Cloud



---

🌐 Live Application

🔗 Deployed Streamlit App:
https://iplmatch-ai-ml-prediction-z8wfgdd666bkob9annwhhu.streamlit.app/


---

📁 Project Structure

IPL_AI_ML_Project/
│
├── app.py
├── pre_match_model.pkl
├── pre_match_encoders.pkl
├── runs_model.pkl
├── bat_label_encoders.pkl
├── wicket_model.pkl
├── requirements.txt
└── README.md


---

▶️ How to Run the Project Locally

1️⃣ Install Dependencies

pip install streamlit pandas numpy scikit-learn joblib

2️⃣ Run Streamlit App

streamlit run app.py

3️⃣ Open in Browser

http://localhost:8501


---

📊 Machine Learning Workflow

1. Data Collection


2. Data Cleaning & Preprocessing


3. Feature Engineering


4. Model Training


5. Model Evaluation


6. Model Deployment using Streamlit




---

🎓 Academic Relevance

Suitable for BCA / MCA / Data Analytics / AI-ML projects

Demonstrates real-world application of Machine Learning

Includes end-to-end deployment

---

📌 Future Enhancements

Live match prediction

Player form analysis

Team strength comparison

Advanced visual analytics



---

🙌 Acknowledgements

This project was developed for academic purposes to understand and apply concepts of Data Analytics and Machine Learning.


---

📧 Author

Name: sky
Course: BCA
