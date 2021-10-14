# SpamClassifier

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [About](#About)
  * [Deployement on Heroku](#deployement-on-streamlit)
  * [Directory Tree](#directory-tree)
  * [Technologies Used](#technologies-used)
  * [Future scope of project](#future-scope)


## Demo
Link: https://share.streamlit.io/prakharsrivastavaa7/spamclassifier/main/home.py


## Overview
A Spam Classifier which receives a user input and classifies it either as spam or not spam. Various models have been tested and the best performing model with the highest precision was selected for deployment. The webapp is deployed using streamlit sharing.

### Input Screenshots      
The landing page on loading the webapp is as follows
![image](https://user-images.githubusercontent.com/63156822/137364263-d28178e4-eeae-41b4-8596-e2bcf0d9cc9a.png)

The user can enter the text content as shown below

![image](https://user-images.githubusercontent.com/63156822/137364297-605efe03-6706-4381-b4ba-c69d04256c02.png)



### Output Screenshots
The output results fior varous mail inputs

![image](https://user-images.githubusercontent.com/63156822/137364341-628a038d-7c6b-43ad-90ab-c738f691840d.png)

![image](https://user-images.githubusercontent.com/63156822/137364363-13afff1b-5afd-41c2-abbf-94a6be71e135.png)

![image](https://user-images.githubusercontent.com/63156822/137364388-e6b48f43-22b6-449e-9568-e965fc606940.png)


  ### Flowchart
There are two main components of the project - Machine Learning based Model Fitting and Web Deployment Using Streamlit.
Initially data is preprocessed and unnecessary rows are removed and a new clean dataset is stored in anew csv file. 
The newly created dataset is opened in a new jupyter notebook where it is preprocessed and text cleaning is done using nltk components like stemming. 
Tfidf vectoriser and Count Vectoriser are used on the test data and then various model training techniques are used to get the best precision. Naive Bayes is one of the most commonly used technique to train text data therefore I used it here. Apart form that DecisionTree is used along with hyperparameter tuning to see the effect on precision. In the end voting classifier is used in which a combination of different techniques are combined to make a new combined model. This way the precision and accuracy can be altered and improved.

![Flowchart (1)](https://user-images.githubusercontent.com/63156822/137371084-50b88c60-1250-4f78-bc93-79a66f1ea325.png)


## About
The project has been designed as part of the evaluation scheme of my college course UCS757 - Building Innovative Systems. This project involves the use of Machine Learning to classify an input mail as spam or not.The data is preprocessed, visualised and then fitted on various models. LogisticRegression is one of the best performing models and therefore used in pickling. Voting classifier also gives high precision and therefore can be used as well.


## Deployment on Streamlit
The webapp is deployed using streamlit share (https://share.streamlit.io/) which allows the user to deploy a webapp created using streamlit.

## Directory Tree 
```
├── __pycache__
├── README.md
├── home.py
├── SpamClassifier.ipynb		
├── model.pkl
├── vectorizer.pkl
├── spamdata.csv
├── nltk.txt
├── Procfile
├── requirements.txt
├── data cleaning.ipynb
├── Flowchart_DS.pdf
├── I_O_Screenshots_DS.pdf
├── setup.sh
├── email.csv
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)
 [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 
 
 
 ## Future Scope

* Include various more classifiers such as url spam classifier
* Imporve Front-End 


