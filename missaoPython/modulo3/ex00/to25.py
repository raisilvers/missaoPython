#!/usr/bin/env python3

n = int(input("Enter a number less than 25: "))

if n > 25:
    print("ERROR")
else:
    while n <= 25:
        print(n)
        n = n + 1
