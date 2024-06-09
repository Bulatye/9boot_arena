import random
from game_classes.things import Thing
from game_classes.paladin import Paladin
from game_classes.warrior import Warrior
from game_classes.person import Person

magic_things = ["Звезда Провидения", "Меч Исцеления", "Плащ Тени", "Кристалл Возрождения", "Жезл Огня", "Щит Защиты", "Амулет Мороза", "Книга Заклинаний", "Сила в Яндексе", "Амулет дьявола", "Ревьер Салатхудинов"]
names = ["Артем", "Борис", "Виктор", "Григорий", "Дмитрий", "Евгений", "Жан", "Захар", "Иван", "Константин", "Леонид", "Михаил", "Николай", "Олег", "Павел", "Роман", "Сергей", "Тимур", "Ульян", "Федор"]

things = [Thing(magic_things[i], random.uniform(0, 0.1), random.randint(10, 20), random.randint(50, 100)) for i in range(0, 10)]
characters = [Person(random.choice(names), random.randint(50, 100), random.randint(10, 20), random.uniform(0, 0.1)) for i in range(10)]

for character in characters:
    count = random.randint(0, 5)
    character_things = []
    for _ in range(0, count):
        character_things.append(random.choice(things))
    character.set_things(character_things)

for character in characters:
    print(f"{character.name} - Здоровье: {character.health}, Атака: {character.base_attack}, Базовая Броня: {character.base_protection_percent}")
    print("Экипировка:")
    for thing in character.things:
        print(f"- {thing.name} (Процент защиты: {thing.protection_percent})")
    print()

print("\n-----------------------------Бой начинается! ---------------------------------------\n")
while len(characters) > 1:
    attacker = random.choice(characters)
    defender = random.choice(characters)
    while defender == attacker:
        defender = random.choice(characters)

    attack_damage = attacker.base_attack
    final_protection = defender.base_protection_percent
    for thing in defender.things:
        final_protection += thing.protection_percent

    damage_taken = max(attack_damage - attack_damage * final_protection, 0)
    defender.health -= damage_taken

    print(f"{attacker.name} наносит удар  {defender.name} на {damage_taken} урона!!!!")

    if defender.health <= 0:
        characters.remove(defender)
        print(f"{defender.name} погиб!")

print("\n----------------------------- Бой закончился ---------------------------------------\n")
print(f"{characters[0].name} переиграл с {characters[0].health} единацами здоровья!!!!!!")
