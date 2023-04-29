import random

def fun(D):
    Z= random.randint(1, 10)
    for i in range(5):
        ch = int(input("\t\tNumber between 1 and 10: "))
        if ch != Z:
            print("\n\t\t\tWrong!!!!! Try again........\n")
            D -= 50
        else:
            print("\n\t\tCongratulations, you guessed.........\n")
            D += 100
            break
    else:
        print("\nGame over. Answer was", Z)
        D = 0
    return D 

print('\n\n-------------Welcome to Guess The Number---------------\n\n')
print('Rule of the game: \n\t You have five chances.\n\n')
D = 200
D = fun(D)
print("Final score:", D)