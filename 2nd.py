import random 

print('\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Welcome to Game of Rock Paper and Scissor!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-\n\n')

Q= 'Y'

while Q == 'Y' or Q == 'y':
    P = random.choice(['Rock','Paper','Scissor'])
    R = input('\nEnter your desired choice: ')
    if (P == 'Rock' and R == 'Scissor') or (P == 'Paper' and R == "Rock") or (P == 'Scissor' and R == 'Paper'):
        print('\n_______________________Computer Wins__________________ ')
    elif P == R:
        print("\n_______________________Nobody Wins________________________")
    else:
        print('\n_______________________The winner is you_____________________')
    Q= input("\n_______________________Do you want to continue____________________(Y/N): ")
