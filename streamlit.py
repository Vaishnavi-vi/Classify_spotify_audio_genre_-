import streamlit as st
import numpy as np
import pickle
from PIL import Image

model = pickle.load(open("xgboost_genre_classifier.pkl", "rb"))
scaler = pickle.load(open("scalar.pkl", "rb")) 

cluster_map = {
    0: "Accosutic",
    1: "Chill",
    2: "Country",
    3: "Feeling",
    4: "Hip-hop"
}


page=st.sidebar.radio("Go to",["Home","Audio Genre Prediction"])
if page=="Home":
    st.header("🎧Classify Audio Genre-Spotify")
    image=Image.open("C:\\Users\\Dell\\Downloads\\image.png",)
    st.image(image,use_container_width=True)
elif page=="Audio Genre Prediction":
    st.header("🎧Real Time Audio Genre Prediction")
    st.subheader("Tune the values below to predict audio genres")
    
    #input features
    popularity=st.slider("Popularity",0,50,100)
    duration_ms=st.slider("duration_ms",0.0,1.0,2.0)
    danceability=st.slider("danceability",0.0,0.5,1.0)
    energy=st.slider("energy",0.0,0.5,1.0)
    loudness=st.slider("loudness",-20,0,20)
    mode=st.slider("mode",0,1)
    speechiness=st.slider("speechiness",0.00,0.15)
    acousticness=st.slider("acousticness",0.00,0.99)
    instrumentalness=st.slider("instrumentalness",0.00,0.12)
    liveness=st.slider("liveness",0.00,0.53)
    valence=st.slider("valence",0.0,0.5,1.0)
    tempo=st.slider("tempo",0,125,250)
    
    
        # Step 1: Convert to array
    user_input = np.array([[popularity,duration_ms,danceability,energy,loudness,mode,speechiness,acousticness,instrumentalness,liveness,
                                valence,tempo]])

        #  Step 2: Scale the input (same as model training)
    user_input_scaled = scaler.transform(user_input)
        
    if st.button("Predict Genre"):
        prediction=model.predict(user_input_scaled)
        predicted_cluster=int(prediction[0])
        genre_name=cluster_map.get(predicted_cluster,"Unknown Genre")
        
        st.markdown(f"""
    <div style="background-color:#1DB954;padding:15px;border-radius:10px">
        <h3 style="color:white;">🎧 Predicted Genre: {genre_name}</h3>
        <p style="color:white;">(Cluster {predicted_cluster})</p>
    </div>
    """, unsafe_allow_html=True)
        

    
    
