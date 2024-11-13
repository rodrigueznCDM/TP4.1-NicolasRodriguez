"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Exercice POO #1
"""
print("TP4.1 - POO #1\n")


class StringFoo:
    def __init__(self):
        self.message = "[user_message]"

    def set_string(self, string):
        self.message = string

    def print_string(self):
        print(f"\nTon message: {self.message.upper()}\n")


user_input = StringFoo()
user_input.set_string(input("\nQuel est votre message?:\n"))
user_input.print_string()
