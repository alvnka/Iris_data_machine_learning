# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Uc3PNePg_HQKgjNGZ3B9il6BHq5kJIA3
"""
# @authors include 
## Mugo lazarus - CS/MG/1772/09/19
## Kamande Alvin A Ndung'u - CS/MG/2671/09/19
## Edwin Wachira - CS/MG/2926/09/19
import pandas as pd

from sklearn import datasets

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.svm import SVC
import pickle

#lazer
import streamlit as st
import pickle
import numpy as np

#load dataset
#from sklearn.datasets import load_iris as iris
from sklearn import datasets 
iris=datasets.load_iris()
X = iris.data

#print(iris)
X = iris.data
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(X,y)
lin_reg = LinearRegression()
log_reg = LogisticRegression()
svc_model = SVC()
line_reg = lin_reg.fit(x_train,y_train)
log_reg = log_reg.fit(x_train, y_train)
svc_model = svc_model.fit(x_train, y_train)
print(lin_reg.score(x_test, y_test))

pickle.dump(lin_reg,open('lin_model.pkl','wb'))
pickle.dump(log_reg,open('log_model.pkl','wb'))
pickle.dump(svc_model,open('svc_model.pkl','wb'))

lin_model=pickle.load(open('lin_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))
svc_model=pickle.load(open('svc_model.pkl','rb'))

def classify(num):
  if num < 0.5:
      return 'Setosa'
  elif num < 1.5:
      return 'Versicolor'
  else:
      return 'Virginica'
def main():
  st.title("Streamlit Tutorial")
  html_temp = """
  <div style="background-color: teal ;padding:10px">
  <h2 style="color:white;text-aling:center;">Iris Classification
  """
  
  st.markdown(html_temp, unsafe_allow_html = True)
  activities = ['Linear Regression','Logistic Regression','SVM']
  option=st.sidebar.selectbox('Which model do you want to use?', activities)
  st.subheader(option)
  st.spinner("Hello")
  sl=st.slider('Select Sepal Length ', 0.0, 10.0)
  sw=st.slider('Select Sepal Width ', 0.0, 10.0)
  pl=st.slider('Select Petal Length ', 0.0, 10.0)
  pw=st.slider('Select Petal Width ', 0.0, 10.0)
  inputs=[[sl, sw, pl, pw]]
  if st.button('Classify'):
    if option=='Linear Regression':
      st.success(classify(lin_model.predict(inputs)))
    elif option=='Logistic Regression':
      st.success(classify(log_model.predict(inputs)))
    else:
      st.success(classify(svc_model.predict(inputs)))

if __name__=='__main__':
  main()
