#!/usr/bin/python3
while True:
    print('Enter a number')
    a = int(input())
    b = str (a)[-1]
    c = int(b)
    if c > 5:
    #    print("The last digit of ", a, "is", b)
        print(f"last digit of {a} is greatr than 5 ")
    elif c == 0:
        print(f"The last digit of {a} is equal to 0")
    else:
        print(f"The last digit of {a} is less than 6 and not 0")