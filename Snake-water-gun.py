import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, 0, -1])
youstr = input("Enter your choice : ")
youdict = {"s" : 1, "w" : -1, "g" : 0}
reversedict = {1 :"snake", 0 : "gun", -1 :"water"}
you = youdict[youstr]

print(f"Computer chose: {reversedict[computer]}")
print(f"You chose: {reversedict[you]}")

if computer == -1 and you == 1:
    print("Snake drinks water 🐍💧")
    print("You win....!")

elif computer == -1 and you == 0:
    print("Water drown gun💧🔫")
    print("You lose....!")

elif computer == -1 and you == -1:
    print("Both choose water💧")
    print("match draw....!")

elif computer == 1 and you == 1:
    print("Both chose Snake 🐍")
    print("match draw....!")

elif computer == 1 and you == 0:
    print("Gun shoots snake 🔫🐍")
    print("You win....!")

elif computer == 1 and you == -1:
    print("Snake drinks water 🐍💧")
    print("You lose....!")

elif computer == 0 and you == 1:
    print("Gun shoots snake 🔫🐍")
    print("You lose....!")

elif computer == 0 and you == -1:
    print("Water drowns gun 💧🔫")
    print("You win....!")

elif computer == 0 and you == 0:
    print("Both chose Gun 🔫")
    print("match draw....!")

else:
    print("Something wrong......!")