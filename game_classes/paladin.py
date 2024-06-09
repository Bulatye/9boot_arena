from game_classes.person import *

class Paladin(Person):
    def __init__(self, name, health, base_attack, base_protection_percent):
        super().__init__(name, health * 2, base_attack, base_protection_percent * 2)