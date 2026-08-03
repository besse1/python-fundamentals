#!/usr/bin/python3
import random
a = random.randint(-100, 100)
if a < 0 :
    print(f"{a} is negative")
elif a == 0:
    print(f"{a} is zero")
else :
    print (f" {a} is positive")
