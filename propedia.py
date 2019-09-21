number = input("Θα δοκιμάσουμε την προπαίδεια του; ")
for n in range(10):
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
