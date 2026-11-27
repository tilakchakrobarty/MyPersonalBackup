import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import streamlit as st 

df = pd.read_excel('CarPrice.xlsx')

st.title('Car Price Prediction') 

user_brand=st.sidebar.selectbox('Select Brand:',df['Car_Model'].unique())

user_year=st.sidebar.selectbox('Select Year:',df['Year'].unique())
user_km=st.sidebar.number_input('Enter KM ran:',5000,90000)
user_fuel=st.sidebar.selectbox('Select fuel type:',df['Fuel_Type'].unique())
user_trans=st.sidebar.selectbox('Select transmission:',df['Transmission'].unique())


brand_encoder = LabelEncoder()
df['Brand_Encoded'] = brand_encoder.fit_transform(df['Car_Model'])
fuel_encoder = LabelEncoder()
df['Fuel_Encoded'] = fuel_encoder.fit_transform(df['Fuel_Type'])
trans_encoder = LabelEncoder()
df['Trans_Encoded'] = trans_encoder.fit_transform(df['Transmission'])


x = df[['Brand_Encoded', 'Year', 'Km_Driven', 'Fuel_Encoded', 'Trans_Encoded']]
y = df['Price_INR']


model = LinearRegression()
model.fit(x, y)


brand_num = brand_encoder.transform([user_brand])[0]
fuel_num = fuel_encoder.transform([user_fuel])[0]
trans_num = trans_encoder.transform([user_trans])[0]


result = model.predict([[brand_num, user_year, user_km, fuel_num, trans_num]])
st.subheader(f'Predicted Car Price: ₹{result[0]:,.2f}')
