
# 🏃Workout Tracker

This web app helps you to keep all our workout vidoes organised. You can add or delete vidoes at your wish. The vidoes that you add will be stored to the [MongoDB](https://www.mongodb.com/). This app will also recommed the workout video everyday. 


## 🪛Installation

Create and activate the Conda Environment
```
conda create -p /env python==3.8 -y
```
```
conda activate ./env
```
```
pip install -r requirements.txt
```
```
streamlit run app.py
```
## 👨‍💻Tech Stack

**Client:** Streamlit, Python

**Server:** MongoDb


## 🕵️‍♂️Environment Variables

To run this project, you will need to add the following environment variables to your config.py file

`MONGO_DB_URL` = "YOUR  HARPERDB USERNAME"


NOTE - Store your API key and SECRET key in your environment variable for eshtablishing secure connections.



## 🔗Important References

 - [Streamlit](https://streamlit.io/)
 - [MongoDB](https://www.mongodb.com/)


## 🎯App Screenshots

![image](https://user-images.githubusercontent.com/55878408/188103624-255b7bf9-c64a-454b-b5db-192e5fd70240.png)

![image](https://user-images.githubusercontent.com/55878408/188103798-1ffcd3dd-b4dc-461c-a73e-6588a3abedb2.png)

![image](https://user-images.githubusercontent.com/55878408/188103906-c9b3dee5-1077-41f6-aebd-32b174d76014.png)
