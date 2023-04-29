import random
a= ['python', 'computer', 'programming', 'algorithm', 'coding']
w = random.choice(a)
card = '_' * len(w)
roll= 6
guess= []
hanng = [
    """
     _______
    |/      +
    |      
    |      
    |       
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      
    |       
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |       |
    |       |
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|
    |       |
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      / 
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      / \\
    |
    """
]
while roll > 0 and '_' in card:
    print(f'Word: {card}')
    print(f'Turns left: {roll}')
    print(f'Guessed letters: {", ".join(guess)}')
    print(hanng[6-roll])
    g = input('Guess a letter: ').lower()
    if not g.isalpha() or len(g) != 1:
        print('Invalid input! Please enter a single letter.')
        continue
    if g in guess:
        print(f'You already guessed {g}!')
        continue
    guess.append(g)
    if g in w:
        print(f'Correct! {g} is in the word.')
        card = ''.join([c if c == g or card[i] != '_' else '_' for i, c in enumerate(w)])
    else:
        print(f'Wrong! {g} is not in the word.')
        roll -= 1
if '_' not in card:
    print(f'Congratulations, you won! The word was {w}.')
else:
    print(f'Sorry, you lost! The word was {w}.')
    print(hanng[6])