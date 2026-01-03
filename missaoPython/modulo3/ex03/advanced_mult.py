#!/usr/bin/env python3

l = 0
while l < 11:
    print("Table of :",l, end=" ")
    c = 0
    while c < 11:
        print(l * c, end=" ")
        c = c + 1
    l = l + 1
    print()
