from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from gensim.models import Word2Vec
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt 
from matplotlib import style
style.use("ggplot")


my_phrases = []
with open('feeds.txt') as my_file:
	my_phrases = my_file.readlines()


             
phrase = []
with open('feeds1.txt') as my_file1:
	phrases = my_file1.readlines()


vectorizer = TfidfVectorizer(min_df=3, stop_words='english')
all_phrases = phrase + my_phrases
my_features = vectorizer.fit_transform(all_phrases)
scores = (my_features[0, :] * my_features[1:, :].T).A[0]
best_score = np.argmax(scores)
answer = my_phrases[best_score]
print answer



