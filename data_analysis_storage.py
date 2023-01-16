# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 19:03:45 2023

@author: dell
"""

import json
import pandas as pd


def json_to_df(file):
    with open(file) as f:
        js_file=json.load(f)
        
    return pd.DataFrame(js_file)


authors_df=json_to_df('authors.json')

qs_df=json_to_df('quotes.json')

#data exploration
'''
print(authors_df.head())
print(authors_df.info())
print(qs_df.head())
print(qs_df.info())
'''
authors_df=authors_df.explode('quoteIds')

data_df=pd.merge(qs_df, authors_df, how='inner', left_on='id',right_on='quoteIds')
data_df=data_df.drop(['id_x','id_y'],axis=1)
