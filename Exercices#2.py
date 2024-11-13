"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Exercice POO #2
"""
print("TP4.1 - POO #2\n")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.calculate_area()

    def calculate_area(self):
        area = self.length * self.width
        return area

    def display_info(self):
        print(f"\nLes mesures de votre rectangle sont:\n"
              f"\nLongueur: {self.length}"
              f"\nLargeur: {self.width}"
              f"\nAire: {self.area}")


length_input = int(input("\nQuelle est la longueur de votre rectangle?:\n"))
width_input = int(input("\nQuelle est la largeur de votre rectangle?:\n"))
shape = Rectangle(length_input, width_input)
shape.display_info()
