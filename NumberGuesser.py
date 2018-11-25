import random

print('Welcome to my number guessing game!!! \n \nYou will guess a number between 1 and 50 and you will have 10 tries to get it! GOOD LUCK!!!')

secret_num = random.randint(1, 50) # random is selecting any integer from 1 to 50

tries = 10

while tries >= 1 :
    print("") # Space to make the words easier to see
    guess = input("Guess a number: ")# Where the user will guess
    guess_int = int(guess)# the guess is turned from integer to a string so that its can match up to the secret number

    if guess_int < secret_num :
        print("") #Space to make the words easier to see
        print("Guess higher!") #HINT IF NUMBER IS TOO HIGH
        tries = tries -1 # This is to subtract the tries you have left
        print('You have ' + str(tries) + ' tries left!') # To inform the player of how many tries they have left
    if guess_int > secret_num :
        print("") #Space to make the words easier to see
        print("Guess lower!") # HINT IF NUMBER IS TOO LOW
        tries = tries - 1
        print('You have ' + str(tries) + ' tries left!') # To inform the player of how many tries they have left
    if guess_int == secret_num:
        print("")  # Space to make the words easier to see
        print("YOU GOT IT!!! " + "THE NUMBER WAS " + str(secret_num) + "!"); break
    if tries == 0:
        print('Opps, you\'ve ran out of tries...'); break



                                            #### NOTES ####

#1. On line26, this code only runs if the guess is equal to the number the player has guessed. After the semicolon,
#   the break is to make the code stop looping and asking for another guess even if it has already been guessed.

#2. On line 27, this is to make the code stop looping after the player has exceeded the tries that were available.
#3. I will be working on a way to make this code loop again if the player wishes to play again without having to close out of the program.