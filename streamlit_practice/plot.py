import streamlit as st
import pandas as pd
import numpy as np  

import matplotlib.pyplot as plt
import matplotlib
import altair as alt
plt.style.use('ggplot')



def main():
    st.title('plotting')

    df = pd.read_csv('iris.csv')
    st.dataframe(df.head())
    #df['species'].value_counts().plot(kind='bar')  
    fig ,ax =  plt.subplots()  
    ax.scatter(*np.random.random(size=(2,100)))
    st.pyplot(fig)
    #method 2 simple method 
    fig = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    fig ,ax = plt.subplots()
    df['species'].value_counts().plot(kind='bar')   
    st.pyplot(fig)
    # alternative method    
    #fig = plt.figure()
    #sns.countplot(df['species'])
    #st.pyplot(fig)

    st.subheader('plotting part2')
    # df['sepal_length'] = df['sepal_length'].astype(float)
    # df['petal_length'] = df['petal_length'].astype(float)
    # st.bar_chart(df['sepal_length', 'petal_length' ])
    st.subheader('plotting part3')  
    df2=pd.read_csv('lang_data.csv')
    st.dataframe(df2.head())
    lang_list=df2.columns.tolist()
    lang_chocies = st.multiselect('choose languages',lang_list,default='Python')    
    new_df = df2[lang_chocies]  
    st.line_chart(new_df)
    # area chart

    st.area_chart(new_df,use_container_width=True)
    st.subheader('plotting part4--altair')
    # altair

    df3 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])

    c = alt.Chart(df3).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    )

    st.dataframe(df3.head())

    st.altair_chart(c, use_container_width=True)


if __name__ == '__main__':  
    main()



