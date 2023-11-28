import  streamlit as st
import streamlit as st
import langdetect
# Importer les packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
st.title('Text Abstractor: English & French')
texts = st.text_area("", placeholder="Entrez votre texte ici")
import nltk

from data_clean import cleaning 
from sumy.summarizers.text_rank import TextRankSummarizer
# nettoyer le text 
text=cleaning(texts)
# Detect the language of the text
import langid
from util import config 
language, confidence = langid.classify(text)

# Définir la taille de la police souhaitée
font_size = "20px"

# Définir la police de caractères souhaitée
font_family = "Times New Roman, serif"


# Définir la couleur du texte souhaitée (code hexadécimal)
text_color = "white"



config()

if language=="fr":
    
    # Créer un text parser utilisant de tokenisation
    parser = PlaintextParser.from_string(text, Tokenizer('french'))
    stopwords = nltk.corpus.stopwords.words('french')
elif language =="en":
    
      # Créer un text parser utilisant de tokenisation
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    stopwords = nltk.corpus.stopwords.words('english')

number_of_sentences_slider = st.slider("Number of sentences to summarize:", min_value=1, max_value=10, value=1)
if st.button('TextRankSummarizer',type='primary'):
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
        st.write(
                f'<div style="font-size: {font_size}; color: {text_color}; font-family: {font_family};">'
                f"{text_summary} "
                '</div>',
                unsafe_allow_html=True
            )   


if  st.button('LexRankSummarizer',type="primary"):
# Initialiser le modèle
    summarizer_textrank = TextRankSummarizer()
# Summariser en 5 phrases
    summary = summarizer_textrank(parser.document,number_of_sentences_slider)
# Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence) + " "
    st.write(
                f'<div style="font-size: {font_size}; color: {text_color}; font-family: {font_family};">'
                f"{text_summary} "
                '</div>',
                unsafe_allow_html=True
            )   
    
if st.button('LsaSummizer',type="primary"):
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
    st.write(
                f'<div style="font-size: {font_size}; color: {text_color}; font-family: {font_family};">'
                f"{text_summary} "
                '</div>',
                unsafe_allow_html=True
            )   

if st.button('Summarisation',type="primary"):
     sentence_list = nltk.sent_tokenize(text)
# Stopwords
     #stopwords = nltk.corpus.stopwords.words('french')
# Dictionnaire de fréquences des mots
     word_frequencies = {}
     for word in nltk.word_tokenize(text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
# Fréquence maximale
     maximum_frequency = max(word_frequencies.values())
# Calculer la fréquence pondérée
     for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequency
# Liste des scores de chaque phrase
     sentence_scores = {}
# Calculer le score de chaque phrase
     for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
# Ordonner les phrases par pondération et recupérer les 10 premières phrases
     summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=False)[:number_of_sentences_slider]
# regrouper ensemble les phrases qui ont les poids les plus élévés
     summary = ' '.join(summary_sentences)
     st.write(
                f'<div style="font-size: {font_size}; color: {text_color}; font-family: {font_family};">'
                f"{summary} "
                '</div>',
                unsafe_allow_html=True
            )   
    