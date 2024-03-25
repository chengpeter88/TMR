import streamlit as st
import pandas as pd 

def main():
    st.title('streamlit forms and salary calculator')
    menu = ['Home','About']
    choice = st.sidebar.selectbox('Menu',menu)  

    if choice == 'Home': 
        st.subheader('Home')
        # method 1
        with st.form(key='form1'):
            firstname = st.text_input('Enter your name')
            lastname = st.text_input('Enter your last name')    
            dob = st.date_input('Enter your date of birth')
            age = st.number_input('Enter your age')
            submit_button = st.form_submit_button(label='SignUp')
            
        if submit_button:
            st.success('hello {} you have created your account'.format(firstname))
    # method 2  
        form2 = st.form(key='form2')
        username = form2.text_input('Enter your username')  
        jobtype  = form2.selectbox('Select job type',['Data Scientist','Data Analyst','Data Engineer']) 
        salary = form2.number_input('Enter your salary',min_value=1000,max_value=100000)    
        submit_button2 = form2.form_submit_button(label='Login')

        if submit_button2:   
            st.write(username.upper())


    elif choice == 'About': 
        st.subheader('About')



if __name__ == '__main__':  
    main()  