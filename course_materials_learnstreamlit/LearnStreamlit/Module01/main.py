#core package 

import streamlit as st
# load EDA package  
import pandas as pd
def main():
    df = pd.read_csv('iris.csv')
    st.title('Streamlit Tutorial')  

    st.subheader('Hello World')
    st.text('台灣每過一分鍾，非州就過60s')
    name = 'peter'
    st.text('this is {}'.format(name))

    st.markdown('### This is a Markdown')  
    ##background color boostraps aler
    st.success('Successful')    
    st.warning('This is a warning') 
    st.info('This is a info')
    st.error('This is an error')
    st.exception('NameError(\'name not defined\')') 
    #superfunction  
    st.write('normal test')
    st.write(1+2) 
    st.write(dir(st))
    st.write('## table')
    # st.dataframe(df,500,500)
    # dataframe
    # st.dataframe(df.style.highlight_max(axis=0)) 
    #NOTE - highlight_max(axis=0) is used to highlight the maximum value in each column.
    # st.table(df) 

    #method  using superfunction st.write
    st.write(df.head)
    st.json({'foo':'bar','fu':'ba'})

    #code block
    mycode = '''
    def hello():
        print("hello, streamlit")   
        
        '''
    st.code(mycode,language='python')

    #widget 
    st.button('simple button')
    if st.button('button'):
        st.write('button clicked')
    name = st.text_input('Enter Name','Type Here...')   
    if st.button('Submit'):
        result = name.title()
        st.success(result)
    name = st.text_area('Enter Name','Type Here...')
    if st.button('sumbit'):
        st.write('name:{}'.format(name.upper))

    ### working with button
    yourname ='Jesse'
    if st.button('Submit',key='submit'):
        st.write('Your name is {}'.format(yourname.upper()))
    st.write('---') 
    if st.button('submit',key='submit_button'):
        st.write('Your name is {}'.format(yourname.lower()))
    
    #checkbox   
    status = st.radio('what is your status',('Active','Inactive'))  

    if status == 'Active':
        st.success('You are Active')
    elif status == 'Inactive':
        st.warning('You are Inactive')  

    #checkbox
    if st.checkbox('Show/Hide'):
        st.text('Showing or Hiding Widget')

    if st.expander('python code'):
        st.success('```python\nimport streamlit as st\n```')


    my_lang = ['Python','Java','C++']
    choice = st.selectbox('Choose Language',my_lang)    
    

    spoken_lang = ['English','Chinese','Japanese']  
    spoken = st.multiselect('Choose Language Spoken',spoken_lang,default='English')

    #slider
    age = st.slider('What is your age',1,100,5)
    color  = st.select_slider('Choose Color',options=['red','green','orange','pink','blue'],value=('red','green'))

    #file upload    
    from PIL import Image   
    img =Image.open('test.png')
    st.image(img,use_column_width=True,caption='Simple Image')
    st.image('https://www.istockphoto.com/photo/beautiful-meadow-field-with-fresh-grass-and-yellow-dandelion-flowers-in-nature-gm1301592082-393590542')
    video_file = open('data/secret_of_success.mp4','rb').read() 
    st.video(video_file,start_time=2)
    audio_file = open('data/song.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

    #text input
    fname = st.text_input('enter firstname',max_chars=10)
    st.title(fname)
    #text area 
    message = st.text_area('enter message',height=100)
    st.write(message)
    # date input
    date = st.date_input('Select Date')
    st.write('Selected Date:', date)

    # time input
    time = st.time_input('Select Time')
    st.write('Selected Time:', time)

    # file uploader
    uploaded_file = st.file_uploader('Upload a file')
    if uploaded_file is not None:
        st.write('File uploaded successfully!')

    # color picker
    color = st.color_picker('Pick a color', '#FF0000')
    st.write('Selected Color:', color)
    number = st.number_input('enter number',1,25)
    
    mytime = st.time_input('my time')
    
    password = st.text_input('enter your password',type='password')

if __name__ == '__main__':
    main()  # Run the main function