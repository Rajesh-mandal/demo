import base64
import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 


#load the model from pickle file  
def load_model(picklefile,CRSDepTime, DepTime, CRSArrTime, ArrTime, CarrierDelay, WeatherDelay, NASDelay, SecurityDelay, LateAircraftDelay):
    with open(picklefile, 'rb') as f: 
        model = pickle.load(f)
    
    res = model.predict([[CRSDepTime, DepTime, CRSArrTime, ArrTime, CarrierDelay, WeatherDelay, NASDelay, SecurityDelay, LateAircraftDelay]])
    return res

def welcome():
    return "Welcome on Board!!!!"

def main():
    st.title('Flight Delay Prediction')  
    with open("Aeroplane1.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    
    CRSDepTime = st.text_input('CRSDepTime',placeholder='Computer Reservation Scheduled Departure Time in hhmm')
    DepTime = st.text_input('DepTime',placeholder='Departure Time in hhmm')
    CRSArrTime = st.text_input('CRSArrTime',placeholder='Computer Reservation Scheduled Arrival Time in hhmm')
    ArrTime = st.text_input('ArrTime',placeholder='Arrival Time in hhmm')
    CarrierDelay = st.text_input('CarrierDelay',placeholder='Carrier Delay in min')
    WeatherDelay = st.text_input('WeatherDelay',placeholder='Weather Delay in min')
    NASDelay = st.text_input('NASDelay',placeholder='NAS Delay in min')
    SecurityDelay = st.text_input('SecurityDelay',placeholder='Security Delay in min')
    LateAircraftDelay = st.text_input('LateAircraftDelay',placeholder='LateAircraft Delay in min')
    
    result = ""
    if st.button('Predict'):
        result = load_model('flight.pkl',CRSDepTime, DepTime, CRSArrTime, ArrTime, CarrierDelay, WeatherDelay, NASDelay, SecurityDelay, LateAircraftDelay)
        # st.text('The output is {}'.format(int(result[0])))
        if result == 0:
            st.text("THERE IS NO DELAY IN FLIGHT. FLIGHT WILL ARRIVE ON TIME !!!!!!!!")
        else:
            st.text("THERE IS DELAY IN FLIGHT. FLIGHT WILL NOT ARRIVE ON TIME !!!!!!!!")
               
        
if __name__ == '__main__':
    main() 
