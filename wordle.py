def processGuess(theAnswer, theGuess):
    position=0
    clue=""
    for letter in theGuess:
        if letter == theAnswer[position]:
            clue += "G" #G represents True Letter on Complete position
        elif letter in theAnswer:
            clue += "Y" #Y represents True Letter on Different position
        else:
            clue += "_" #_ represents False Letter 
        position += 1
    print(clue)
    return clue == "GGGGG" #True if correct,False otherwie

answer="SONAR"

num_of_guesses=0
guesses_correctly = False
print("G=Letter is True, Y=True Letter In wrong Spot and _= Wrong Letter")
while num_of_guesses < 6 and not guesses_correctly:
    #get input from user
    guess = input("Enter five character:")
    print("You have guess",guess)
    num_of_guesses += 1

    #process guess
    guessed_correctly = processGuess(answer, guess)

#Display end of game message
if guessed_correctly:
    print("Congratulations You have guesses Correct Word:-",answer)
else:
    print("You have used guesses:-", num_of_guesses)
    print("Game Over Better luck Next Time...")

            
