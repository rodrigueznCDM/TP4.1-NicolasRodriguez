"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Exercice POO #1
"""
print("TP4.1 - POO #1\n")


class StringFoo:
    def __init__(self):
        self.message = "[message here]"

    def set_string(self, string):
        self.message = string

    def print_string(self):
        print(f"Ton message: {self.message.upper()}")


user = StringFoo()
user.set_string(input("\nQuel est votre message?:\n"))
user.print_string()
