###  Challenge 01 ###

"""
Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""



def is_multiple_three(number):
    return number % 3 == 0

def is_multiple_five(number):
    return number % 5 == 0

def is_multiple_three_and_five(number):
    return is_multiple_three(number) and is_multiple_five(number)

def fizzbuzz():
    for i in range(1,101):
        if is_multiple_three_and_five(i):
            print(f"{i}: fizzbuzz")
        elif is_multiple_five(i):
            print(f"{i}: buzz")
        elif is_multiple_three(i):
            print(f"{i}: fizz")
        else:
            print(i)

fizzbuzz()

