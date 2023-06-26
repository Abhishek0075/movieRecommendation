import ast
import numpy as np
import pandas as pd

def convert(obj):
    l=[]
    for i in ast.literal_eval(obj) :
        l.append(i['name'])
    return l


def convert3(obj):
    l = []
    counter = 0
    for i in ast.literal_eval(obj) : 
        if counter != 3 :
            l.append(i['name'])
            counter+=1
        else : 
            break
        return l
    

credits_df=pd.read_csv("dataset/credits.csv")
movies_df=pd.read_csv("dataset/movies.csv")
merged=movies_df.merge(credits_df,on="title")

# merged['cast'] = merged['cast'].apply(convert3)
# merged['cast'] = merged['cast'].apply(convert3)
# merged['cast'] = merged['cast'].apply(convert3)
print(merged.head(2))