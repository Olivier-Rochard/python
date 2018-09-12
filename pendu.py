import random

wordList=['logis','pizza','ronde','rouge','tarte']
word=random.choice(wordList)
guess='*****'

import turtle
turtle.pensize(5)
errors=0
def showStickman():
    if(errors==1):
        turtle.bk(100)
        turtle.fd(200)
    if(errors==2):
        turtle.bk(100)
        turtle.lt(90)
        turtle.fd(300)
    if(errors==3):
        turtle.rt(90)
        turtle.fd(150)
    if(errors==4):
        turtle.rt(90)
        turtle.fd(50)
    if(errors==5):
        turtle.dot(50)
    if(errors==6):
        turtle.fd(100)
        turtle.bk(75)
    if(errors==7):
        turtle.rt(45)
        turtle.fd(50)
        turtle.bk(50)
    if(errors==8):
        turtle.lt(90)
        turtle.fd(50)
        turtle.bk(50)
    if(errors==9):
        turtle.rt(45)
        turtle.fd(75)
        turtle.rt(45)
        turtle.fd(50)
        turtle.bk(50)
    if(errors==10):
        turtle.lt(90)
        turtle.fd(50)

while((guess!=word) and (errors<10)):
    print('Voici le mot à deviner : ', guess)
    letter=input('Devine une lettre ')
    hasLetter=False
    newguess=[]

    for n in range(5):
        if(letter==word[n]):
            newguess.append(letter)
            hasLetter=True
        else:
            newguess.append(guess[n])

    guess=''.join(newguess)

    if(hasLetter):
        print('C\'est exact ')
    else:
        print('Essaie encore ')
        errors=errors+1
        showStickman()
print('La réponse était ',word)
