### Challenge 3 ###

"""

/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */


"""



"""def fibonacci(num):
        if num == 0:
                return 0
        elif num == 1:
                return 1
        else:
                return fibonacci(num - 1) + fibonacci(num - 2)
        

for i in range(50):
        print(fibonacci(i))


"""

def fibonacci():
    prev = 0
    next = 1

    for i in range(0,50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()