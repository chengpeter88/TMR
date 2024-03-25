import streamlit as st  
import pandas as pd
tabel=pd.read_csv("Data.csv") 
st.title('Streamlit Tutorial')  
st.subheader('Hello World') 
st.header('This is a header')   
st.text('Hello Streamlit')
st.markdown('### This is a Markdown')
st.markdown('[google](https://www.google.com)') 
st.markdown('---')
st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)''')
st.latex(r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}")
json_data = {'name': 'John', 'age': 22, 'city': 'New York'} 
st.json(json_data) 
code= """
def hello():    
    print('Hello, Streamlit')

"""
st.code(code, language='python')    

st.write('## head2')
st.metric(label='wind speed', value="120ms⁻¹", delta="1.4ms⁻¹", delta_color="normal")
st.write('## hello 中文不知道有沒有')
st.latex(r"\sum_{m=1}^{n}\frac{1}{m}=\frac{1}{2} \times \frac{1}{3} \times \frac{1}{4} \times \cdots \times \frac{1}{n}")
st.table(tabel)
st.dataframe(tabel)
def change():
    print(st.session_state.checker)
st.checkbox('I agree',value=True,key='checker',on_change=change)  
if st.checkbox('Show/Hide'):
    st.write('I am showing')
st.radio('What is your favorite color?', ('Red', 'Green', 'Blue'))
def button():
    print('Button clicked')
btn= st.button('Click me',on_click=button)  
select=st.selectbox('Select', ['a', 'b', 'c']) 
print(select)  
mult=st.multiselect('Multiselect', ['a', 'b', 'c'])  
st.write(mult)
