import streamlit as st
import pandas as pd 

def main():
    st.title('streamlit forms and salary calculator')
    menu = ['Home','About']
    choice = st.sidebar.selectbox('Menu',menu)  

    if choice == 'Home': 
        st.subheader('Home')
        with st.form(key='salaryform'):  
            col1,col2,col3 = st.columns([3,2,1])  
            with col1:
                amount = st.text_input('input your hourly rate')

            with col2: 
                hour_per_week = st.text_input('input your hours worked',1,120)
            
            with col3:
                submit_salary= st.form_submit_button(label='Calculate')    
        
        if submit_salary:
            amount = int(amount)  # 將amount轉換為整數
            hour_per_week = int(hour_per_week)  # 將hour_per_week轉換為整數
            with st.expander('Results'):
                daily = [amount * 8] 
                weekly = [amount*hour_per_week]
                df = pd.DataFrame({'Daily':daily,'Weekly':weekly})
                st.dataframe(df.T)


        # method 1
        with st.form(key='form1',clear_on_submit=True):
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
        #salary = form2.number_input('Enter your salary',min_value=1000,max_value=100000)    
        submit_button2 = form2.form_submit_button(label='Login')

        if submit_button2:   
            st.write(username.upper())


    elif choice == 'About': 
        st.subheader('About')



if __name__ == '__main__':  
    main()  