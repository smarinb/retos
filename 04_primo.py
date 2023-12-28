"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

def es_primo(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2,number):
            return not number % i == 0
    


for i in range (1,101):
    print(f"{i}: {es_primo(i)}")