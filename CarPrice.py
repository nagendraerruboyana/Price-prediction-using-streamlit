import pandas as pd
import numpy as np
import datetime
import pickle
import streamlit as st

cars_df = pd.read_csv('./cars24.csv')

st.write(
        '''
         # Cars24 Used Car price Prediction
        ''')

st.dataframe( cars_df, use_container_width=True, height=250)

col1, col2 = st.columns(2)

with col1:
    fuel_type = col1.selectbox("Select the fuel type",(cars_df['fuel_type'].unique()),)
    engine = col1.slider("Set the Engine power", min_value=int(cars_df['engine'].min()), max_value=int(cars_df['engine'].max()), step=100)

with col2:
    transmission_type = col2.selectbox("Select the Transmission type",(cars_df['transmission_type'].unique()),)
    seats = col2.selectbox("Select the Transmission type",(cars_df['seats'].unique()),)

encode_dict = {
    'fuel_type':{'Diesel':1,'Petrol':2,'CNG':3,'LPG':4,'Electric':5},
    'transmission_type':{'Manual':1,'Automatic':2}
}

def model_pred(fuel_type, transmission_type, engine, seats):

    with open('car_pred', 'rb') as file:
        reg_model = pickle.load(file)
        input_features = [[2019.0, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]

        return reg_model.predict(input_features)


if (st.button('Predict')):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fuel_type,transmission_type,engine,seats)

    st.text(f'The price of the car is {price[0].round(2)} lakhs rupees')