#!/usr/bin/python3
while True:
    for i in range (ord('a'),ord('z')+1):
        if i == ord('e') or i == ord('q'): continue
        print(chr(i), end='')
    break