import streamlit as st
from PIL import Image   
import pandas as pd
import docx2txt 
from PyPDF2 import PdfFileReader    
import pdfplumber
# import textract

print("pd.__version__",pd.__version__)
print("st.__version__",st.__version__)
def load_image(image_file): 
    img = Image.open(image_file)    
    return img  

def read_pdf(file): 
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()
    return all_page_text


def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()

	return all_page_text
def main(): 
    st.title("File Upload Tutorial")    
    menu = ["Home","Dataset","DocumentFiles","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == 'Home':
        st.subheader("Home")
        image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg']) 
        if image_file is not None:
            st.write(type(image_file))
            #st.write(dir(image_file))    
            #st.image(image_file, width=300)
            #st.write(image_file)
            file_details = {"FileName":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
            st.write(file_details)
            st.image(load_image(image_file), width=300)

    
    elif choice == 'Dataset':
        st.subheader("Dataset") 
        data_file = st.file_uploader("Upload CSV",type=['csv'])
        if data_file is not None:
            st.write(type(data_file))
            st.write(data_file)
            file_details = {"FileName":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
            st.write(file_details)
            df = pd.read_csv(data_file)
            st.dataframe(df)
    elif choice == 'DocumentFiles': 
        st.subheader("DocumentFiles")
        docx_file = st.file_uploader("Upload Document",type=['txt','docx','pdf'])
        if st.button("Process"):

            if docx_file is not None:
                file_details = {"FileName":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
                st.write(file_details)

                if docx_file.type == "text/plain":
                    # Read as string
                    raw_text = str(docx_file.read(),"utf-8" )
                    st.write(raw_text)
                elif docx_file.type == "application/pdf":
                    # try :
                    #     with pdfplumber.open(docx_file) as pdf:
                    #         pages = pdf.pages[0]
                    #         st.write(pages.extract_text())
                    # except :
                    #     st.write("PDF file is not supported")
                    raw_text = read_pdf(docx_file)  
                    st.write(raw_text)  
                    
                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)  

    else:
        st.subheader("About")

if __name__ == '__main__':  
    main()