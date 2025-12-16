#!/usr/bin/env python3

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

res = n1 * n2

if res == 0:
    print("ZERO")
elif res > 0:
    print("POSITIVO")
else:
    print("NEGATIVO")

print(res)
