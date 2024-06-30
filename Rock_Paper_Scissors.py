import random

Methods = {'R':0,'P':1,'S':2,}
YesNo = 'Y'

while(YesNo=='Y'):
    try:
        Computer = random.randint(0,2)
        Player = input("Select your choice between Rock(R),Paper(P),Scissor(S): ").upper()
        PlayerVal = Methods[Player]
        
        if((Computer==0) and (PlayerVal==1)):
            print("Its Paper You Wins!")
        elif((Computer==1) and (PlayerVal==2)):
            print("Its Scissor You Wins!")
        elif((Computer==2) and (PlayerVal==0)):
            print("Its Rock You Wins!")
        elif((Computer==1) and (PlayerVal==0)):
            print("Its Rock You Loose!")
        elif((Computer==2) and (PlayerVal==1)):
            print("Its Paper You Loose!")
        elif((Computer==0) and (PlayerVal==2)):
            print("Its Scissor You Loose!")
        else:
            print("Draw")
        YesNo = input("Are you intent on continue the game(Y/N): ").upper()
    except Exception as e:
        print(f"Error... {e}")
        print("Please try again")