#version 1
#starting my quiz
print("𝖜𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝖙𝖍𝖊 𝖋𝖔𝖔𝖙𝖇𝖆𝖑𝖑 𝖖𝖚𝖎𝖟")
# This is a mini quiz asking users what they like!
#Variable and Constants
import os # This is my module - for clearing text
import time #This is for time
import random

ADULTAGE = 18 #This is my constant - this sets my age for 'adult'

#Functions

#Clearing the text
def clearText():
    os.system('cls' if os.name == 'nt' else 'clear')

#Welcome text
print("Hello! Welcome to this program where you answer questions and I judge you...")
age = int(input("Hey how old are you... please enter your age!: "))

#Age check
if age > ADULTAGE:
    print("You are way too old to be at High School... go home")
    exit()
else:
    #Checking if the user is ready?
    ready = input("Are you ready to play? ").lower()
    if ready == "yes":
        #Giving instructions
        print("Perfect lets begin... \nThis game is easy... you just answer the questions with the options given \n Make sure you are spelling it correctly!")
        time.sleep(1.5)
        clearText()
    
#This is my list of questions
        questions = ["1.who scored most goal in football history?"
                     "2.who is the most ballon'dor winner?"
                     "3.how many english manger has ever won the premier league?"
                     "4.who is the bundesliga all-time top goal scorer?"
                     "5.which is the only club to have won all three of the champions league,europe league and connference league?"
                     "6.which country won the most world cup?"
                     "7.who won 2022 world cup?"
                     "8.who won the 2018 world cup"
                     "9.who won the champinons league in 2016,2017,2018?"
                     "10 how much world cup did brazil won?"

            ]

# This is my list of responses
        responses = [
            ]
        
        for q in questions:
            input(q)
            print(random.choice(responses))
           


    else:
        print("Oh... goodbye then")
        exit()

