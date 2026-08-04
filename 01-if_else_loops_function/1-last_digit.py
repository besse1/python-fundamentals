#!/usr/bin/python3
import random
a = random.randint(-2048,2048)
b = abs(a) % 10
if a < 0:
    b = -b

if b > 5:
    #    print("The last digit of ", a, "is", b)
    print(f"The last digit of {a} is {b} and is greater than 5")
elif b == 0:
    print(f"The last digit of {a} is {b} and is equal to 0")
else:
    print(f"The last digit of {a} is {b} and is less than 6 and not 0")