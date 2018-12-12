import random

def easy():

    print("\nWelcome to Easy Mode!!!\nYou get 10 tries and need to guess a number between 1-50.")
    secret_num = random.randint(1, 50)
    tries = 10

    while tries >=0:
        guess_int = int(input("Guess a number: "))
        if guess_int < secret_num:
            print("\nGuess higher!")
            tries -= 1
            print('You now have ' + str(tries) + ' tries left.')
        if guess_int > secret_num:
            print("\nGuess lower!")
            tries -= 1
            print('You now have ' + str(tries) + ' tries left.')
        if guess_int == secret_num:
            print("\nYOU GOT IT!!! THE NUMBER WAS " + str(secret_num) + "!");break
        if tries == 0:
            print('\nWell you have ran out of tries...');break

    choice = input("\nChoose 1 = restart | 2 = main menu | 3 = exit :  ")

    if choice == "1":
            easy()
    if choice == "2":
        mainMenu()
    if choice == "3":
        exit()


def normal ():
    print("\nWelcome to Normal Mode!!! You have 10 tries and you need to guess a number between 1-100.")
    secret_num = random.randint(1, 100)
    tries = 10

    while tries >=0:

        guess_int = int(input("Guess a number: "))

        if guess_int < secret_num:
            print("\nGuess higher!")
            tries -= 1
            print('You now have ' + str(tries) + ' tries left.')
        if guess_int > secret_num:
            print("\nGuess lower!")
            tries -= 1
            print('You now have ' + str(tries) + ' tries left.')
        if guess_int == secret_num:
            print("\nYOU GOT IT!!! THE NUMBER WAS " + str(secret_num) + "!");break
        if tries == 0:
            print("You've ran out of tries...");break

    choice = input("\nChoose 1 = restart | 2 = main menu | 3 = exit :  ")

    if choice == "1":
        normal()
    if choice == "2":
        mainMenu()
    if choice == "3":
        exit()

def jackpot():
    print("\nWell aren't you feeling lucky? Welcome to Jackpot Mode!!!\nYou only get one try to guess a number 1 - 1,000,000\nGOOD LUCK!!!")
    secret_num = random.randint(1, 100000000)
    tries = 1

    while tries >= 0:
        guess_int = int(input("Guess a number: "))

        if guess_int == secret_num:
            print("\nYOU GOT IT!!! HOLY S@#$T!!! THE NUMBER WAS " + str(secret_num) + "!");break
        if tries != secret_num:
            print("\nHey, I can't even get an A+ so yeah...\n");break

    choice = input("Choose 1 = restart | 2 = main menu | 3 = exit :  ")

    if choice == "1":
        jackpot()
    if choice == "2":
        mainMenu()
    if choice == "3":
        exit()

def mainMenu():

    choice = input("\nWhat are you willing to go for in terms of actually guessing this number?\n\n1 = easy, 2 = normal, 3 = jackpot: ")

    if choice == "1" :
        easy()
    elif choice == "2":
        normal()
    else:
        jackpot()

mainMenu()