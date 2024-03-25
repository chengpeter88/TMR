import streamlit as st
from PIL import Image
import pandas
import plotly.express as px 
import pandas as pd
img = Image.open('data/image_01.jpg')
#st.set_page_config(page_title='hello everyone',
#                   page_icon=':smiley:'
#                   ,initial_sidebar_state='expanded')
#st.set_page_config(page_title='hello everyone',
#                   page_icon=img)

page_confi = {'page_title':'hello everyone','page_icon':':smiley:','layout':'wide'}
st.set_page_config(**page_confi)


def main():
    st.title('hello😆')
    st.sidebar.success('Menu')
    st.title('plotting graphs')
    df = pd.read_csv('data/prog_languages_data.csv')
    st.dataframe(df)
    fig = px.pie(df, values='Sum', names='lang', title='Pie chart')
    st.plotly_chart(fig)    
    fig2 = px.bar(df, x='lang', y='Sum', title='Bar chart') 
    st.plotly_chart(fig2)   

if __name__ == '__main__':
    main()