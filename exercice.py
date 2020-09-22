#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste = []
    for caractere in prefixes:
        liste.append(caractere+suffixe)

    return liste


def prime_integer_summation() -> int:
    sum = 0
    for x in range(2,101): # x est le nombre a tester pour savoir si il est premier
        for y in range(2,x+1): # y est le nombre avec lequel on fait le test de primalite
            if y == x: # x a passe tous les tests de primalite, il est premier
                sum += x
            if x%y == 0: # x n'est pas premier
                break
    return sum


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
