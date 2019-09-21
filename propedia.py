import random

number = input("Θα δοκιμάσουμε την προπαίδεια του; ")
factors = list(range(10))
random.shuffle(factors)

for n in factors:
    wrong = True
    while wrong:
        question = f"{n} x {number} = "
        answer = input(question)
        if answer == "q": exit()
        if int(answer) == (n * int(number)):
            print('Μπράβο!')
            wrong = False
        else:
            print('Δοκίμασε ξανά')
