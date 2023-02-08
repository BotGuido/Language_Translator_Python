# pip install googletrans==4.0.0-rc1
'''
The first thing we need to do is to import the required packages and modules.
In this project, we import the googletrans package to make use of its functions.
We will be importing the Translator class from the googletrans package.
'''
from googletrans import Translator

translator = Translator()

'''
Next, we will be defining a dictionary called language. 
In this dictionary, we fix all the languages code for 10+ languages like the following.
'''

language = {"bn": "Bangla",
            "en": "English",
            "ko": "Koren",
            "fr": "French",
            "de": "German",
            "he": "Hebrew",
            "hi": "Hindi",
            "it": "Italian",
            "ja": "Japanese",
            'la': "Latin",
            "ms": "Malay",
            "ne": "Nepali",
            "ru": "Russian",
            "ar": "Arabic",
            "zh": "Chinese",
            "es": "Spanish"
            }

'''
In the next section, we ask the user for the language code and check if it is valid or not.
'''

allow = True  # variable to control correct language code input

while allow:  # checking if language code is valid

    user_code = input(
        f"Please input desired language code. To see the language code list enter 'options' \n")

    if user_code == "options":  # showing language options
        print("Code : Language")  # Heading of language option menu
        for i in language.items():
            print(f"{i[0]} => {i[1]}")
        print()  # adding an empty space

    else:  # validating user input
        for lan_code in language.keys():
            if lan_code == user_code:
                print(f"You have selected {language[lan_code]}")
                allow = False
        if allow:
            print("It's not a valid language code!")

'''
In the last section, we will start translating the given text 
to the selected language with the help of the googletrans package. 
We will loop until the user enters close for the exit.
'''

while True:  # starting translation loop
    string = input(
        "\nWrite the text you want to translate: \nTo exit the program write 'close'\n")

    if string == "close":  # exit program command
        print(f"\nHave a nice Day!")
        break

    # translating method from googletrans
    translated = translator.translate(string, dest=user_code)

    # printing translation
    print(f"\n{language[user_code]} translation: {translated.text}")
    # printing pronunciation
    print(f"Pronunciation : {translated.pronunciation}")

    for i in language.items():  # checking if the source language is listed on language dict and printing it
        if translated.src == i[0]:
            print(f"Translated from : {i[1]}")