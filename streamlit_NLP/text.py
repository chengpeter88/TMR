
##module 4 
# python 3.8.19
# 這些東西都是要安裝的 cmd terminal pip
## pip install neattext 
## pip install textblob
## pip install spacy
#python -m spacy download en_core_web_sm

###text test 的文字
'''
#NeatText:a simple NLP package for cleaning textual data and text preprocessing. 
#Simplifying Text Cleaning For NLP & ML
'''
#ANCHOR -  import 套件
import streamlit as st
import pandas as pd 
import spacy
from spacy import displacy  
nlps = spacy.load('en_core_web_sm') 

import neattext as nt
import neattext.functions as nfx
from textblob import TextBlob
from collections import Counter 
import matplotlib.pyplot as plt 
import seaborn as sns   
plt.style.use('fivethirtyeight')
sns.set_style("whitegrid")

from wordcloud import WordCloud 
import base64   
import time
timestr=time.strftime("%Y%m%d-%H%M%S")

### [file upload 需要的套件]
import docx2txt 
import pdfplumber
import PyPDF2
from PyPDF2 import PdfReader

############
#ANCHOR - function 
# def text_analyzer(my_text): 
#     docx = nlps(my_text)
#     allData = [('"Token":{},\n"Lemma":{}'.format(token.text, token.lemma_)) for token in docx]
#     return allData


def text_analyzer(my_text):
	docx = nlps(my_text)
	allData = [(token.text,token.shape_,token.pos_,token.tag_,token.lemma_,token.is_alpha,token.is_stop) for token in docx]
	df = pd.DataFrame(allData,columns=['Token','Shape','PoS','Tag','Lemma','IsAlpha','Is_Stopword'])
	return df 

def get_entities(my_text):
    docx = nlps(my_text)
    entities = [(entity.text,entity.label_) for entity in docx.ents]
    return entities	

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
# @st.cache
def render_entities(rawtext):
	docx = nlps(rawtext)
	html = displacy.render(docx,style="ent")
	html = html.replace("\n\n","\n")
	result = HTML_WRAPPER.format(html)
	return result

#most common tokens 
def get_most_common_tokens(my_text,num=5):
    word_tokens = Counter(my_text.split())
    most_common_tokens = dict(word_tokens.most_common(num))
    return most_common_tokens   


def get_sentiment(my_text): 
    blob = TextBlob(my_text)
    sentiment = blob.sentiment
    return sentiment

def plot_wordcloud(my_text):
    wc = WordCloud(width=800,height=400,random_state=21,max_font_size=110).generate(my_text)
    plt.figure(figsize=(10,8))
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

def make_downloadable(data):
    cvsfile = data.to_csv(index=False)
    b64 = base64.b64encode(cvsfile.encode()).decode()
    new_filename = "nlp_result_{}.csv".format(timestr)
    st.markdown("###  📩 ⬇️ Download CSV file r")
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click here!</a>'
    st.markdown(href,unsafe_allow_html=True)

def read_pdf(file):
    #模組有更新
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    all_page_text = ""
    for i in range(count):
        page = pdfReader.pages[i]
        all_page_text += page.extract_text()
    return all_page_text

def read_pdf2(file):
    with pdfplumber.open(file) as pdf:
        pages = pdf.pages[0]
        text = pages.extract_text()
###########
#@st.cache(suppress_st_warning=True)  
def main():
    st.title(" Summarization NLP App")  
    meun = ["Home",'NLP(file)', "About"]
    choice=st.sidebar.selectbox("Menu", meun)
    if choice == 'Home':
        st.subheader("Home:analyze text")
        text = st.text_area("Enter Text")   
        st.write(text)  
        num_of_most_common_words = st.sidebar.number_input("Number common tokne", 5,15)
        if st.button('analyze'):
            with st.expander('Original Text'):  
                st.write(text)  


            with st.expander('Text Analysis'):  
                token_result = text_analyzer(text)   
                st.dataframe(token_result)
                

            with st.expander('entity recognition'):   
                # entity_result=get_entities(text)
                # st.write(entity_result) 
                entity_result=render_entities(text)
                st.write(entity_result,unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                with st.expander('word stats'):
                    st.info('word stats here...')
                    docx= nt.TextFrame(text)
                    st.write(docx.word_stats())


                with st.expander('top keywords'):
                    st.info('top keywords here...')
                    pro_text=nfx.remove_stopwords(text) #good for removing stop words (etc:and,the,or,)
                    most_common_tokens = get_most_common_tokens(pro_text,num_of_most_common_words)
                    st.write(most_common_tokens)

                with st.expander('sentiment analysis'):
                    st.write("Here are some word stats...")
                    sentiment_result = get_sentiment(text)
                    st.write(sentiment_result)

            with col2:
                with st.expander('plot word frequency'):
                    st.write("Here are some word stats...")
                    fig = plt.figure(figsize=(10,8))
                    top_keywords = get_most_common_tokens(pro_text,num_of_most_common_words)
                    plt.bar(top_keywords.keys(), top_keywords.values())
                    plt.xticks(rotation=45)
                    #token_result['Token'].value_counts().head(num_of_most_common_words).plot.bar()
                    st.pyplot(fig)

                with st.expander('plot part of speech'):
                #     st.write("Here are some word stats...")
                    fig = plt.figure(figsize=(10,8))
                    token_result['PoS'].value_counts().plot.bar()
                    st.pyplot(fig)

                    # sns.countplot(x='PoS', data=token_result)
                    # plt.show()
                    

                with st.expander('plot word cloud'):
                    st.write("Here are some word stats...")
                    plot_wordcloud(text)


            with st.expander('Text Summarization download'):  
                st.write("Here are download file..")
                make_downloadable(token_result)
                    # st.write(token_result)

#ANCHOR -  nlp(file)
    elif choice == 'NLP(file)': 
        st.subheader("NLP(file):analyze text from file")    
        uploaded_file = st.file_uploader("Choose a file", type=['pdf','docx','txt'])
        num_of_most_common_words = st.sidebar.number_input("Number common tokne", 5,15)
        if uploaded_file is not None:
            if uploaded_file.type == 'application/pdf':
                raw_text  = read_pdf(uploaded_file)
                st.write(raw_text)
                

            elif uploaded_file.type == 'text/plain':
                raw_text = str(uploaded_file.read(),"utf-8")    
                #st.write(text)

            else:   
                raw_text  = docx2txt.process(uploaded_file)
                #st.write(text)
            
            with st.expander('Original Text'):  
                st.write(raw_text)  


            with st.expander('Text Analysis'):  
                token_result = text_analyzer(raw_text)   
                st.dataframe(token_result)
                    

            with st.expander('entity recognition'):   
                    # entity_result=get_entities(text)
                    # st.write(entity_result) 
                entity_result=render_entities(raw_text
                    )
                st.write(entity_result,unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                with st.expander('word stats'):
                    st.info('word stats here...')
                    docx= nt.TextFrame(raw_text)
                    st.write(docx.word_stats())


            with st.expander('top keywords'):
                st.info('top keywords here...')
                pro_text=nfx.remove_stopwords(raw_text) #good for removing stop words (etc:and,the,or,)
                most_common_tokens = get_most_common_tokens(pro_text,num_of_most_common_words)
                st.write(most_common_tokens)

            with st.expander('sentiment analysis'):
                st.write("Here are some word stats...")
                sentiment_result = get_sentiment(raw_text)
                st.write(sentiment_result)

            with col2:
                with st.expander('plot word frequency'):
                    st.write("Here are some word stats...")
                    fig = plt.figure(figsize=(10,8))
                    top_keywords = get_most_common_tokens(pro_text,num_of_most_common_words)
                    plt.bar(top_keywords.keys(), top_keywords.values())
                    plt.xticks(rotation=45)
                        #token_result['Token'].value_counts().head(num_of_most_common_words).plot.bar()
                    st.pyplot(fig)

            with st.expander('plot part of speech'):
                #     st.write("Here are some word stats...")
                try:
                    fig = plt.figure(figsize=(10,8))
                    token_result['PoS'].value_counts().plot.bar()
                    st.pyplot(fig)
                    # sns.countplot(x='PoS', data=token_result)
                    # plt.show()
                except:
                    st.write('No data to plot')

                        

            with st.expander('plot word cloud'):
                    st.write("Here are some word stats...")
                    plot_wordcloud(raw_text)


            with st.expander('Text Summarization download'):  
                st.write("Here are download file..")
                make_downloadable(token_result)
                        # st.write(token_result)     

    elif choice == 'About':
        st.subheader("About:about this app")




if __name__ == "__main__":  
    main()  