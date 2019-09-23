import requests
import json

# URL
url = 'Devitapv.pythonanywhere.com/api'

# Change the value of experience that you want to test
r=requests.post(url,json=[{"MARRIAGE":2,"EDUCATION":2,"SEX":0},
                            {"MARRIAGE":1,"EDUCATION":3,"SEX":0},
                            {"MARRIAGE":0,"EDUCATION":4,"SEX":0},
                            {"MARRIAGE":1,"EDUCATION":3,"SEX":0},
                            {"MARRIAGE":1,"EDUCATION":2,"SEX":1},
                            {"MARRIAGE":1,"EDUCATION":2,"SEX":0},
                            {"MARRIAGE":2,"EDUCATION":4,"SEX":1},
                            {"MARRIAGE":1,"EDUCATION":2,"SEX":0},
                            {"MARRIAGE":1,"EDUCATION":3,"SEX":1},
                            {"MARRIAGE":0,"EDUCATION":2,"SEX":0}])
print(r.json())