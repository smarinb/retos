"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */

"""
def reverse_word(word:str):
    new_word=[]
    cont = len(word)-1
    while cont >= 0:
        new_word.append(word[cont])
        cont-=1
        
    
    print(new_word)

reverse_word("Hola mundo")


