import json #the dictionary itself is a json fil,e so i need to be able to have python know how to load it using the json library 
from difflib import get_close_matches #I am using this library to get an estimate guees if the user miss-typed a word that exists in
					#the dictionary

data = json.load(open("data.json"))#I'm instructing Python to load this file into my variable called "data"

""" Down below is the function that will take care of predicting, matching and returning words and definitions """

def word(w): # This is where the users input is processed
    w = w.lower() # The input is made into lower case 
    if w in data: # if the input is in data then the definition will be returned 
	    return data[w]
    elif len(get_close_matches(w, data.keys())) > 0: # Here, the input is being compared to a similarity ration between the input and the words in the dictionary
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])""" The users input is then analuzed and is presented with the closest match at index 0 for the close matches of the word
	 and ask the user if the word they are looking for is the same as the estimate"""
        if yn == "Y" or "y":# If the user says yes, then the word and the definition will be showed to the screen                                                                                     
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or "n":# If the user response is no, then the program will simply say the word does not exist in its dictionary
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:# if the word cannot be compared to anything or its just someone bashing their keyboard, then the program will simply say its not in the dictionary
        return "That word is not in the dictionary, please double check it."

user = input("Enter word: ") #user input is accquired 
output = word(user) # the output of the word function is stored as output

""" Down below is a bit of code to make the outputs of the definitions in the dctionary to be more user frindly to the eye"""

if type(output) == list:# If the output is equal to the list as a list in the dictionary, then the for loop goes off
    for item in output: # stores output into item
        print(item) # prints out the output, but without quotes and other non neccessary marks
else:
    print(output)
