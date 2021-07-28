import random
while True:
    choices=['stone','paper','scissor']

    program_choice=random.choice(choices)

    player=None

    while player not in choices:
        player=input("stone,paper or scissor ? :").lower()

        if player==program_choice:
            print("computer: ",program_choice)
            print("player: ",player)
            print("game is tie!")

        elif player=='stone':
            if program_choice=='paper':
                print("computer: ",program_choice)
                print("player: ",player)
                print("You Lose!")

        if program_choice=='scissor':
                print("computer: ", program_choice)
                print("player: ", player)
                print("You Win!")

        elif player=='scissor':
            if program_choice=='paper':
                print("computer: ", program_choice)
                print("player: ", player)
                print("You Win!")
            if program_choice=='stone':
                print("computer: ", program_choice)
                print("player: ", player)
                print("You Lose!")

        elif player=='paper':
            if program_choice=='scissor':
                print("computer: ", program_choice)
                print("player: ", player)
                print("You Lose!")

            if program_choice=='stone':
                print("computer: ", program_choice)
                print("player: ", player)
                print("You win!")


    play_more=input("Enter yes to play or no to quit: ?").lower()

    if play_more!="yes":
         break


print("Bye! catch you later !")