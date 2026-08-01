#!/usr/bin/python3
while True:
    a = 10
    b = 10
    for i in range (a):
        for j in range (b):
            if i < j:
                print(f"{i}{j}")
    break