player1 = input("Player 1, enter rock, paper or scissors: ").lower()
player2 = input("Play 2, enter rock, paper or scissors: ").lower()

if player1 == player2:
   print("Tie")
else: 
    if player1 == "rock":
            if player2 == "paper":
                    print("Player 2 wins")
            else: 
                print("Player 1 wins")
    elif player1 == "scissors":
               if player2 == "rock":
                print("Player 2 wins")
               else:
                    print("Player 1 wins")
    elif player1 == "paper":
                if player2 == "scissors":
                 print("Player 2 wins")
                else:
                    print("Player 1 wins")

    else:
        print("Invalid input from Player 1")
