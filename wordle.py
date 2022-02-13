import os,sys,random
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

staticals_list=[]
def processGuess(theAnswer, theGuess):
    position=0
    clue=""
    distribution=0
    for letter in theGuess:
        if letter == theAnswer[position]:
            clue += "G" #G represents True Letter on Complete position
            distribution+=20
        elif letter in theAnswer:
            clue += "Y" #Y represents True Letter on Different position
            distribution+=10
        else:
            clue += "_" #_ represents False Letter 
        position += 1
    print(clue)
    staticals_list.append(distribution)
    print(staticals_list)
    print(distribution)
    return clue == "GGGGG" #True if correct,False otherwie

def logicCode():
    wordList=["about","above","abuse","actor","acute","admit","adopt","adult","after","again","agent","agree","ahead","alarm","album","alert","alike","alive","allow","alone","along","alter","among","anger","Angle","angry","apart","apple","apply","arena","argue","arise","array","aside","asset","audio","audit","avoid","award","aware","badly","baker","bases","basic","basis","beach","began","begin","begun","being","below","bench","billy","birth","black","blame","blind","block","blood","board","boost","booth","bound","brain","brand","bread","break","breed","brief","bring","broad","broke","brown","build","built","buyer","cable","calif","carry","catch","cause","chain","chair","chart","chase","cheap","check","chest","chief","child","china","chose","civil","claim","class","clean","clear","click","clock","close","coach","coast","could","count","court","cover","craft","crash","cream","crime","cross","crowd","crown","curve","cycle","daily","dance","dated","dealt","death","debut","delay","depth","doing","doubt","dozen","draft","drama","drawn","dream","dress","drill","drink","drive","drove","dying","eager","early","earth","eight","elite","empty","enemy","enjoy","enter","entry","equal","error","event","every","exact","exist","extra","faith","false","fault","fiber","field","fifth","fifty","fight","final","first","fixed","flash","fleet","floor","fluid","focus","force","forth","forty","forum","found","frame","frank","fraud","fresh","front","fruit","fully","funny","giant","given","glass","globe","going","grace","grade","grand","grant","grass","great","green","gross","group","grown","guard","guess","guest","guide","happy","harry","heart","heavy","hence","henry","horse","hotel","house","human","ideal","image","index","inner","input","issue","japan","jimmy","joint","jones","judge","known","label","large","laser","later","laugh","layer","learn","lease","least","leave","legal","level","lewis","light","limit","links","lives","local","logic","loose","lower","lucky","lunch","lying","magic","major","maker","march","maria","match","maybe","mayor","meant","media","metal","might","minor","minus","mixed","model","money","month","moral","motor","mount","mouse","mouth","movie","music","needs","never","newly","night","noise","north","noted","novel","nurse","occur","ocean","offer","often","order","other","ought","paint","panel","paper","party","peace","peter","phase","phone","photo","piece","pilot","pitch","place","plain","plane","plant","plate","point","pound","power","press","price","pride","prime","print","prior","prize","proof","proud","prove","queen","quick","quiet","quite","radio","raise","range","rapid","ratio","reach","ready","refer","right","rival","river","robin","roger","roman","rough","round","route","royal","rural","scale","scene","scope","score","sense","serve","seven","shall","shape","share","sharp","sheet","shelf","shell","shift","shirt","shock","shoot","short","shown","sight","since","sixth","sixty","sized","skill","sleep","slide","small","smart","smile","smith","smoke","solid","solve","sorry","sound","south","space","spare","speak","speed","spend","spent","split","spoke","sport","staff","stage","stake","stand","start","state","steam","steel","stick","still","stock","stone","stood","store","storm","story","strip","stuck","study","stuff","style","sugar","suite","super","sweet","table","taken","taste","taxes","teach","teeth","terry","texas","thank","theft","their","theme","there","these","thick","thing","think","third","those","three","threw","throw","tight","times","tired","title","today","topic","total","touch","tough","tower","track","trade","train","treat","trend","trial","tried","tries","truck","truly","trust","truth","twice","under","undue","union","unity","until","upper","upset","urban","usage","usual","valid","value","video","virus","visit","vital","voice","waste","watch","water","wheel","where","which","while","white","whole","whose","woman","women","world","worry","worse","worst","worth","would","wound","write","wrong","wrote","yield","young","youth"]
    answer=random.choice(wordList)
    num_of_guesses=0
    guesses_correctly = False
    print("G=Letter is True, Y=True Letter In wrong Spot and _= Wrong Letter")
    while num_of_guesses < 6 and not guesses_correctly:
        #get input from user
        ROOT = tk.Tk()
        ROOT.withdraw()
        # the input dialog
        guess = simpledialog.askstring(title="Input Box",prompt="Enter five character:")

        #guess = input("Enter five character:")
        print("You have guess",guess)
        num_of_guesses += 1

        #process guess
        guessed_correctly = processGuess(answer, guess)      
    return guessed_correctly,num_of_guesses
#main Function of Program
if __name__=='__main__':
    guessed_correctly,num_of_guesses=logicCode()
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

    if playAgain == 'yes':
        total_game_played+=1
        messagebox.showinfo("Game Staticals","\n".join(messagebox_info))
        logicCode()
    elif playAgain =='no':
        print("Goodbye")
        ROOT = tk.Tk()
        ROOT.withdraw()      
        messagebox.showinfo("Game Staticals","\n".join(messagebox_info))  
        break
    else:
        print("Goodbye")
