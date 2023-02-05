import pandas as pd
import re
import sqlite3

import nltk #Natural Language Tool Kit for pre-processing
# nltk.download('omw-1.4')
# nltk.download('stopwords') #Stopwords removal
# nltk.download('wordnet') #To find Synonyme & Antonyme
from nltk.corpus import stopwords
stopwords = stopwords.words("english")
stopwords.extend(['advanced', 'intelligent', 'multidisciplinary', 'systems', 'aims', 'lab'])
from nltk.stem import WordNetLemmatizer #Lemmatization
lemmatizer = WordNetLemmatizer()

import spacy
# nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('en_core_web_lg')



# Fettch Database Table
def db_to_df(database, table):
    conn = sqlite3.connect(database)
    df = pd.read_sql(
        "select * from "+table,
        conn)
    conn.close()
    return df
database = "Database/AIMS_Lab.sqlite"


# Preprocessing
def preprocessing(text: str):
  NonSymbolicTweet_i = re.sub("[^a-zA-Z0-9]"," ",text)
  LowerTweet_i = NonSymbolicTweet_i.lower()
  TokenizedWordsOfTweet_i = LowerTweet_i.split()

  #Lemmatization
  LemmaWordsOfTweet_i = [lemmatizer.lemmatize(w) for w in TokenizedWordsOfTweet_i if w  not in stopwords ]
  CleanedTweet_i = " ".join(LemmaWordsOfTweet_i)
  return CleanedTweet_i


# Similarity check
def spacy_similarity(doc1, doc2):
  doc1 = nlp(doc1)
  doc2 = nlp(doc2)
  return doc1.similarity(doc2)

# Return similar query
def spacy_cosine(text:str, col:list):
  text = preprocessing(text)
  max_sim = 0
  similar_q = ''
  for q_raw in col:
    q = preprocessing(q_raw)
    sim = spacy_similarity(text,q)
    if sim > max_sim:
      sim , max_sim = max_sim, sim
      similar_q = q_raw
  return similar_q

# df = db_to_df(database, 'Lab_Info')
# col = df["queries"]

# texts = [
#     "Who is the founder of the aims lab?",
#     "What is the goal of the lab?",
#     "When was the lab established?",
#     "What is the mission of the lab?",
#     "What is the field of research of the lab?"]
# for text in texts:
#     similar_q = spacy_cosine(text, col)
#     print(f"\nAsked Query: {text} \nSimilar Que: {similar_q}\n")

def most_sim_query(text):
    df = db_to_df(database, 'Lab_Info')
    col = df["queries"]
    similar_q = spacy_cosine(text, col)
    return similar_q