#!/usr/bin/python3
def uppercase(str):

    result = ""
    for i in str:
        if ord (i)  >=97 and ord (i) <=122:
            k = ord(i) -32
            result += chr(k)
        else:
            result += i
    return result
        
print(uppercase ('Oll'))

