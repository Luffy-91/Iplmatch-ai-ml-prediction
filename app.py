import streamlit as st
import joblib

# ================= LOAD MODELS =================
pre_match_model = joblib.load("pre_match_model.pkl")
pre_match_encoders = joblib.load("pre_match_encoders.pkl")

runs_model = joblib.load("runs_model.pkl")
bat_encoders = joblib.load("bat_label_encoders.pkl")

wicket_model = joblib.load("wicket_model.pkl")

# ================= STREAMLIT CONFIG =================
st.set_page_config(page_title="IPL AI/ML System", layout="centered")
st.title("🏏 IPL AI/ML Prediction System")

# ================= DROPDOWN OPTIONS =================
# Pre-match dropdowns
venues = list(pre_match_encoders["venue"].classes_)
teams = list(pre_match_encoders["team1"].classes_)
toss_teams = list(pre_match_encoders["toss_winner"].classes_)

# Player runs dropdowns
bat_venues = list(bat_encoders["venue"].classes_)
bat_teams = list(bat_encoders["team"].classes_)
bat_opponents = list(bat_encoders["opposition_team"].classes_)

# ================= TABS =================
tab1, tab2, tab3 = st.tabs([
    "Pre-Match Winner",
    "Player Runs",
    "Player Wickets"
])

# =====================================================
# TAB 1: PRE-MATCH WINNER
# =====================================================
with tab1:
    st.header("Pre-Match Winner Prediction")

    venue = st.selectbox("Venue", venues)
    team1 = st.selectbox("Team 1", teams)
    team2 = st.selectbox("Team 2", teams)
    toss_winner = st.selectbox("Toss Winner", toss_teams)
    toss_decision = st.selectbox("Toss Decision", ["bat", "field"])

    if st.button("Predict Match Winner"):
        try:
            X = [[
                pre_match_encoders["venue"].transform([venue])[0],
                pre_match_encoders["team1"].transform([team1])[0],
                pre_match_encoders["team2"].transform([team2])[0],
                pre_match_encoders["toss_winner"].transform([toss_winner])[0],
                pre_match_encoders["toss_decision"].transform([toss_decision])[0]
            ]]

            pred = pre_match_model.predict(X)[0]
            winner = team1 if pred == 1 else team2
            st.success(f"🏆 Predicted Winner: {winner}")

        except Exception as e:
            st.error("❌ Prediction error. Please check inputs.")

# =====================================================
# TAB 2: PLAYER RUNS
# =====================================================
with tab2:
    st.header("Player Runs Prediction")

    season = st.number_input("Season", min_value=2008, step=1)
    venue = st.selectbox("Venue (Batting)", bat_venues)
    team = st.selectbox("Batting Team", bat_teams)
    opp = st.selectbox("Opposition Team", bat_opponents)
    balls = st.number_input("Balls Faced", min_value=0, step=1)
    sr = st.number_input("Strike Rate", min_value=0.0)

    if st.button("Predict Runs"):
        try:
            X = [[
                season,
                bat_encoders["venue"].transform([venue])[0],
                bat_encoders["team"].transform([team])[0],
                bat_encoders["opposition_team"].transform([opp])[0],
                balls,
                sr
            ]]

            runs = runs_model.predict(X)
            st.success(f"🏏 Predicted Runs: {int(runs[0])}")

        except Exception as e:
            st.error("❌ Prediction error. Please check inputs.")

# =====================================================
# TAB 3: PLAYER WICKETS
# =====================================================
with tab3:
    st.header("Player Wickets Prediction")

    overs = st.number_input("Overs Bowled", min_value=0.0)
    economy = st.number_input("Economy", min_value=0.0)

    if st.button("Predict Wickets"):
        try:
            pred = wicket_model.predict([[overs, economy]])
            st.success(f"🎯 Wicket Category: {pred[0]}")
        except Exception as e:
            st.error("❌ Prediction error. Please check inputs.")
