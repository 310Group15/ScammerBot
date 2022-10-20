from random import randrange


class readInput():
    curseWords = ["damn","crap"]
    iceBreakers = ["Hi, how are you?","How are you doing today?","Hey, how are you feeling?","Yo, how's it going?"]
    @staticmethod
    def validate(userInput):
        flag = True
        for word in readInput.curseWords:
            if word in userInput:
                print("inappropriate input: '{}' is not acceptable".format(word))
                flag = False
        return flag

    @staticmethod
    def startConvo():
        userInput = input("{}\n".format(readInput.iceBreakers[randrange(len(readInput.iceBreakers))]))
        if(readInput.validate(userInput)):
            return userInput


#test code
uinp=readInput.startConvo()
        
