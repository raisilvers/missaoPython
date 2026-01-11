#!/usr/bin/env python3

n = input("Enter a number: ")

try:
    numero_float = float(n)

    if numero_float.is_integer():
        print("Esse numero é inteiro!")
    else:
        print("Esse numero é decimal")
except:
    print("Numero invalido")
