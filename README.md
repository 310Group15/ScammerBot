# ScammerBot
## Concept behind chatbot
The idea behind our chatbot is to analyze user input as a list of words. Then, we have a bunch of canned responses that are deemed relevant based on how many words in the user input match words we would expect in a statement relating to the category of the canned response. For example, a category could be SHOES, with canned responses like "I have xxx climbing shoes, i love them!", the words we would expect to elicit this response would be things like "what", "kind", "of", "shoes", "have", and "you". We also have a list of required words for a given response category. These words MUST be present to elicit a response from that category. For the case of SHOES, these keywords might be "shoes" and "you". For responses to user inputs like "hi", "hey", etc. (single word inputs that can be responded to with a response from the GREETING category for example), we have no required words.
## Classes
All are contained within chatbotClasses.py
# ReadInput
Responsible for reading user input, validating it (for now, this consists of checking for cursewords), and processing it for analysis by splitting the input into individual words and eliminating special characters
# Response
Stores bot response categories and a list of responses for each category. This includes the scam target link. Also has a function to randomly select a response from a response category
# InputAnalysis
This class is the bulk of the chatbot; it houses the probability function to determine how likely it is that a given canned response will be appropriate based on how many words from the user input match the words we would expect in a statement relating to that category and whether the user input contains the requried words. The class also contains the checkAllResponses function which compiles a dictionary of canned responses from each category and the probability score for each canned response.