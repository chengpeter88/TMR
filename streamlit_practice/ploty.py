import pandas as pd
import numpy as np
import plotly.express as px 
import streamlit as st  

def main(): 
    st.title('plotting')    
    df = pd.read_csv('prog_languages_data.csv')
    st.dataframe(df.head())
    st.subheader('plotting part1')  
    fig = px.pie(df ,values='Sum',names='Languages',title='Pie chart')
    st.plotly_chart(fig)

    st.subheader('plotting part2')  
    fig2 = px.bar(df ,x='Languages',y='Sum',title='Bar chart')
    st.plotly_chart(fig2)





if __name__ == '__main__':
    main()  
