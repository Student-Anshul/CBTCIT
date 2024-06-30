from getpass import getpass

print("\n==== Mastermind Game ====\n")
print("Enter a number of length 5 between(0 to 9):-")
attempts1 = 0
attempts2 = 0
Player1 = getpass("Player1 Enter a number: ")
if(len(Player1)<5 or len(Player1)>5):
    print("Please enter a number of length 5.")
else:
    p1 = list(Player1)
    
    while(True):
    
        Guess = input("Guess a number: ")
        a1 = set(Player1)==set(Guess)
        if(len(Guess)==0 or len(Guess)>5):
            print("Please enter a number of maximum length 5.")
        else:
            n1 = list(Guess)
            attempts1+=1
            
            if(attempts1==5):
                hint = input("You want to take hints(Y/N): ").upper()
                if(hint =='Y'):
                    print(f"The number is {p1[0]}{p1[1]}***")
            elif(Guess != Player1):
                revP = p1[::-1]
                if(a1 == False):
                    for i in revP:
                        for j in n1:
                            if(i==j):
                                print(f"{j} is in the number")
                if(a1):
                    print("You guess the numbers right.Now arrange them in a correct order.")
            else:
                if(attempts1==10):
                    hint = 'N'
                    print("You want to take hints(Y/N)")
                    if(hint =='Y'):
                        print(f"1st and 2nd position numbers are {p1[0]} and {p1[1]}")
                elif(attempts1 == 1):
                    print("Congratulation Player1 wins and crowned as Mastermind")
                    break
                else:
                    print(f"Player2's attempts are {attempts1}")
                break

if(attempts1 > 1):
    Player2 = getpass("Now Player2 Enter a number: ")
    if(len(Player2)<5 or len(Player2)>5 or Player2==' '):
        print("Please enter a number of length 5.")
    else:
        p2 = list(Player2)

        while(True):
            
            Guess = input("Guess a number: ")
            a2 = set(Player2)==set(Guess)
            if(len(Guess)==0 or len(Guess)>5):
                print("Please enter a number of maximum length 5.")
            else:
                n2 = list(Guess)
                attempts2+=1
                
                
                if(attempts2==5):
                    hint = input("You want to take hints(Y/N): ").upper()
                    if(hint =='Y'):
                        print(f"The number is {p2[0]}{p2[1]}***")
                elif(Guess != Player2):
                    revP2 = p2[::-1]
                    if(a2 == False):
                        for i in revP2:
                            for j in n2:
                                if(i==j):
                                    print(f"{j} is in the number")
                    elif(a2):
                        print("You guess the numbers right.Now arrange them in a correct order.")
                else:
                    if(attempts2 < attempts1):
                        print("Congratulation Player2 wins and crowned as Mastermind")
                        print(f"And Your attempts are {attempts1} and {attempts2}")
                    elif(attempts1==attempts2):
                        print("Its a draw!")
                    else:
                        print(f"Player1's attempts are {attempts1}")
                        print("Congratulation Player1 wins and crowned as Mastermind")
                    break