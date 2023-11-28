import spacy
from requests import get
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')



def cleaning(article_text):
    
   article_text = re.sub(r'[[\w]*]', ' ', article_text)
   # Supprimer les chaines de \xa0, \u200c
   article_text = re.sub(r'\xa0|\u200c', ' ', article_text)
   # Remplacer les espaces multiples par l'espace simple
   article_text = re.sub(r'/s+', ' ', article_text)
   # Remplacer l'espace en debut et fin de corpus
   article_text = re.sub(r'^\s|\s$', '', article_text)
   article_text = re.sub(r'^\n|\n$', '', article_text)
   return article_text
    