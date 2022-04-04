import os,sys,random
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import logging
import re
import collections
from datetime import datetime

logging.basicConfig(filename='GamePlay.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)
todayDate=datetime.today().strftime("%m/%d/%Y, %H:%M:%S")
logger.info('Your Gameplay for '+todayDate)

staticals_list=[]
class WordleGame():
    def __init__(self):
        guessed_correctly,num_of_guesses=self.logicCode()
        #Display end of game message
        if guessed_correctly:
            print("Congratulations You have guesses Correct Word:-",guessed_correctly)
        else:
            print("You have used guesses:-", num_of_guesses)
            print("Game Over Better luck Next Time...")
        total_game_played=1
        while True:        
            ROOT = tk.Tk()
            ROOT.withdraw()
            playAgain=messagebox.askquestion("Confirm","Do You Want To Play Again?")  
            messagebox_info=["No of Game Played: "+str(total_game_played),"Your Staticals of Game","1st Attempt: "+str(staticals_list[0]),"2nd Attempt: "+str(staticals_list[1]),"3rd Attempt: "+str(staticals_list[2]),"4th Attempt: "+str(staticals_list[3]),"5th Attempt: "+str(staticals_list[4]),"6th Attempt: "+str(staticals_list[5])]
            staticals_list.pop(0)
            staticals_list.pop(0)
            staticals_list.pop(0)
            staticals_list.pop(0)
            staticals_list.pop(0)
            staticals_list.pop(0)
            logger.info(messagebox_info)
            if playAgain == 'yes':
                total_game_played+=1
                messagebox.showinfo("Game Staticals","\n".join(messagebox_info))
                self.logicCode()
            elif playAgain =='no':
                print("Goodbye")
                ROOT = tk.Tk()
                ROOT.withdraw()      
                messagebox.showinfo("Game Staticals","\n".join(messagebox_info))  
                break
            else:
                print("Goodbye")

    def word_fetch(self):
        try:
            a = open("demo.txt", "w")
            f = open("words.txt", "r")
            for x in f:
                if(len(x)==6):
                    a.write(x)
        except IOError:
            print("File not accessible")
        a.close()
        f.close()


    def processGuess(self,theAnswer, theGuess):
        position=0
        clue=""
        hint=""
        pos=""
        distribution=0
        for letter in theGuess:
            if letter == theAnswer[position]:
                hint += letter + ''
                pos=str(position) +','
                clue += "G" #G represents True Letter on Complete position
                distribution+=20
            elif letter in theAnswer:
                clue += "Y" #Y represents True Letter on Different position
                distribution+=10
            else:
                clue += "_" #_ represents False Letter 
            position += 1
        self.find_similar_words(hint,clue,pos,theAnswer)
        staticals_list.append(distribution)
        print(staticals_list)
        print(clue)
        logger.info('Your clue:-'+ clue)
        logger.info('Answer:-'+ theAnswer)
        logger.info('Your Guess:-'+ theGuess)
        logger.info('Your guessing percentage:-'+str(distribution))
        return clue == "GGGGG" #True if correct,False otherwie

    def verifyGuess(self,theGuess):
        if(len(theGuess) > 5 ):
            return theGuess[:5].strip()
        else:
            return theGuess

    def find_similar_words(self,hint,clue,pos,theAnswer):
        array_hintt=[]
        array_hint=hint.split()
        array_pos=pos.split(",")
        for i in hint:
            array_hintt.append(i)
        linked_list = collections.deque()
        line_count=0
        if(hint!=""):
            print(len(hint))
            wordList=open("demo.txt", "r+")
            lines = wordList.read().splitlines()
            for line in lines:
                for i in array_pos:
                    if (line[0] == theAnswer[0]) and (line[4] == theAnswer[4]):
                        linked_list.append(line)
                    elif(hint in line):
                        linked_list.append(line)
                        
            print(linked_list)
        else:
            wordList=open("demo.txt", "r+")
            for i in range(50):
                line = wordList.read().splitlines()
                linked_list.append(line)
            print(linked_list)
            
            
    
    def removeWord(self,answer):
        #Code for removing word which is already selected To avoid repeated word in Gameplay.
        wordList=open("demo.txt", "r+")
        lines = wordList.readlines()
        wordList.truncate(0)
        for line in lines:
            if line.strip() != answer:
                wordList.write(line)
            
        wordList.close()

    def giveHint(self,answer):
        first_letter=answer[0]
        last_letter=answer[4]
        print('First Letter is :-'+first_letter)
        print('Last Letter is :-' +last_letter)
        
    def logicCode(self):
        #words=[]
        p=os.path.getsize("demo.txt")
        if(p==0):
            self.word_fetch()
            
        wordList=open("demo.txt", "r+")  
        words = wordList.read().splitlines()
        wordList.close()
        answer=random.choice(words)
        self.giveHint(answer)
        #self.removeWord(answer)
        num_of_guesses=0
        guesses_correctly = False
       
        print("G=Letter is True, Y=True Letter In wrong Spot and _= Wrong Letter")
        while num_of_guesses < 6 and not guesses_correctly:
            #get input from user
            ROOT = tk.Tk()
            ROOT.withdraw()
            # the input dialog         
            guess = simpledialog.askstring(title="Input Box",prompt="Enter five character:")
            theGuess=self.verifyGuess(guess)
            #guess = input("Enter five character:")
            print("You have guess",theGuess)
            num_of_guesses += 1
            #process guess
            guessed_correctly = self.processGuess(answer, theGuess)      
        return guessed_correctly,num_of_guesses

    def __str__ (self):
        return 'Good Bye! You have Quit Game.'
    
#main Function of Program
if __name__=='__main__':
    game=WordleGame()
    print(game.__str__())
    
