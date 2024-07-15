from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

#called Fast APi Class
app=FastAPI()
# create a class of type sentence
class Sentence(BaseModel):
    Sentence:str

@app.post('/analysis/')
def analyzer(Sentence_reference:Sentence):
    blob=TextBlob(Sentence_reference.Sentence)

    y=blob.sentiment
    return y
#for now it's not working
@app.get('/')
def intro():
    return "worked"