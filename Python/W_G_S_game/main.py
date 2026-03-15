#   Water, Gun and Snake Game
'''
0 = Water 
1 = Snake 
-1 = gun 
'''
import random 

Com_choice = random.choice([-1, 0, 1])
your_choice = input("Enter s/w/g :")
Dict = {
    "s" : 1,
    "w" : 0,
    "g" : -1,
}
Reverse_Dict = {1 : "snake", 0 : "water", -1 : "gun"}
if your_choice not in Dict:
    print("Invalid Input")
    exit()

your = Dict[your_choice]
com = Com_choice

print("You choose", Reverse_Dict[your])
print("computer choose", Reverse_Dict[com])


#conditions 
if your == com:
    print("Draw!")
elif your == 1 and com == 0: #1
    print("You Win!")
elif your == 0 and com == 1: #-1
    print("You lose com wins!")
elif your == -1 and com == 1: # -2 
    print("You win!")
elif your == 1 and com == -1: # 2 
    print("you lose and com wins")
elif your == 0 and com == -1: # 1
    print("You win!")
elif your == -1 and com == 0: # -1
    print("You lose and com wins!")

