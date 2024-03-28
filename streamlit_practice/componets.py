import pandas as pd 
import streamlit as st  
import streamlit.components.v1 as stc

def main(): 
    st.title('Components static ')

    stc.html("<p  style = 'color:red;'> streamlit is awesome</p>")
    st.markdown('<p  style = 'color:red> streamlit is awesome</p>')





if __name__ == '__main__':
    main()  