# -*- coding: utf-8 -*-
"""Article Data Processing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BD4J_VfrIGyjEeHOcd23EkOxXg19bErm
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
train=pd.read_csv('/content/train (1).csv')
train.head()

article=pd.read_csv('/content/article_info.csv')
article.head()

train=train.dropna(axis=0)
article=article.dropna(axis=0)

ratings = train.merge(article[['article_id','title', 'website']], how='left', 
                           left_on = 'article_id', right_on = 'article_id')
ratings.head()

ratings['article'] = ratings['article_id'].map(str) + str(': ') + ratings['title'].map(str) + str(': ') + ratings['website'].map(str)

ratings.head()

ratings['rating'].unique()

ratings.isnull().sum()

one=ratings['rating']==1
ratings_one=ratings[one]
ratings_one.head()

two=ratings['rating']==2
ratings_two=ratings[two]
ratings_two.head()

three=ratings['rating']==3
ratings_three=ratings[three]
ratings_three.head()

four=ratings['rating']==4
ratings_four=ratings[four]
ratings_four.head()

five=ratings['rating']==5
ratings_five=ratings[five]
ratings_five.head()

ratings_one=ratings_one.drop(['user_id'],axis=1)
rating_two=ratings_two.drop(['user_id'],axis=1)
ratings_three=ratings_three.drop(['user_id'],axis=1)
ratings_four=ratings_four.drop(['user_id'],axis=1)
ratings_five=ratings_five.drop(['user_id'],axis=1)

ratings_one.head()

ratings_two.head()

ratings_three.head()

ratings_four.head()

ratings_five.head()

pd.DataFrame(ratings_one).to_csv('rating_one.csv',index=None)
pd.DataFrame(ratings_two).to_csv('rating_two.csv',index=None)
pd.DataFrame(ratings_three).to_csv('rating_three.csv',index=None)
pd.DataFrame(ratings_four).to_csv('rating_four.csv',index=None)
pd.DataFrame(ratings_five).to_csv('rating_five.csv',index=None)
