import spacy 
from spacy.matcher import Matcher
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob




#Finds Subject of sentence, if no subject is found returns false

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
def find_Subject(inputs):
    
    piano_class_doc = nlp(inputs)
    sents = []
    sents = list(piano_class_doc.sents)
    
    for sentence in sents:
        sent = sentence
        print(sent)
        for ent in sent.ents:      
            if ent.label_ == 'PERSON':                    #pos to identify search term
                print(ent.text + '     :person')
                return ent.text
        for token in sent:
            if token.tag_ == 'NNP':
                print(token.text + '     :noun')
                return token.text
def find_Sentiment(inputs):
    
    piano_class_doc = nlp(inputs)
    sents = []
    sents = list(piano_class_doc.sents)
    for sentence in sents:
        sent = sentence
        for ent in sent.ents:      
            if ent.label_ == 'PERSON':                    #pos to identify search term
                print(ent.text + '     :person')
                blob = TextBlob(str(sent))
                print(blob.sentiment_assessments.polarity)
                return blob.sentiment_assessments.polarity
        for token in sent:
            if token.tag_ == 'NNP':
                print(token.text + '     :noun')
                blob = TextBlob(str(sent))
                print(blob.sentiment_assessments.polarity)
                return blob.sentiment_assessments.polarity   