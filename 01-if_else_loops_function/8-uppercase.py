#!/usr/bin/python3
def uppercase(str):
    if ord (str)  >=97 and ord (str) <=122:
        k = ord(str) -32
        return chr(k)
    else :
        return str
print(uppercase ('a'))

