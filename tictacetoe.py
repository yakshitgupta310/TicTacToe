print ("Welcome to game of Tic Tac Toe !!!!")

def board_print() :
    print("     |     |     ")
    print("  "+board[1]+"  |  "+board[2] +"  |  "+board[3]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[4]+"  |  "+board[5] +"  |  "+board[6]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[7]+"  |  "+board[8] +"  |  "+board[9]+"  ")
    print("     |     |     ")

board=[0," "," "," "," "," "," "," "," "," "]

def player_input():

    y=input("Player 1 -what do you want to choose X or O ")
    if y.lower() == "x" :
        marker_1="X"
        marker_2="O"
        recall(marker_1,marker_2)     
    elif y.lower()=="o":
        marker_1="O"
        marker_2="X"
        recall(marker_1,marker_2)        
    else :
        print("wrong choice try again")
        player_input()



def player_1(marker_1,marker_2) :
    print("player 1 turn .....")
    choice=int(input("Enter the position = "))
    if board[choice] == " " :
        board[choice]=marker_1
        board_print()
        check(marker_1,marker_2)
    else :
        print("choosen position already filled")
        player_1(marker_1,marker_2)
    
 

def player_2(marker_1,marker_2) :
    a=" "
    if a in board:
        print("player 2 turn .....")
        choice=int(input("Enter the position = "))
        if  board[choice] == " " :
            board[choice] = marker_2
            board_print()
            check(marker_1,marker_2)
        else:
            print("choosen position already filled")
            player_1(marker_1,marker_2)


def recall(marker_1,marker_2):
    a=" "
    for i in range(1,10) :
        
        if a in board :
            player_1(marker_1,marker_2)
            player_2(marker_1,marker_2)


def check(marker_1,marker_2) :
    positions={"a":[1,2,3] , "b":[4,5,6] ,"c":[7,8,9] , "d":[1,5,9],"e":[3,5,7] ,"f":[1,4,7] ,"g":[2,5,8] ,"h":[3,6,9]}
    for value in positions.values():
            b=value           
            counter_1=0   
            counter_2=0
            for j in range (0,3) :
                f=b[j]
                if board[f] == marker_1 :
                    counter_1+=1
                    pass
                else :
                    break
            else:           
                for j in range(0,3) :
                    f=b[j]
                    if board[f] == marker_2 :
                       counter_2+=1
                       pass
                    else :
                       break
                if counter_2 == 3 :
                    print("player 2 wins")
                    
                    
                    play_again()
                elif counter_1==3 :
                    print("player 1 wins ")
                   
                   
                    play_again()
    b=" "
    if (b not in board) and (counter_1!=3 or counter_2!=3) :
            print("It's a Draw !!!!!")

   

def play_again():
    while True :
        
        num=input("would you like to play again? ")
        if  num.lower() == "y" :
            global board
            board=[0," "," "," "," "," "," "," "," "," "]   
            player_input()
        else:
            print("Thanks for playing")
            quit()

player_input()    