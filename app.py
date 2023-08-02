import random
import streamlit as st
from src.get_youtube_details import YouTubeInfoExtractor
from src.workout_data import WorkoutData
from src.constants import *




yt_extractor = YouTubeInfoExtractor()
db = WorkoutData()

@st.cache_data()
def get_workouts():
    return db.get_all_workouts()

def get_duration_text(duration_s):
    seconds = duration_s % 60
    minutes = int((duration_s/60)%60)
    hours = int(duration_s/ (60*60)%24)
    text = ''
    if hours > 0:
        text += f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        text += f'{minutes:02d}:{seconds:02d}'
    return text

st.title('WORKOUT TRACKER')

menu_options = ("Today's Workout", "All Workouts", "Add Workout")
selection = st.sidebar.selectbox("Menu", menu_options)

if selection == "All Workouts":
    st.markdown(f"## All Workouts")

    workouts = get_workouts()
    if workouts:
        for wo in workouts:
            url = "https://youtu.be/" + wo["id"]
            st.text(wo['title'])
            st.text(f"{wo['channel']} - {get_duration_text(wo['duration'])}")

            ok = st.button('Delete Workout', key=wo['id'])
            if ok:
                db.delete_workout(wo['id'])
                st.cache_data.clear()
                st.experimental_rerun()

            st.video(url)
       
    else:
        st.text("No Data Found! Add some videos.")

elif selection=='Add Workout':
    st.markdown(f"## Add workout")

    url = st.text_input("Please enter the video url")
    if url:
        workout_data = yt_extractor.get_info(url)
        if workout_data is None:
            st.text("No workout videos!!")
        else:
            st.text(workout_data['title'])
            st.text(workout_data['channel'])
            st.video(url)
            if st.button("Add workout"):
                db.insert_workout(
                    records=workout_data)
                st.text("Added workout!")
                st.cache_data.clear()

else:
    st.markdown(f"## Workout Today")

    workouts = get_workouts()
    if not workouts:
        st.text("No workout videos!!")
    else:
        wo = db.get_workout_today()

        if not wo:
            # not yet defined
            workouts = get_workouts()
            n = len(workouts)
            idx = random.randint(0, n-1)
            wo = workouts[idx]
            db.insert_workout_today(wo)
        else:
            # first item in list
            wo = wo[0]

        if st.button("Choose Another Workout"):
            workouts = get_workouts()
            n = len(workouts)
            if n > 1:
                idx = random.randint(0, n-1)
                wo_new = workouts[idx]
                while wo_new['id'] == wo['id']:
                    idx = random.randint(0, n-1)
                    wo_new = workouts[idx]
                wo = wo_new
                db.update_workout_today(wo, insert=True)

            
        url = "https://youtu.be/" + wo["id"]
        st.text(wo['title'])
        st.text(f"{wo['channel']} - {get_duration_text(wo['duration'])}")
        st.video(url)

