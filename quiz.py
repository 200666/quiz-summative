#VARIABLES
global score
#I made the score the global variable so it could be used in both the endings
score=0
choiceone= 0
choicetwo= 0
choicethree = 0
choicefour = 0
choicefive = 0
choicesix = 0
choiceseven = 0
choiceeight= 0
choicenine= 0
choiceten = 0
choiceeleven = 0
choicetwelve = 0
choicethirteen = 0
choicefourteen = 0
choicefifteen = 0
#there is a varaible for each question
#FUNCTIONS
def end ():
    choiceone= 0
    print("WRONG!! you lost!! your score is", score, "/15.") #displays score
# I tried to make the game go back to the begingn by using funcitons, but this didn't work with the rest so i cut it
def final ():
    print("you wonnn!! good job!! your score is", score, "/15") # displays score when the user won. should be 15/15

#MAIN CODE
choicetwo = input(""""Welcome to the Quiz!
To play you just read throught the questions and choose the best awnser!
Do you wish to start? type 2 for start and 3 for no""")
#this is the beginging of the actual quiz, so it is an input statement
print(choicetwo)
if choicetwo == "2" :
    text_file= open ("questions.text") #defines a variable to open the text file
    lines = text_file.readlines() #uses the variable above to define a new variable to choose specific lines in the text file
    print(lines[0:4]) # prints lines in a specific range. repeated to show each question
    while choicethree != 1 or 2 or 3: # I used a while loop because this is a method i am used to
        score = 0
        choicethree = input("awnser, 1 2 or 3")
        if choicethree == "1":
            print("correct! i am a pretty great mc, arnet i ahhahah NEXT QUESTION!!")
            score = score+ 1 # adds one point to the score
            print(lines[5:9])
            while choicefour != 4 or 5 or 6:
                choicefour = input("awnser, 4 5 or 6")
                if choicefour == "6":
                    print("correct! we have all been through that phase!! lolll randooooom ahhahah NEXT QUESTION!!")
                    score = score+ 1
                    print(lines[10:15])
                    while choicefour != 7 or 8 or 9:
                        choicefour = input("awnser, 7 8 or 9")
                        if choicefour == "8":
                            print("correct! other popular languages include french, italian, and romnash NEXT QUESTION!!")
                            score = score+ 1
                            print(lines[14:19])
                            while choicefive != 10 or 11 or 12:
                                choicefive = input("awnser, 10 or 11 or 12")
                                if choicefive == "10":
                                    print("correct! NEXT QUESTION!!")
                                    score = score+ 1
                                    print(lines[20:25])
                                    while choicefive !=  1 or 2 or 3 :
                                        choicefive = input("awnser")
                                        if choicefive == "1":
                                            print("correct! you sure do know colors NEXT QUESTION!!")
                                            score = score+ 1
                                            print(lines[25:30])
                                            while choicesix !=  1 or 2 or 3 :
                                                choicesix = input("awnser")
                                                if choicesix == "3":
                                                    print("correct!  NEXT QUESTION!!")
                                                    score = score+ 1
                                                    print(lines[30:35])
                                                    while choiceseven !=  1 or 2 or 3 :
                                                        choiceseven = input("awnser")
                                                        if choiceseven== "3" :
                                                            print("correct!  NEXT QUESTION!!")
                                                            score = score+ 1
                                                            print(lines[35:40])
                                                            while choiceeight !=  1 or 2 or 3 :
                                                                choiceeight = input("awnser")
                                                                if choiceeight == "1":
                                                                    print("correct!  NEXT QUESTION!!")
                                                                    score = score+ 1
                                                                    print(lines[40:45])
                                                                    while choicenine !=  1 or 2 or 3 :
                                                                        choicenine = input("awnser")
                                                                        if choicenine == "1" :
                                                                            print("correct!  NEXT QUESTION!!")
                                                                            score = score+ 1
                                                                            print(lines[45:49])
                                                                        while choiceten !=  1 or 2 or 3 :
                                                                            choiceten = input("awnser")
                                                                            if choiceten == "1" :
                                                                                print("correct!  NEXT QUESTION!!")
                                                                                score = score+ 1
                                                                                print(lines[50:54])
                                                                                while choiceeleven !=  1 or 2 or 3 :
                                                                                    choiceeleven = input("awnser")
                                                                                    if choiceeleven == "3" :
                                                                                        print("correct!  NEXT QUESTION!!")
                                                                                        score = score+ 1
                                                                                        print(lines[55:59])
                                                                                        while choicetwelve !=  1 or 2 or 3 :
                                                                                            choicetwelve = input("awnser")
                                                                                            if choicetwelve == "3":
                                                                                                print("correct!  NEXT QUESTION!!")
                                                                                                score = score+ 1
                                                                                                print(lines[60:64])
                                                                                                while choicethirteen !=  1 or 2 or 3 :
                                                                                                    choicethirteen = input("awnser")
                                                                                                    if choicethirteen == "2":
                                                                                                        print("correct!  NEXT QUESTION!!")
                                                                                                        score = score+ 1
                                                                                                        print(lines[65:69])
                                                                                                        while choicefourteen !=  1 or 2 or 3 :
                                                                                                            choicefourteen = input("awnser")
                                                                                                            if choicefourteen == "3" :
                                                                                                                print("correct!  NEXT QUESTION!!")
                                                                                                                score = score+ 1
                                                                                                                print(lines[70:75])
                                                                                                                while choicefifteen !=  1 or 2 or 3 :
                                                                                                                    choicefifteen = input("awnser")
                                                                                                                    if choicefifteen == "1":
                                                                                                                        score = score+1
                                                                                                                        final() # the last end funciton
                                                                                                                    else:
                                                                                                                        print("the awnser was")
                                                                                                                        print(lines[73]) # i used this to show the user what the correct awnser was
                                                                                                                        end() # the first end function
                                                                                                            else:
                                                                                                                print("the awnser was")
                                                                                                                print(lines[69])
                                                                                                                end()
                                                                                                    else:
                                                                                                        print("the awnser was")
                                                                                                        print(lines[52])
                                                                                                        end()
                                                                                            else:
                                                                                                print("the awnser was")
                                                                                                print(lines[58])
                                                                                                end()
                                                                                    else:
                                                                                        print("the awnser was")
                                                                                        print(lines[53])
                                                                                        end()
                                                                            else:
                                                                                print("the awnser was")
                                                                                print(lines[47])
                                                                                end()
                                                                        else:
                                                                            print("the awnser was")
                                                                            print(lines[42])
                                                                            end()
                                                                else:
                                                                    print("the awnser was")
                                                                    print(lines[37])
                                                                    end()
                                                        else:
                                                            print("the awnser was")
                                                            print(lines[33])
                                                            end()
                                                else:
                                                    print("the awnser was")
                                                    print(lines[28])
                                                    end()
                                        else:
                                            print("the awnser was")
                                            print(lines[21])
                                            end()
                                else:
                                    print("the awnser was")
                                    print(lines[16])
                                    end()
                        else:
                            print("the awnser was")
                            print(lines[13])
                            end()
                else:
                    print("the awnser was")
                    print(lines[8])
                    end()
        else:
            print("the awnser was")
            print(lines[1])
            end()
else:
    print("")
