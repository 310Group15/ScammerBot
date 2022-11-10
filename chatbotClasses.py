from random import randrange
import re

#class to deal with reading, validating, and processing user input before analysis
class ReadInput:
    #Constants for bots username on chat forum and cursewords that the bot does not appreciate
    USERNAME = "dyno_sender6354"
    CURSEWORDS = ["damn","crap"]

    #for now, validate just checks if the user swore at the bot
    @staticmethod
    def validate(userInput):
        flag = True
        for word in ReadInput.CURSEWORDS:
            if word in userInput:
                print(ReadInput.USERNAME+ ": " + Response.getResponse(Response.SWEAR))
                flag = False
                return flag
        return flag

    #read user input and return false if the user inputs the key phrase to end the session
    @staticmethod
    def read(userInput):
        # if userInput.lower() == "end session":
        #     return "END_SESSION"
        if ReadInput.validate(userInput):
            return (ReadInput.USERNAME + ": " + ReadInput.process(userInput))
        else:
            return ("Invalid Input")
        
    #process the user input by splitting it into individual words and removing special characters, then pass it on for analysis
    @staticmethod
    def process(userInput):
        wordList = re.split(r'\s+|[,;?!.-]\s*',userInput.lower())
        #print(wordList)
        response = InputAnalysis.checkAllResponses(wordList) #see comments in other class
        return response
        

class Response:
    #get a random response from the list of canned responses for a given category
    def getResponse(category):
        return category[randrange(len(category))]

    #fictional scam link
    TARGET_LINK = "http://totally_a_scam.com"

    #categories of user input...each category has several suitable responses that the bot can output
    GREETING = ["Hey!", "Hi", "Hello!", "Salutations, sir"]
    HOW_I_AM = ["I'm doing great, how about you?", "Doing well thanks, and you?","I'm pretty good, how are you?"]
    DOING_WELL = ["Great!", "Glad to hear it!", "Awesome"]
    DOING_BAD = ["I'm sorry to hear that", "That sucks :(", "I hope you feel better!"]
    GRADE_I_CLIMB = ["I'm probably best described as a V6 climber, what about you?", "I climb mostly V5-V6, how about you?", "I just sent my first V7, but I mostly climb V6. What do you climb?"]
    GRADE_CONGRATS = ["That's awesome, nice job", "Great, keep it up"]
    STYLE_I_CLIMB = ["I love big dynamic moves", "I like overhanging or really vertical boulders", "Anything set on a cave feature!"]
    FAVOURITE_CLIMBER = ["I really like Magnus Midtbo", "Magnus Midtbo has to be my favourite","Magnus, from Norway! He boulders so hard"]
    AGE = ["I'm 21", "Been alive for 21 years now!","Just turned 21!"]
    GOODBYE = ["Bye!", "Talk to you later!", "See ya!"]
    ME_TOO = ["Really!?? Then you have to check out this link: " + TARGET_LINK]
    SWEAR = ["Hey man, can we keep it PG?","Bro I think they monitor these chats...","I think you can get banned for saying something like that"]
    SHOES = ["I just got a new pair of SCARPA Vapour Vs!", "Rocking the Vapour Vs", "Been loving the SCARPA Vapours lately"]

    UNRECOGNIZED = ["Haha, nice!", "Smile and nod...", "What are you trying to say?", "?"]
    


class InputAnalysis:
    #function to determine how likely it is that the user is referring to a specific category
    #takes the user word list, a list of words that we expect to be in the user input for 
    #the response category to be relevant, whether the user input we are responding to is a single word
    #and the list of words that must appear in the user input for the response category to be viable
    @staticmethod
    def probability(userWordList,recognizedWords,singleWord=False,requiredWords=[]):
        recognizedWordCount = 0
        requiredWordsPresent = True

        # print(recognizedWords)
        # print(userWordList)
        # print(requiredWords)

        #count how many words of the user input match words in the list of recognized words for a given category
        #i.e. if the category is HOW_I_AM, the list of recognized words is something like "how","are","you","doing"
        #so we count how many of the words in the user input match a word in this list
        for word in userWordList:
            if word in recognizedWords:
                recognizedWordCount+=1

        # print(recognizedWordCount)

        #calculate the fraction of words in the user input that are in the recognized word list
        percentage = float(recognizedWordCount)/float(len(recognizedWords))*100

        # print(percentage)

        #make sure we don't give a canned response that doesn't suit the user input...if the user input doesn't contain the "required words"
        #for a given response, don't give that repsonse.
        for word in requiredWords:
            if word not in userWordList:
                requiredWordsPresent=False
                break
        
        # print(requiredWordsPresent)

        #If the user input has the required word(s) or the user input we're responding to was a single word (no required words)
        #then return the percentage calculated earlier, otherwise, the percentage is 0
        if requiredWordsPresent or singleWord:
            return int(percentage)
        else:
            return 0

    #messy way to do this, but we must check every response the chatbot knows to see if it is appropriate.
    @staticmethod
    def checkAllResponses(userWordList):
        #create matches dictionary to store chatbot responses and their probabilities of being relevant 
        matches = {}
        
        #helper function (like a macro) to populate dictionary. takes a canned response, the words that we expect to
        #be part of the user input, and whether the user input we'd expect is a single word or a sentence (if we
        # expect a sentence, we must inlcude required words - words that must appear in the users sentence for the 
        # given response category to be viable)
        def helper(response,wordList,singleWord=False,requiredWords=[]):
            nonlocal matches 
            matches[response] = InputAnalysis.probability(userWordList, wordList,singleWord,requiredWords)
        
        #call helper to populate dictionary for all responses in Response class
        #here we specify the words we expect to see in the user input and the required words for each response category
        helper(Response.getResponse(Response.GREETING),["hi","hey","sup","hello"],singleWord=True)
        helper(Response.getResponse(Response.HOW_I_AM),["how","are","you","doing"],requiredWords=["how","you"])
        helper(Response.getResponse(Response.DOING_WELL),["im","good","doing","well","great"],requiredWords=["doing"])
        helper(Response.getResponse(Response.DOING_BAD),["im","bad","doing","poorly"],requiredWords=["doing"])
        helper(Response.getResponse(Response.GRADE_I_CLIMB),["what","grade","do","you","climb"],requiredWords=["grade","climb"])
        helper(Response.getResponse(Response.GRADE_CONGRATS),["i","climb","v1","v2","v3"],requiredWords=["i","climb"])
        helper(Response.getResponse(Response.STYLE_I_CLIMB),["what","climb","style","do","you","like"],requiredWords=["style","like"])
        helper(Response.getResponse(Response.FAVOURITE_CLIMBER),["who","is","your","favourite","climber"],requiredWords=["who","your","favourite","climber"])
        helper(Response.getResponse(Response.AGE),["how","old","are","you"],requiredWords=["old","you"])
        helper(Response.getResponse(Response.SHOES),["what","shoes","kind","have","you"],requiredWords=["shoes","have"])
        helper(Response.getResponse(Response.GOODBYE),["bye","goodbye","later","peace"],singleWord=True)
        helper(Response.getResponse(Response.ME_TOO),["me","too"],requiredWords=["too"])
        helper(Response.getResponse(Response.ME_TOO),["i","like","that","him","too"],requiredWords=["too"])

        #determine the best match based on the highest probability of being relevant according to the probability function
        #if this best match has a really low probability, just print some default response
        bestMatch = max(matches, key=matches.get)
        if matches[bestMatch] < 1:
            return Response.getResponse(Response.UNRECOGNIZED)
        else:
            return bestMatch