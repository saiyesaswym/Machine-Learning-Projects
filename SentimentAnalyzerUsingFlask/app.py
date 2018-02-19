import numpy as np
#need to 'conda install flask' for this to work
from flask import Flask, abort, jsonify, request, render_template
import json
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup


my_sent_classifier = pickle.load(open("sent_class.pkl", "rb"))
vectormodel = pickle.load(open("vect_model.pkl", "rb"))

app= Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route('/showsentiment',methods = ['POST', 'GET'])
def make_sentiment():
    if request.method=='POST':
        #all kinds of error checking should go here
        data = request.form['sentence']

        a = []
        a.append(clean_review(data))

        rev2 = vectormodel.transform(a)

        rev3 = rev2.toarray()

        revsent = my_sent_classifier.predict(rev3)

        if(revsent==0):
            review_data='Negative review'
        else:
            review_data="Positive review"

        class_final2 = "It's " + review_data
        #return our prediction

        return render_template("index.html", value2=class_final2,entered2=data)

def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict
   

def clean_review( raw_review ):
    #
    # Remove HTML
    review_text = BeautifulSoup(raw_review,"lxml").get_text() 
    #
    # Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    #
    # Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #
    # In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    
    #Stemming  using PorterStemmer
    ps = PorterStemmer()
    stemmed_words=[]
    for i in meaningful_words:
        stemmed_words.append(ps.stem(i))
    #
    # Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( stemmed_words )) 
    
if __name__=="__main__":
    app.run()
