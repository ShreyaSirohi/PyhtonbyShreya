from random import choice

wordlist = ['python', 'computer', 'rainbow', 'money', 'molecule', 'geometry']
word = choice(wordlist)
turns = len(word)*2
guesses = []

for j in word:
    print('_')

while turns >= 0:
    correct = 0
    ask = input("Guess the alphabet ")
    guesses.append(ask)

    for i in word:
        if i in guesses:
            print(i)
            correct += 1

        elif i not in guesses:
            print("_")

    if correct == len(word):
        print(f"You Win!!! \nthe Word is '{word}'")
        break
    elif turns == 0:
        print(f"You Lose... :( \nthe Word is '{word}'")

    if ask not in word:
        print('Wrong!', 'You have', turns, 'turns left.')
        if turns == 0:
            print('Wrong... no turn left')
    else:
        print(turns, 'turns left')

    turns -= 1
