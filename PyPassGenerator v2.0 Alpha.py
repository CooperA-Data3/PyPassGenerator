# This is just going to be a straight up password generator via the console i cannot be bothered to make this work with a GUI


# Imports
import random # To make things random
import string # because pythons sucks and cant join different data types into a single string
import time # To set delays when needed
import pyperclip # to copy the password (im too lazy to copy it myself)
import numpy # For more math shenannigans


class password:
    words = [
        "Apple", "Table", "Carrot",
        "Banana", "Turtle", "Flower",
        "Cherry", "Orange", "Window",
        "Giraffe", "Yellow", "Hammer",
        "Circle", "Dragon", "Sphere",
        "Anchor", "Planet", "Guitar",
        "Rabbit", "Butter", "Donkey",
        "Pocket", "Cotton", "Breeze",
        "Laptop", "Puzzle", "Forest",
        "Marble", "Rocket", "Candle",
        "Bumble", "Helmet", "Camera",
        "Castle", "Feather", "Purple",
        "Wallet", "Basket", "Crayon",
        "Collar", "Lizard", "Wrench",
        "Summer", "Winter", "Spring",
        "Orange", "Screen", "Fallen",
        ]
    symbols = ['!', '@', '#', '$', '*', '%']
    
    # Function to get a random choice from the array of words
    def getWord(self):
        self.chosenWord = random.choice(self.words)
        # print(self.chosenWord) # Debugging
        return self.chosenWord

    
    # Function to chose random symbol from the "symbols" array
    def getSymbol(self):
        self.chosenSymbol = str(random.choice(self.symbols))
        # print(self.chosenSymbol) # Debugging
        return self.chosenSymbol


    def getNumber(self):
        self.chosenNumber = str(random.randint(100,9999))
        # print(self.chosenNumber) # Debugging

    def join(self):
        self.getWord()
        self.getSymbol()
        self.getNumber()

        self.final = self.chosenWord + self.chosenSymbol + self.chosenNumber
        return self.final



generatePass = password()
finalPass = generatePass.join()
print(f"Password: {finalPass}")
pyperclip.copy(finalPass)
print("\nPassword Copied to Clipboard!\n")
x = 10
while x != 0:
    print(f"Program will close in {x} seconds")
    x -= 1
    time.sleep(1)




