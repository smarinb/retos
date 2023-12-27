### Chalange 2 ###
"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

"""

def is_anagram(word_one: str, word_two: str):
    if word_one.lower() == word_two.lower():
        return False
    else:
        """word_one_list = list(word_one.lower())
        word_two_list = list(word_two.lower())
        word_one_list.sort()
        word_two_list.sort()
        return word_one_list == word_two_list"""
        return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Escuchar","Churaces"))

