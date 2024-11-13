"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Exercice POO #5
"""
from random import randint
from dataclasses import dataclass

print("TP4.1 - POO #5\n")


# Pour calculer les stats d'un personnage dans D&D, on fait la somme de quatre d6 à laquelle on soustrait  la valeur du
# d6 le plus petit.
def stat_calculation():
    first_d6 = randint(1, 6)
    second_d6 = randint(1, 6)
    third_d6 = randint(1, 6)
    fourth_d6 = randint(1, 6)

    smallest = min(first_d6, second_d6, third_d6, fourth_d6)
    return first_d6 + second_d6 + third_d6 + fourth_d6 - smallest


# Les stats dans D&D ont ce qu'on appelle des modifiers. Ceux-ci sont utilisés pour beaucoup de choses dans le jeux.
@dataclass
class PlayerStats:
    strength: int = stat_calculation()
    dexterity: int = stat_calculation()
    constitution: int = stat_calculation()
    intelligence: int = stat_calculation()
    wisdom: int = stat_calculation()
    charisma: int = stat_calculation()

    strength_modifier: int = (strength - 10) // 2
    dexterity_modifier: int = (dexterity - 10) // 2
    constitution_modifier: int = (constitution - 10) // 2
    intelligence_modifier: int = (intelligence - 10) // 2
    wisdom_modifier: int = (wisdom - 10) // 2
    charisma_modifier: int = (charisma - 10) // 2
