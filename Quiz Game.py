print("Welcome to Quiz")
print("Test your knowledge with us !!")
print()

answer = input("would you like to play: ").lower()

if answer != "yes":
    print("OKAY ! Have a good day  ")
    quit()
else:
    print("Lets start !")
    score = 0

question1= input("What is the full form of CPU?  ").lower()

if question1 == "control processing unit":
    print("Correct Answer ")
    score +=1
else:
    print("Your Answer is wrong")

question2 = input("What is the full form of GPU?  ").lower()

if question2 == "Graphic processing unit":
    print("Correct Answer ")
    score += 1
else:
    print("Your Answer is wrong")
    
question3= input("What is the full form of RAM?  ").lower()

if question3 == "Random Access Memory":
    print("Correct Answer ")
    score +=1
else:
    print("Your Answer is wrong")
    
question4= input("What is the extention of python?  ").lower()

if question4 == ".py":
    print("Correct Answer ")
    score +=1
else:
    print("Your Answer is wrong")
    
    
question5= input("What is int in python  ").lower()

if question5 == "integer":
    print("Correct Answer ")
    score +=1
else:
    print("Your Answer is wrong")
    
print("Your quiz is completed ")
check = input("Want to see the result ").lower()

if check != "yes":
    quit()
else:
    print("Your total score",score, "Out of 5")
    print("Your percentage is ", (score/5)*100,"%")



