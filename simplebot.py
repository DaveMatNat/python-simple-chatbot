import random
####### GLOBAL VARIABLES #######

# DYNAMIC
user_name = ""                      # user's name input at the beginning
magic_word_ct = 0                   # number of times magic word is said
unlocked_password = False           # flag for whether or not the user said both passwords

# CONSTANTS
BOT_NAME = "$0mch4i"                       # your bot's name
EXIT_COMMAND = "goodbye"            # user input command to exit the program
MAGIC_WORD = "spicy"                     # magic word to check for in user input
PASSWORD1 = "Khobkhun"                      # first password to check in user input
PASSWORD2 = "Sabaidee"                      # second password to check in user input
SECRET_MESSAGE = "Seems like you know quite a few Thai words! You've made my day :D"                 # message to show if the user unlocked it with both passwords


# Additional variables below (if needed) #

thaiFoods = ["Pad Kra Pao","Koaw Mun Gai",
              "Moo Yahng with Sticky Rice",
                "Khao Pad",
                  "Massaman Curry"]

mangoFoods = ["Mango Sticky Rice",
               "Mango Chobani Yogurt",
                 "Mango Bingsu"]

defaultResponses = ["Oooo that's a good one...",
                     "555+", "UNRELATED but give me a few Thai words!",
                       "I'm Sorry?"]

popularBands = [
    "Led Zeppelin",
    "Pink Floyd",
    "The Rolling Stones",
    "Queen",
    "The Eagles",
    "AC/DC",
    "The Who",
    "Fleetwood Mac",
    "Aerosmith",
    "Metallica",
    "Guns N' Roses",
    "Nirvana",
    "The Clash",
    "The Police",
    "U2",
    "R.E.M.",
    "Red Hot Chili Peppers",
    "Jimi Hendrix",
    "Sade",
    "Bon Jovi"
]

popularDrinks = [
    "Coca-Cola",
    "Vanilla Milkshake",
    "Boba Tea",
    "Thai Tea with all my life",
    "Apple Juice",
    "Hokkaido Milk",
    "Red Wine",
    "Chai Tea Latte",
    "Lemonade",
    "Avocado Smoothie",
    "Hot Chocolate n Marshmallows",
    "Caramel Macchiato"
]
####### AI LOOP #######

# ask for the user's name and save it
user_name = input("What can I call you?> ")

# YOUR CODE HERE #

#Welcoming Text
print(f"Sawasdee Krub {user_name}! I'm {BOT_NAME}, what would you like to know about me?")

# enter user input loop
while True:
    # ask for user input
    user_input = input("> ").strip()

    # check if the user wants to exit with the exit command
    # 'break' comes out of the while loop. the AI will continue infinitely until the command is said
    if user_input.lower() == EXIT_COMMAND:
        break
    else:
        if user_input == "":
            print("Did you say something?")
            continue
        #Magic word & Password (Highest Priority)
        if MAGIC_WORD in user_input.lower():
            magic_word_ct += user_input.count(MAGIC_WORD)

        if (PASSWORD1 in user_input) and (PASSWORD2 in user_input):
            unlocked_password = True

        # WRITE YOUR 9 CONDITIONAL STATEMENTS #
        
        if "spicy" in user_input.lower():
            print("Say no more... I love Spicy foods!")

        elif "rice" in user_input.lower():
            print(f"Rice is NICE! I'd recommend getting \"{random.choice(thaiFoods)}\" if you ever end up coming to Thailand")
        
        elif "mango" in user_input.lower():
            print(f"I LOVE MANGOES!!! Help yourself by trying \"{random.choice(mangoFoods)}\"")
        
        elif user_input == "do you like dogs?":
            print("I like Dogs...But they don't like me ;(")
        
        elif user_input == "what is your favorite drink?":
            print(f"Lowkeyy I LOVEEEEE {random.choice(popularDrinks).upper()}!!")
        
        elif user_input == "what is your favorite band?":
            print(f"That's a really hard one... I'm currently addicted to \"{random.choice(popularBands)}\"")    
        
        else:
            print(random.choice(defaultResponses))

# say goodbye to the user
print("\nI'm sad to see you leaving me alone here in this Digital World...")
 
# print the magic phrase count if it was more than 0
print(f"You said the Magic Word {magic_word_ct} time(s)!") if magic_word_ct else None

# check whether the user entered the correct passwords, and print a secret message if so
print(SECRET_MESSAGE) if unlocked_password else None

# YOUR CODE HERE #
