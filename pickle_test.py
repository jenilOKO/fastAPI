import csv
import random
import numpy as np
import pandas as pd
import difflib
from fastapi import FastAPI
import pickle as pkl
from collections import deque
import json

app = FastAPI()
dicts = {}
global json_file
list1 = ['Asian']
file = open('Prediction_Model.pkl', 'rb')
random_number = 25
SR_NO = random_number
# dump information to that file
similarity = pkl.load(file)
dataa = pd.read_csv('Design_full_demo.csv')

data1 = []
with open('Design_full_demo.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data1.append(row)

db_length = len(data1)

@app.get("/")
async def root(button_value : int):
    global list1, random_number, SR_NO, dicts
    #SR_NO = int(input('Enter Tile number: '))
    print(SR_NO)
    if button_value == 1:
        print(SR_NO)
        indexs = dataa['SR_NO'] == SR_NO
        index = dataa.index
        indexs = index[indexs]
        new_output = indexs.tolist()
        index_of_tile = new_output[0]
        print(index_of_tile)
        #index_of_tile = dataa[dataa.NAME == close_match]['SR_NO'].values[0]
        similarity_score = list(enumerate(similarity[index_of_tile]))
        sorted_similar_tile = sorted(similarity_score, key = lambda x:x[1], reverse = True)
        print("\n")
        print('Tile Suggested For You : \n')

        i = 1
        rec_SR = []
        for tile in sorted_similar_tile:
            index = tile[0]
            SR_from_index = dataa[dataa.index == index]['SR_NO'].values[0]
            if(i < 6):
                print(i,'.',SR_from_index)
                rec_SR.append(SR_from_index)
                i+=1
        
        print("\n")        
        print(sorted_similar_tile[1:6])
        
        
        name = 102
        number = 35
        #lists = [, name, list1[0], number]
        SR_NO = int(rec_SR[0])
        print(SR_NO)
        dicts = {
                'SR_NO': SR_NO, 
                'element2': name, 
                'element3': list1[0], 
                'element4': number
            }
    if button_value == 0:
        name = 102
        number = 35
        list1 = deque(list1) 
        list1.rotate(-1) 
        list1 = list(list1)
        print( list1)
        SR_NO = int(random.choice(list(dataa['SR_NO'])))
        dicts = {
            'SR_NO': SR_NO, 
            'element2': name, 
            'element3': list1[0], 
            'element4': number
        }
    
    return(dicts)
