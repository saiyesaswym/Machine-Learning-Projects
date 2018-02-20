# SPAM/HAM CLASSIFIER 

This classifier is written in Python and the web applciation is built using FLASK. 

The Enron Email Corpus is used for training the mode. It is one of the biggest email data sources in the world. It has 600,000 emails spread over 2.5 GB. 

Naive Bayes classifier is built on the train data after tokenizing the sentences and creating the word features. The accuracy on the test data turned out to be 98.92%.

The classifier is serialized using 'Pickle' and dumped as a package to Flask. Using flask, a web application is designed by providing an interface using HTML & CSS. The flask application is deployed on the 'PythonAnywhere' web server. 

Web Application: http://saiyesaswy.pythonanywhere.com/

Here are some of the most informative features derived from the model:

Most Informative Features

