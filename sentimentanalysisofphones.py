# -*- coding: utf-8 -*-
"""SentimentAnalysisOfPhones.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IG_zObkBeZYJYOUgp_8pq0YWI3A4Ok1u

### **Sentiment Analysis of Phones of different brands on the basis of their reviews**

**below are some commands used to import dataframes from my google drive to google colab**
"""

# This only needs to be done once in a notebook.
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
# This only needs to be done once in a notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# List .txt files in the root.
#
# Search query reference:
# https://developers.google.com/drive/v2/web/search-parameters
listed = drive.ListFile({'q': "title contains '.csv' and 'root' in parents"}).GetList()
for file in listed:
  print('title {}, id {}'.format(file['title'], file['id']))

# Download a file based on its file ID.
#
# A file ID looks like: laggVyWshwcyP6kEI-y_W3P8D26sz
file_id = '1-ShZIodEJGB285nrQ8Kq3nomagjIcqYQ'
downloaded = drive.CreateFile({'id': file_id})

downloaded.GetContentFile('reviews.csv')

# Download a file based on its file ID.
#
# A file ID looks like: laggVyWshwcyP6kEI-y_W3P8D26sz
file_id = '10iXUK9X8gPpWjxNc_5CnBrL8RE27aNGu'
downloaded = drive.CreateFile({'id': file_id})

downloaded.GetContentFile('items.csv')

"""**ls command is used to view all the present files in my colab**
 We have items.csv and reviews.csv :
- items.csv contains all the information about all the phones sold by amazon
- reviews.csv contains all the reviews given by users
"""

!ls

"""**we have imported pandas to manipulate these dataframes**"""

import pandas as pd

"""**read the information in the .csv files and place it in the respective variable dataframes**"""

df_review = pd.read_csv('reviews.csv')
df_item = pd.read_csv('items.csv')

df_review.head()

"""**since we do not need all the columns in the dataframe we are contracting the data frames**"""

df_item = df_item[['asin','brand']]
df_review = df_review[['asin','title','body']]

"""**here we have divided our "items" dataframe into a small dataframes based on their brands**"""

df_item_samsung = df_item[df_item['brand']=='Samsung']
df_item_apple = df_item[df_item['brand']=='Apple']
df_item_Nokia = df_item[df_item['brand']=='Nokia']
df_item_motorola = df_item[df_item['brand']=='Motorola']
df_item_Google = df_item[df_item['brand']=='Google']
df_item_HUAWEI = df_item[df_item['brand']=='HUAWEI']
df_item_Sony = df_item[df_item['brand']=='Sony']
df_item_Xiaomi = df_item[df_item['brand']=='Xiaomi']

"""**since we do not have reviews in our "items" dataframe we need to join "brand based dataframes" and "reviews" dataframe**"""

df_final_samsung = df_item_samsung.set_index('asin').join(df_review.set_index('asin'))
df_final_apple = df_item_apple.set_index('asin').join(df_review.set_index('asin'))
df_final_Nokia = df_item_Nokia.set_index('asin').join(df_review.set_index('asin'))
df_final_motorola = df_item_motorola.set_index('asin').join(df_review.set_index('asin'))
df_final_Google = df_item_Google.set_index('asin').join(df_review.set_index('asin'))
df_final_HUAWEI = df_item_HUAWEI.set_index('asin').join(df_review.set_index('asin'))
df_final_Sony = df_item_Sony.set_index('asin').join(df_review.set_index('asin'))
df_final_Xiaomi = df_item_Xiaomi.set_index('asin').join(df_review.set_index('asin'))

"""**There are possibilities that these dataframes might have null values in them so to remove those null values we have used the function dropna() function**"""

df_final_samsung = df_final_samsung.dropna()
df_final_apple = df_final_apple.dropna()
df_final_Nokia = df_final_Nokia.dropna()
df_final_motorola = df_final_motorola.dropna()
df_final_Google = df_final_Google.dropna()
df_final_HUAWEI = df_final_HUAWEI.dropna()
df_final_Sony = df_final_Sony.dropna()
df_final_Xiaomi = df_final_Xiaomi.dropna()

"""**nltk import**"""

import nltk
from nltk import sent_tokenize
from nltk import word_tokenize

nltk.download('punkt')

"""**We have taken the "title" section of the reviews to do further sentiment analysis... further we have converted it into lists for easy manipulation**"""

list_title_samsung = list(df_final_samsung['title'])
list_title_apple = list(df_final_apple['title'])
list_title_nokia = list(df_final_Nokia['title'])
list_title_motorola = list(df_final_motorola['title'])
list_title_google = list(df_final_Google['title'])
list_title_huawei = list(df_final_HUAWEI['title'])
list_title_sony = list(df_final_Sony['title'])
list_title_xiaomi = list(df_final_Xiaomi['title'])

"""**We tried tokenizing them into sentences and words but the sentimentIntensityAnalyzer that we have used doesn't need tokenized words... It automatically tokenizes them and lemmitizes them and finds the sentiment in them**"""

for x in list_title_samsung: 
  sentences = sent_tokenize(x)
  print(len(sentences))
  print(sentences)

for x in list_title_samsung: 
  words = word_tokenize(x)
  print(len(words))
  print(words)

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

list_clean_title = []
for word in list_title:
    word = WordNetLemmatizer().lemmatize(word)
    list_clean_title.append(word)

pip install twython

"""SentimenIntensityAnalyzer needs twython library to be installed"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer

import nltk
nltk.downloader.download('vader_lexicon')

"""**here we have created a function called sentiment_analyse**"""

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    return score

"""**convert list to string for sentiment analysis**"""

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1

sentiment_analysis_samsung = sentiment_analyse(listToString(list_title_samsung))

print(sentiment_analysis_samsung)

sentiment_analysis_apple = sentiment_analyse(listToString(list_title_apple))

sentiment_analysis_nokia = sentiment_analyse(listToString(list_title_nokia))

sentiment_analysis_motorola = sentiment_analyse(listToString(list_title_motorola))

sentiment_analysis_google = sentiment_analyse(listToString(list_title_google))

sentiment_analysis_huawei = sentiment_analyse(listToString(list_title_huawei))

sentiment_analysis_sony = sentiment_analyse(listToString(list_title_sony))

sentiment_analysis_xiaomi = sentiment_analyse(listToString(list_title_xiaomi))

"""**since the output of sentiment_analysis is a dictionary so we need to convert it into a list**"""

sentiment_list_samsung = []
for key, value in sentiment_analysis_samsung.items():
    temp = [key,value]
    sentiment_list_samsung.append(temp)

sentiment_list_apple = []
for key, value in sentiment_analysis_apple.items():
    temp = [key,value]
    sentiment_list_apple.append(temp)

sentiment_list_nokia = []
for key, value in sentiment_analysis_nokia.items():
    temp = [key,value]
    sentiment_list_nokia.append(temp)

sentiment_list_motorola = []
for key, value in sentiment_analysis_motorola.items():
    temp = [key,value]
    sentiment_list_motorola.append(temp)

sentiment_list_google = []
for key, value in sentiment_analysis_google.items():
    temp = [key,value]
    sentiment_list_google.append(temp)

sentiment_list_huawei = []
for key, value in sentiment_analysis_huawei.items():
    temp = [key,value]
    sentiment_list_huawei.append(temp)

sentiment_list_sony = []
for key, value in sentiment_analysis_sony.items():
    temp = [key,value]
    sentiment_list_sony.append(temp)

sentiment_list_xiaomi = []
for key, value in sentiment_analysis_xiaomi.items():
    temp = [key,value]
    sentiment_list_xiaomi.append(temp)

"""**here we have defined 4 functions to create lists for negetive neutral positive and compound sentiments**"""

def neg_list(dictlist_of_phones):
  neg_list_values = dictlist_of_phones[0][1]
  return neg_list_values

def neu_list(dictlist_of_phones):
  neu_list_values = dictlist_of_phones[1][1]
  return neu_list_values

def pos_list(dictlist_of_phones):
  pos_list_values = dictlist_of_phones[2][1]
  return pos_list_values

def compound_list(dictlist_of_phones):
  compound_list_values = dictlist_of_phones[3][1]
  return compound_list_values

phones_sentiment_list = [sentiment_list_samsung,sentiment_list_apple,sentiment_list_nokia,sentiment_list_motorola,sentiment_list_google,sentiment_list_huawei,sentiment_list_sony,sentiment_list_xiaomi]

print(phones_sentiment_list)

neg_list_plot = []
neu_list_plot = []
pos_list_plot = []
compound_list_plot = []
for phone in phones_sentiment_list:
  neg_list_plot.append(neg_list(phone))
  neu_list_plot.append(neu_list(phone))
  pos_list_plot.append(pos_list(phone))
  compound_list_plot.append(compound_list(phone))

print(neg_list_plot)
print(neu_list_plot)
print(pos_list_plot)
print(compound_list_plot)

"""**importing matplotlib for ploting sentiments**"""

import matplotlib.pyplot as plt
import numpy as np

x_axis_values = ['samsung','apple','nokia','motorola','google','huawei','sony','xiaomi']

plt.xticks(x, x_axis_values)
plt.plot(x,neg_list_plot,color='r')
plt.show()

plt.xticks(x, x_axis_values)
plt.plot(neu_list_plot,color='g')
plt.show()

plt.xticks(x, x_axis_values)
plt.plot(pos_list_plot,color='b')
plt.show()

plt.xticks(x, x_axis_values)
plt.plot(compound_list_plot,color='y')
plt.show()

"""**since we have a positive compound value it shows that they have a positive response in general**"""

plt.xticks(x, x_axis_values)
plt.plot(neg_list_plot,color='r')
plt.plot(neu_list_plot,color='g')
plt.plot(pos_list_plot,color='b')
plt.plot(compound_list_plot,color='y')

plt.show()