"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Exercice POO #3
"""
from math import pi

print("TP4.1 - POO #3\n")


class Cercle:
    def __init__(self, radius):
        self.radius = radius
        self.circonference = self.calculate_circonferance()
        self.area = self.calculate_area()

    def calculate_circonferance(self):
        circonference = 2 * pi * self.radius
        return circonference

    def calculate_area(self):
        area = pi * self.radius ** 2
        return area

    def display_info(self):
        print(f"\nLes mesures de votre cercle sont:\n"
              f"\nCirconférance: {self.circonference}"
              f"\nAire: {self.area}")


radius_input = int(input("\nQuel est le rayon de votre rectangle?:\n"))
user = Cercle(radius_input)
user.display_info()
