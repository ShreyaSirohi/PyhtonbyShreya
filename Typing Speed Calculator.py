from timeit import default_timer as timer

words = 'the quick brown fox jumps over the lazy fat dog'
print("This is what you have to type:", "'", words, "'")
ask = input("When ready to start press,'y':")

if ask == 'y':
    start = timer()
    test = input('start typing:')

sure = input("When ready to submit, press 's'':")

a = words.split()
b = test.split()

if sure == 's':
    if words == test:
        end = timer()
        print('Seconds', end - start)

    else:
        end = timer()
        print('You have entered the wrong word!!!')
        print('Seconds', end - start)


def calculate(a, b):
    x = a / b
    y = x * 60
    print('Words per minute:', y)


calculate(len(b), end - start)

correct = 0
wrong = 0
z = 0
while z <= len(a) - 1:
    if a[z] == b[z]:
        correct += 1
    else:
        wrong += 1
    z += 1

print('Number of correct words:', correct)
print('Number of wrong words:', wrong)

accuracy = correct / len(b) * 100
print('Your accuracy:', accuracy, '%')
