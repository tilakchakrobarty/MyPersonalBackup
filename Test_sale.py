import streamlit as st 
import pandas as pd 
from pandasql import sqldf

st.title ("Sales report analysis") 
ds=pd.read_csv("Salesdata.csv")
country_count=ds.groupby("Country").size()
st.subheader("Country wise data count") 
query=""" 
select country, count(*) as customer_count from ds group by Country 
ORDER BY  Customer_count DESC """ 

result_df=sqldf(query,globals())
st.dataframe(result_df)
st.bar_chart(result_df.set_index("Country")["customer_count"])
