import numpy as np
#need to 'conda install flask' for this to work
from flask import Flask, abort, jsonify, request, render_template
import json
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


my_spam_classifier = pickle.load(open("spam_class.pkl", "rb"))


app= Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route('/showclass',methods = ['POST', 'GET'])
def make_predict():
    if request.method=='POST':
        #all kinds of error checking should go here
        data2 = request.form['number1']

        #predict_request = json.loads(data)
        #words = data['text']
        words = data2.replace('//','')
        words.replace("\\",'')
        words.replace('\n','')
        words = word_tokenize(words)
        my_data = create_word_features(words)
        #convert our json to a numpy array

        class_final = "It's " + my_spam_classifier.classify(my_data)
        #return our prediction

        return render_template("index.html", value=class_final, entered=data2)


def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict



if __name__=="__main__":
    app.run()