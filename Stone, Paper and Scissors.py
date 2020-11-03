import random

# rules are:
# stone vs paper - paper wins
# paper vs scissors - scissors win
# scissors vs stone - stone wins

print("This is 'Stone, Paper and Scissors'")

gameobj = ['Stone', 'Paper', 'Scissors']
name = input('enter your name:')

print(f'Ok {name}...let us start...\n')

playerpoints = 0
CPUpoints = 0
drawmatches = 0
round = 1

z = 1

while z <= 10:
    print(f'Round {round}')
    ask = input('Stone, Paper or Scissors...make your choice:')
    ran = random.choice(gameobj)

    print(f'{name}: {ask} \t\t\tCPU: {ran}')

    if ask == 'Stone':
        if ran == 'Stone':
            print('No one wins... :(')
            drawmatches += 1
        elif ran == 'Paper':
            CPUpoints += 1
            print('CPU wins!')
        elif ran == 'Scissors':
            playerpoints += 1
            print('You win!')

    if ask == 'Paper':
        if ran == 'Paper':
            print('No one wins... :(')
            drawmatches += 1
        elif ran == 'Scissors':
            CPUpoints += 1
            print('CPU wins!')
        elif ran == 'Stone':
            playerpoints += 1
            print('You win!')

    if ask == 'Scissors':
        if ran == 'Scissors':
            print('No one wins... :(')
            drawmatches += 1
        elif ran == 'Stone':
            CPUpoints += 1
            print('CPU wins!')
        elif ran == 'Paper':
            playerpoints += 1
            print('You win!')
    print('\n')
    round += 1
    z += 1

print(f"Your score: {playerpoints}, CPU's score: {CPUpoints}, Draw: {drawpoints}")

if playerpoints > CPUpoints:
    print(f'Congratulations {name}!!! You have won the match')
elif CPUpoints > playerpoints:
    print(f'Oh no {name}... You have lost the match')
elif playerpoints == CPUpoints:
    print(f'{name}, both you and CPU have scored the same points...this match is a tie')