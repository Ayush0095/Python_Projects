import random 

print('\n\n___________________________________Welcome to Game of Dice_______________________________\n')
NAME = input('____________________________________Enter your name_______________________________: ')
print(f"\nHello! {NAME} Let's Start !!..")
f = 'Y'
dr = []
while f == 'Y' or f == 'y':
    print('\n1. Roll\n2. Exit')
    b = int(input('\nEnter Your Choice: '))
    clt= random.choice([1,2,3,4,5,6])
    rt= random.choice([1,2,3,4,5,6])
    if b == 1:
        print('\nNumber on the dices are: ',clt,rt)
        dr.append([clt,rt])
    elif b == 2:
        print('\nTotal outcomes: ',dr)
        print('\n\t\tThank You')
    else:
        print('\nEnter valid choice')
        b = int(input('\n_____________Enter Your Choice: '))
    f = input("\n______________Do you want to continue(Y/N): ")
else:
    print('\nTotal outcomes: ',dr)
    print('\n\t\t________Thank You for Playing_______')