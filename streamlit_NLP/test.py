from gensim.summarization import summarize
from rouge import Rouge
import streamlit as st
import pandas as pd
import altair as alt

def evaluate_summary(summary, reference):    
    if not summary:
        return pd.DataFrame()

    r = Rouge()
    eval_score = r.get_scores(summary, reference)
    eval_score_df = pd.DataFrame(eval_score[0])    
    return eval_score_df

def main():
    st.title("Text Summarization and Evaluation")

    text = st.text_area("Enter Text","Type Here ..")

    if st.button("Analyze"):
        with st.spinner("Analyzing the text …"):
            my_summary = summarize(text)

            if my_summary:
                st.write(my_summary)
                eval_df = evaluate_summary(my_summary, text)

                if not eval_df.empty:
                    st.dataframe(eval_df)
                    eval_df['metrics'] = eval_df.index
                    c = alt.Chart(eval_df).mark_bar().encode(
                        x='metrics',y='rouge-1')
                    st.altair_chart(c)
                else:
                    st.write("No summary generated.")
            else:
                st.write("No summary generated.")

if __name__ == '__main__':
    main()