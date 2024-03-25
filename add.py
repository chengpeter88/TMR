import streamlit as st
import pandas as pd
import streamlit.components as stc  
import base64   
import time 
timestr =  time.strftime("%Y%m%d-%H%M%S")

def text_downloader(raw_text):  
    b64 = base64.b64encode(raw_text.encode()).decode()  
    new_filename = f"new_text_file_{timestr}.txt"   
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">click here</a>'
    st.markdown(href,unsafe_allow_html=True)      

def csv_downloader(data):  
    csvfile= data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()  
    new_filename = "new_text_file_{}_.csv".format(timestr)   
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">click here</a>'
    st.markdown(href,unsafe_allow_html=True) 

class FileDownloader(object):   
    """
    this class is used to download file
    """

    def __init__(self, data, file_label='myfile', file_extension='txt'):
        super(FileDownloader, self).__init__()  
        self.data = data
        self.file_label = file_label
        self.file_extension = file_extension

    def downloader(self):  
        b64 = base64.b64encode(self.data.encode()).decode()  
        new_filename = "{}_{}_{}".format(self.file_label,timestr,self.file_extension)   
        st.markdown("#### Download File ###")
        href = f'<a href="data:file/{self.file_extension};base64,{b64}" download="{new_filename}">click here</a>'
        st.markdown(href,unsafe_allow_html=True)      



def main():
    menu = ["Home","CSV","About"]# 坐下拉菜单   
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":    
        st.subheader("Home")    
        my_text = st.text_area("type message")  
        if st.button("Submit"):
            st.write(my_text)   
            # text_downloader(my_text)
            Dowanload  =  FileDownloader(my_text).downloader()

    elif choice == "CSV":   
        df = pd.read_csv("iris.csv")   
        st.dataframe(df)
        #csv_downloader(df)  
        Dowanload  =  FileDownloader(df.to_csv(),file_extension='csv').downloader()

    else:   
        st.subheader("About")    
        st.write("This is about page")

    





if __name__ == '__main__':
    main()  # Run the main function