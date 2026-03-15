# Water, Gun and Snake Game
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

#condition 

if your == com:
    print('Draw')
elif your - com == 1 or your - com == -2:
    print("you win!")
else:
    print("you lose computer wins")
