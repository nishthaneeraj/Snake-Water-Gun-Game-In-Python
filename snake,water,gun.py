import random

chance = 1

human_point = 0
computer_point = 0

print("s for snake , w for water , g for gun ; you can use both uppercase or lowercase characters")

while (chance <= 10):

    lst=["s","w","g"]
    computer_choice=random.choice(lst)

   

    usr = input("Snake, Water & Gun : ")
    usr = usr.lower()

    if usr == computer_choice:
        print("Tie\nNobody get points")
       
    elif usr == "s" and computer_choice=="w":
        print("You Win!")
        human_point = human_point + 1
        print(f"You Choosed {usr} Computer Choosed {computer_choice} ")
        
    elif usr == "s" and computer_choice=="g":
        print("You Loose")
        computer_point = computer_point + 1
        print(f"You Choosed {usr} Computer Choosed {computer_choice} ")
       
    elif usr == "w" and computer_choice=="g":
        print("You Win!")
        human_point = human_point + 1
        print(f"You Choosed {usr} Computer Choosed {computer_choice} ")
        
    elif usr == "w" and computer_choice=="s":
        print("You Loose")
        computer_point = computer_point + 1
        print(f"You Choosed {usr} Computer Choosed {computer_choice} ")
        
    elif usr == "g" and computer_choice=="s":
        print("You Win!")
        human_point = human_point + 1
        print(f"You Choosed {usr} Computer Choosed {computer_choice} ")
       
    elif usr == "g" and computer_choice=="w":
        print("You Loose")
        computer_point = computer_point + 1
        print(f"You Choosed {usr} Computer Choosed {computer_choice} ")

    else:
        print("Invalid Input")
        continue

        if attempts>10:
            print("Game Over!")

    print("No. of guesses left: {}".format(10 - chance))
    chance = chance + 1

if computer_point < human_point:
    print("All Over You Win! And Computer Loose")
    print(f"Your score: {human_point} \nComputer's score: {computer_point}")

elif computer_point > human_point:
    print("All Over Computer Win! And You Loose")
    print(f"Your score: {human_point} \nComputer's score: {computer_point}")

else:
    print("It Was A Tie")

    print(10 - chance, "no. of guesses left")
    chance = chance + 1