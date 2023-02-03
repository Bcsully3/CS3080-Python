'''
Homework 1 
Name: Brendan Sullivan
Date: 2/2/2022
Description of your program: This program asks the user 4 questions on order to give them access to the secret message. 
    The first 3 questions are math related, using random numbers and hard coded numbers. There are also a variety of 
    different math symbols and operations. Then, the last question asks how many digits have appeared, and they should 
    look veerrrry closely (hint). Then, if they get that right, the secret message is displayed
'''

from random import randint



complete = False
answer1 = 0
answer3 = 0
num1, num2, num12 = 0,0,0
while (complete == False):

    

    for i in range (0,4):
        ## MATH PROBLEMS
        
        ## MATH PROB 1
        if (i == 0) :
            print("HELLO!!    WELCOME TO MY GAME. IN ORDER TO GET THE SECRET MESSAGE AT THE END, YOU MUST ANSWER A SERIES OF QUEST1ONS")

            print("\nFirst, lets start with some math:")
            num1 = randint(100,200)                ## generate 2 random numbers to subtract
            num2 = randint(50,100)
            print("What is " + str(num1) + " - " + str(num2) + "?")
            answer1 = input()
            if (int(answer1) != num1 - num2):               ## test for wrong answer
                print("WRONG! YOU HAVE FAILED THE TEST\n\n\n")
                break
            else:
                print("Correct!")
                continue

        ## MATH PROB 2
        
        if (i == 1):
            num12 = randint(1,100)
            print("Is " + str(num12) + " an even number? Enter y or n")
            answer = input()
            if num12 % 2 == 0:    ## test for even or odd
                isEven = True
            else:
                isEven = False
            if ((answer == 'y') and (isEven == True)):      ## if they got it right, and it is even
                print("Correct!")
                continue
            elif ((answer == 'n') and (isEven == False)):          ## if they got it right, and it is odd
                print("Correct!")
                continue
            else:
                print("WRONG! YOU HAVE FAILED THE TEST\n\n\n")
                break
        

        ## MATH PROB 3
        if (i == 2):
            print("\nWhat is 12 + 3 * 4?")
            answer3 = input()
            if (answer3 != '24'):
                print("WRONG! YOU HAVE FAILED THE TEST\n\n\n")           ## Test for the right answer
                break
            else:
                print("Correct")
                continue


        ## LAST QUESTION
        if (i==3):
            print("\n\n\n\nTime for the last question. Congrats on making it this far......")
            print("How many digits have appeared on the screen for this game?")
            answer4 = input()
            totalDigits = len(answer3) + len(answer1) + len(str(num1)) +len(str(num2)) + len(str(num12)) + 5       ## add up the number of digits that have appeared
            
            if (int(answer4) == totalDigits):    ## if they are right, break from loop
                print("Correct!")
                complete = 'yes'
            else:
                print("WRONG! YOU HAVE FAILED THE TEST\n\n\n")
                break


print("\n\n\n\n---------------------------------------------\nCongrats!")        ## display secret message at the end of the loop
print("\nYou have passed the test")
print("\nYour secret message is :\nczggj ocdn dn ocz nzxmzo hznnvbz\n\n")
            

