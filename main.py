import random

from game_classes.things import Thing
from game_classes.paladin import Paladin
from game_classes.warrior import Warrior
from game_classes.person import Person

magic_things = ["Звезда Провидения", "Меч Исцеления", "Плащ Тени", "Кристалл Возрождения", "Жезл Огня", "Щит Защиты", "Амулет Мороза", "Книга Заклинаний", "Сила в Яндексе", "Амулет дьявола", "Ревьер Салатхудинов"]


class Thing:
    def __init__(self, name, protection_percent, attack, health):
        self.name = name
        self.protection_percent = protection_percent
        self.attack = attack
        self.health = health


things = [Thing(magic_things[i], random.uniform(0, 0.1), random.randint(10, 20), random.randint(50, 100)) for i in range(random.randint(5, 10))]
names = ["Артем", "Борис", "Виктор", "Григорий", "Дмитрий", "Евгений", "Жан", "Захар", "Иван", "Константин", "Леонид", "Михаил", "Николай", "Олег", "Павел", "Роман", "Сергей", "Тимур", "Ульян", "Федор"]

characters = [Person(random.choice(names), random.randint(50, 100), random.randint(10, 20), random.uniform(0, 0.1)) for i in range(10)]

for character in characters:
    character.set_things(things)

# Вывод информации о персонажах и их экипировке
for character in characters:
    print(f"{character.name} - HP: {character.health}, Attack: {character.base_attack}, Base Protection: {character.base_protection_percent}")
    print("Экипировка:")
    for thing in character.things:
        print(f"- {thing.name} (Процент защиты: {thing.protection_percent})")
    print()
