import  streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import langdetect
# Importer les packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
st.title('Text Abstractor: English & French')
texts = st.text_area("", placeholder="Entrez votre texte ici")


from data_clean import cleaning 
from sumy.summarizers.text_rank import TextRankSummarizer
# nettoyer le text 
text=cleaning(texts)
# Detect the language of the text
import langid
from util import config 
language, confidence = langid.classify(text)



config()

if language=="fr":
    
    # Créer un text parser utilisant de tokenisation
    parser = PlaintextParser.from_string(text, Tokenizer('french'))
elif language =="en":
    
      # Créer un text parser utilisant de tokenisation
    parser = PlaintextParser.from_string(text, Tokenizer('english'))

number_of_sentences_slider = st.slider("Number of sentences to summarize:", min_value=1, max_value=10, value=1)
if st.button('TextRankSummarizer'):
    # Importer le TextRankSummarizer
        from sumy.summarizers.text_rank import TextRankSummarizer
      
        # Initialiser le modèle
        summarizer_textrank =TextRankSummarizer()
        # Summariser en 5 phrases
        summary = summarizer_textrank(parser.document,  number_of_sentences_slider)
        # Regrouper les phrases
        text_summary = ""
        for sentence in summary:
            text_summary += str(sentence)
        st.write(text_summary)

if  st.button('LexRankSummarizer'):
# Initialiser le modèle
    summarizer_textrank = TextRankSummarizer()
# Summariser en 5 phrases
    summary = summarizer_textrank(parser.document,number_of_sentences_slider)
# Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence) + " "
    st.write(text_summary)
    
if st.button('LeaSummizer'):
    # Importer LsaSummarizer
    from sumy.summarizers.lsa import LsaSummarizer
    # Initialiser le modèle
    summarizer_lsa =LsaSummarizer()
    # Summariser en 5 phrases
    summary = summarizer_lsa(parser.document,number_of_sentences_slider)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
       text_summary += str(sentence)

    # Afficher le summary
    st.write(text_summary)