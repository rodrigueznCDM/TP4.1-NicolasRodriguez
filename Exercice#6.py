"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Exercice POO #6
"""
from random import randint
from dataclasses import dataclass

print("TP4.1 - POO #6\n")


def stat_calculation():
    first_d6 = randint(1, 6)
    second_d6 = randint(1, 6)
    third_d6 = randint(1, 6)
    fourth_d6 = randint(1, 6)

    smallest = min(first_d6, second_d6, third_d6, fourth_d6)
    return first_d6 + second_d6 + third_d6 + fourth_d6 - smallest


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


# Pour simplifier, on donne une "Longsword", une "chainmail" et un "shield" au fighter (le joueur ne peux pas choisir)
class Fighter:
    def __init__(self, name):
        self.name = name
        self.stats = PlayerStats()
        self.hit_points = 10 + self.stats.constitution_modifier
        self.longsword = randint(1, 8)
        self.chain_mail = 16
        self.shield = 2

    def attack_action(self):
        return self.longsword + self.stats.strength_modifier + 2  # proficiency bonus

    def receiving_damage(self, enemy_attack_roll, damage):
        armour_class = self.chain_mail + self.shield

        if enemy_attack_roll >= armour_class:
            self.hit_points -= damage

        elif enemy_attack_roll < armour_class:
            # Aucun dégas
            pass

    def alive(self):
        return self.hit_points > 0


character = Fighter(input("\nQuel est le nom de votre personnage?:\n\n"))
