import streamlit as st  
from PIL import Image   
import os
@st.cache   # This function will be cached  
def load_image(image_file):
    img = Image.open(image_file)
    return img  # returns PIL image

def sav_upload_file(uplodadfile):
    with open(os.path.join("tempDir",uplodadfile.name),"wb") as f:
        f.write(uplodadfile.getbuffer())
    return st.success("Saved File:{} to tempDir".format(uplodadfile.name))  

def main(): 
    st.title("Mutiple File Uploadd Tutorial")

    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice  =="Home":
        st.subheader("Upload Multiple Images")
        uploadfile = st.file_uploader("Upload multiple images",type=["png","jpg","jpeg"],accept_multiple_files=True)
        if uploadfile is not None:
            #st.write(type(uploadfile))
            st.write(uploadfile) #list 
            for images in uploadfile:
                st.write(images.name)
                st.image(load_image(images),width=250)  
                # save_uploaded_file(images)    
                sav_upload_file(images) 
                # file_details = {"FileName":images.name,"FileType":images.type}
                # st.write(file_details)
                # img = load_image(images)
                # st.image(img,width=250)
                # sav_upload_file(images)
 
    else:
        st.subheader("About")


if __name__ == '__main__':  
    main()