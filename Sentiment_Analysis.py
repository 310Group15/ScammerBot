import spacy 
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob
import Find_Subject
import search_tester
import SkimWikipedia
import random

def getWikiResponse():
    # create sentence based on inputted statement. search for proper noun or persons name in statemetn and assemble sentence based on noun or name. 
    # perform sentiment analysis on input, and cerate sentence that matches inputs sentiment 
    nlp = spacy.load('en_core_web_sm')

    nlp.add_pipe('spacytextblob')

    search = 'Abraham Lincon was the best president ever in the history of the world'
    nsubj = []
    aux = []
    dobj = []
    root = []
    noun = []
    definition = []
    SkimWikipedia.Create_Definition_list(search_tester.extract_search_term(Find_Subject.find_Subject(search)))
    nsubj = SkimWikipedia.Get_Wiki_nsubj()
    aux = SkimWikipedia.Get_Wiki_aux()
    dobj = SkimWikipedia.Get_Wiki_dobj()
    root = SkimWikipedia.Get_Wiki_root()
    noun = SkimWikipedia.Get_Wiki_noun()
    print(len(nsubj), '                                                  tesdt')
    print(len(aux), '                                                  tesdt') 
    print(len(dobj), '                                                  tesdt') 
    print(len(root), '                                                  tesdt')
    print(len(noun), '                                                  tesdt')
    # proper noun, adverb,verb, determiner,  verb, proper noun
    sentiment = Find_Subject.find_Sentiment(search)
    #if it fails:
    if sentiment is None:
        return False

    if sentiment >= 0: 
        return('ah, ', Find_Subject.find_Subject(search), 'I like how ' ,nsubj[random.randint(0,len(nsubj)-1)],dobj[random.randint(0,len(dobj)-1)],aux[random.randint(0,len(aux)-1)],root[random.randint(0,len(root)-1)],nsubj[random.randint(0,len(nsubj)-1)])

    if sentiment <= 0:
        return('ah, ', Find_Subject.find_Subject(search), 'I dislike how ' ,nsubj[random.randint(0,len(nsubj)-1)],dobj[random.randint(0,len(dobj)-1)],aux[random.randint(0,len(aux)-1)],root[random.randint(0,len(root)-1)],nsubj[random.randint(0,len(nsubj)-1)])