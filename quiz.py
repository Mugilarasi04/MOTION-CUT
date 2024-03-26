def quiz_game():
    print("WELCOME TO QUIZ GAME")
    score=0
    print("Question1: What is the capital of India?")
    print(""" a)Delhi          b)TamilNadu
              c)Kerala         d)Assam""")
    answer=input("enter answer:")
    if answer=="Delhi":
        score=score+10
        print("Correct answer")
    else:
        print("Oops! Incorrect answer")

    print("Question2:Who is the Indian Cricket team captain?")
    print(""" a)KL Rahul     b)Rohit Sharma
              c)Virat Kohli  d)Bumrah""")
    answer=input("enter answer:")
    if answer=="Rohit Sharma":
        score=score+10 
        print("Correct Answer")
    else:
        print("Oops! Incorrect Answer")
    print("Question3:What is the National Bird of India?")
    print(""" a)Peacock  b)Eagle
              c)Parrot   d)Penguin""")
    answer=input("Enter answer")
    if answer=="Peacock":
        score=score+10
        print("Correct answer")

    else:
        print("Oops!Incorrect Answer")

    print("Thankyou for participating")     
    print("Your score is ",score)
    exit()
 
quiz_game()


