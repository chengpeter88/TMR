import sys

import streamlit as st
#print(st.write(sys.executable))
import nltk
#nltk.download('punkt')

#nltk.data.path.append('/path/to/your/punkt/resource')
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer   
from sumy.summarizers.lex_rank import LexRankSummarizer 
from rouge import Rouge 
import pandas as pd    
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib
plt.style.use('seaborn-darkgrid')
import seaborn as sns
import os
import altair as alt     
@st.cache   
def evaluate_summary(summary,reference):    
    r = Rouge()
    eval_score = r.get_scores(summary,reference)
    eval_score_df = pd.DataFrame(eval_score[0])    
    return eval_score_df

def sumy_summarize(doc,num=2):
    parser = PlaintextParser.from_string(doc, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, num)
    summary = [str(sentence) for sentence in summary]
    result = ' '.join(summary)  
    return result


def main():
    ## simple summarization NLP app 

    st.title(" Summarization NLP App")
    menu = ["Home", "About"]    
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        text = st.text_area("Enter Text")
        if st.button("Summarize"):
            with st.expander("Original Text"):
                st.write(text)

        c1,c2 = st.columns((1,1))   
        with c1:
            with st.expander('lexrank summary'):
                my_summary = sumy_summarize(text)
                document_len = {"Original":len(text),
                                "Summary":len(my_summary)}
                st.write(document_len)
                st.write(my_summary)  
            

                st.info('Rouge Score')
                eval_score = evaluate_summary(my_summary, text)  
                st.write(eval_score)
                st.write(eval_score['rouge-1']['f'])
                st.dataframe(eval_score.T)
                eval_score['metrics'] = eval_score.index
                c = alt.Chart(eval_score).mark_bar().encode(
                    x='metrics', y='rouge-1'
                )   

                st.altair_chart(c, use_container_width=True)
        with c2:
            with st.expander("TextRank Summary"):
                my_summary = summarize(text)
                document_len = {"Original":len(text),
                        "Summary":len(my_summary)}
                st.write(document_len)
                st.write(my_summary)
                st.info("Rouge Score")
                eval_df = evaluate_summary(my_summary,text)
                st.dataframe(eval_df)
                eval_df['metrics'] = eval_df.index
                c = alt.Chart(eval_df).mark_bar().encode(
                    x='metrics',y='rouge-1')
                st.altair_chart(c)

    elif choice == "About":

        # 建立兩個並排的欄位
        col1, col2 = st.columns(2)

        # 在第一個欄位中顯示文字
        col1.text('這是第一個欄位')

        # 在第二個欄位中顯示文字
        col2.text('這是第二個欄位')
    else:
        st.subheader("About")
        st.write("This is a NLP app for text summarization")



if __name__ == "__main__":  
    main()