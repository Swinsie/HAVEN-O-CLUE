# Written by Swinsor - you may edit and use this code, you may not redistribute the game or the entities of this project without modification and attribution to the source.
# Please see the licencing.


# Module Importation
import time
import random
import sys
from time import sleep


# Values
skillset = ['complaining','complaining that dave broke the code when you know you broke it while trying to "test" it','cooking super noodles']
budget = 100000
popularity = 0
pclifespan = 0


# Main Code
time.sleep(1)
words = "So, you've been hired for a job you don't have the qualifications for. \nYou're now a project manager for a team of 4 programmers. You must maintain the budget and also gain popularity within the team. \nYou don't have a scooby-do what they're doing since you only watched the first 10 minutes of the Matrix. \nYour mission is to safely and steadily lead the project until final release, goodluck, unworthy staff member."
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
print('')
words = '\nYOUR BOSS:'
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
words = "\nTell me, what is your name? I promise you I'm not Mark Zuckerberg.\n"
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
name=input()
words = '\nextracting(data) -- execute.tl'
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(0.5)
words = '\nSOLD DATA SUCCESSFULY'
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(1)
words = '\n\nWelcome to the programming department, ' + name + '. Bub bye, for now.'
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
print('')
time.sleep(1.5)
words = '\nDAVE:'
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
words = "\nHi there " + name + ", here's your office, ignore the smell, it use to be the room for our LAN parties."
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(1)
words = "\nSorry, I'm Dave by the way, the lead programmer here at HAVEN-O-CLUE Studio."
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(1)
words = "\n\nHere's your first decision, " + name + ". Remember, Dave will share his first impressions with his co-workers."
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
words = "\nA: What's a LAN party?\nB: When did I ask?\nC: Hi Dave! I'm so excited to be working with you!\nD: Meh, okay.\n\nPlease enter a letter.\n"
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

    
Achoice=input()
if Achoice.lower() == "a":
    popularity = popularity - 10
    words = "Well, that was stupid. You've made the wrong first impression, Dave is now suspicious of you. Your popularity is now " + str(popularity)+ "..."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
elif Achoice.lower() == "b":
    popularity = popularity - 10
    words = "Well, that was stupid. You've made the wrong first impression, Dave now thinks you're an ass. Your popularity is now " + str(popularity)+ "..."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    
time.sleep(1)
words = "\n\nDAVE:\nJeez, alright then, see yah, " + name + "."
for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    
time.sleep(1)
elif Achoice.lower() == "c":
    popularity = popularity + 10
    words = "Well done, new recruit. You've made the right first impression, Dave really likes you. Your popularity is now " + str(popularity)+ "..."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    
time.sleep(1)
    words = "\n\nDAVE:\nI'm excited to be working with you too, " + name + "."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    time.sleep(1)
elif Achoice.lower() == "d":
    popularity = popularity - 10
    words = "Well, that was stupid. You've made the wrong first impression, Dave now thinks you're lazy. Your popularity is now " + str(popularity)+ "..."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    Achoice=input()

else:
    words = "You blithering idiot. " + name + ", you broke the entire bloody game. Get outta my sight."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    
time.sleep(1)


words = "\n\nYou're in your office and notice that you don't have a computer. Choose a computer you think is suitable considering the budget."
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(1)
words = "\nA: 2002 Toshiba Tower ($69) - 12 power points\nB: 2015 MacBook Air ($399) - 34 power points\nC: 2018 HP Powerwave ($799) - 56 power points\nD: 2021 Alienware Hypervision ($1599) - 89 power points\n\nPlease enter a letter.\n"
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(1)
Bchoice=input()
if Bchoice.lower() == "a":
    budget = budget - 69
    pclifespan = 12
    words = "You've ordered your computer, your budget is now $" + str(budget)+ "..."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    
elif Bchoice.lower() == "b":
    budget = budget - 399
    pclifespan = 34
    words = "You've ordered your computer, your budget is now $" + str(budget)+ "..."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    
elif Bchoice.lower() == "c":
    budget = budget - 799
    pclifespan = 56
    words = "You've ordered your computer, your budget is now $" + str(budget)+ "..."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

elif Bchoice.lower() == "d":
    budget = budget - 1599
    pclifespan = 89
    words = "You've ordered your computer, your budget is now $" + str(budget)+ "..."
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

words = "\n\nCool! Your PC arrived. You plug it in and set it up. What would you like to do with it first?"
for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

words = "\nA: Send a passive-agressive to Dave (1 power point)\nB: Watch YouTube videos of cats (5 power points)\nC: Scavange Facebook for pictures of Minions (3 power point)\nD: Create a detailed write up of your project ideas (2 power point)"
for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
        
