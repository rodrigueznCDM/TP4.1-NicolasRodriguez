"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Exercice POO #4
"""
from random import randint

print("TP4.1 - POO #4\n")


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = randint(1, 10) + randint(1, 10)
        self.attack = randint(1, 6)
        self.defense = randint(1, 6)

    def attack_action(self):
        return randint(1, 6) + self.attack

    def receiving_damage(self, damage):
        self.health -= damage - self.defense

    def alive(self):
        return self.health > 0


character = Hero(input("\nQuel est le nom de votre personnage?:\n\n"))
