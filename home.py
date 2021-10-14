import streamlit as st
import pickle
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


def remove_special_characters(text, remove_digits=True):
    pattern=r'[^a-zA-z0-9\s]'
    text=re.sub(pattern,'',text)
    return text
from nltk.tokenize.toktok import ToktokTokenizer
#Tokenization of text
tokenizer=ToktokTokenizer()
#removing the stopwords
def cleantxt(text, is_lower_case=False):
    tokens = tokenizer.tokenize(text)
    ps = PorterStemmer()
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [ps.stem(token) for token in tokens if token not in set(stopwords.words('english'))]
    else:
        filtered_tokens = [ps.stem(token) for token in tokens if token.lower() not in set(stopwords.words('english'))]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

def main():
    html_temp = '''<div style="background-color: #1f5e6e;padding:10px"><h2 style="color:white;text-align:center;">Email Spam Classifier ML App </h2></div>'''
    st.markdown(html_temp,unsafe_allow_html=True)
    st.subheader("Built with Python and Streamlit by Prakhar")
    inputmail = st.text_area("Enter The Email Content")

    if st.button('Predict Mail'):
        # 1. preprocess
        transformedmail = remove_special_characters(inputmail)
        transfmail = cleantxt(transformedmail)
        # 2. vectorize
        vector_input = tfidf.transform([transfmail]).toarray()
        # 3. predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.error("This is a Spam Mail")
        else:
            st.success("This is Not a Spam Mail")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")    
    html_sub='''<h4 style="color:gray;text-align:center;">The project has been made as a part of the evalation process for the course UCS757. The project takes an input from the user and categorises it as a spam mail or not.</h4>'''
    st.markdown(html_sub,unsafe_allow_html=True)
if __name__=='__main__':
    main()
