#!/usr/bin/python3
import random
a = random.randint(1,50)
b = str (a)[-1]
c = int(b)
if c > 5:
    #    print("The last digit of ", a, "is", b)
    print(f"last digit of {a} is greater than 5 ")
elif c == 0:
    print(f"The last digit of {a} is equal to 0")
else:
    print(f"The last digit of {a} is less than 6 and not 0")