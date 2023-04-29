import random 
import string

print('\n\n_____________________________________Welcome to Strong Password Generator_________________________________\n')

A= string.ascii_uppercase
B = string.ascii_lowercase
c = string.digits
d = string.punctuation

W = ''
n = int(input('\n _______________________________________How many characters you want in password (8/12):__________________'))

if n == 8:
    A1 = random.choices(A,k=2)
    B1 = random.choices(B,k=2)
    c1 = random.choices(c,k=2)
    d1 = random.choices(d,k=2)
    Wl = A1+B1+c1+d1
    for i in Wl:
        W = W + i
elif n==12:
    A1 = random.choices(A,k=3)
    B1 = random.choices(B,k=3)
    c1 = random.choices(c,k=3)
    d1 = random.choices(d,k=3)
    Wl = A1+B1+c1+d1
    for i in Wl:
        W = W + i
else:
    print('______________________________Enter valid choice...')
    n = int(input('\n ________________________________How many characters you want in password (8/12): '))

print('\n\t\t ________________________________Generated password is: ',W)