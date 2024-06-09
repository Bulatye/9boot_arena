class Person:
    def __init__(self, name, health, base_attack, base_protection_percent):
        self.name = name
        self.health = health
        self.base_attack = base_attack
        self.base_protection_percent = base_protection_percent
        self.things = []

    def set_things(self, things):
        self.things = things

    def reduce_health(self, attack_damage):
        total_protection = self.base_protection_percent
        for thing in self.things:
            total_protection += thing.protection_percent
        damage_taken = (attack_damage - attack_damage*total_protection)
        self.health -= damage_taken
        print(f"{self.name} получил {damage_taken} урона. Текущее здоровье: {self.health}")
