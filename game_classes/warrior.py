class Warrior(Person):
    def __init__(self, name, health, base_attack, base_protection_percent):
        super().__init__(name, health, base_attack * 2, base_protection_percent)