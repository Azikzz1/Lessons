# import Lesson1
# from Lesson1 import Person
#
# person_test = Person(name="Andrey", age=20, city="Bishkek")
#
# print(person_test.introduse())


# Принципы ООП
# Объектно-ориентированное программирование (ООП) — это парадигма программирования, которая основывается на
#    представлении программы как совокупности объектов, взаимодействующих между собой. Основные принципы ООП включают:

# Наследование: позволяет одному классу (производному) унаследовать свойства и методы другого класса (базового),
#    расширяя или изменяя их. Наследование способствует повторному использованию кода и созданию иерархии классов.

# Полиморфизм: предоставляет возможность объектам разных классов обрабатывать одно и то же сообщение по-разному.
#   С помощью полиморфизма можно создавать гибкие интерфейсы, работающие с разными типами объектов,
#    что повышает гибкость и масштабируемость кода.

# Инкапсуляция: предполагает объединение данных и методов, работающих с этими данными, в единое целое — объект.
#   Это позволяет скрыть внутреннее устройство объекта и защитить данные от прямого доступа и изменений извне.

# Абстракция: этот принцип позволяет выделить ключевые характеристики объектов, скрывая детали их реализации.
#    Благодаря абстракции, можно сосредоточиться на общих свойствах и поведении объектов, игнорируя излишние детали.

# Базовый\Супер\Родительский\
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        return f"Я {self.name}, мой уровень здоровья: {self.health}"

    def rest(self):
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.health}"

    def action(self):
        return f"{self.name} выполняет базовое действие.\n"


# Класс Mage, наследующийся от Hero
class Mage(Hero):
    def __init__(self, name, health, mana=100):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} использует заклинание! Оставшаяся мана: {self.mana}"
        else:
            return f"{self.name} недостаточно маны для заклинания!"

    def action(self):
        base_action = super().action()
        spell_result = self.cast_spell()  # Вызов метода внутри другого метода
        return f"{base_action} {spell_result}"


def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())


mage = Mage("Гэндальф", 100, 50)

hero_action(mage)


class Tank(Hero):
    def __init__(self, name, health, power=100):
        super().__init__(name, health)
        self.power = power

    def cast_spell(self):
        if self.power >= 20:
            self.power -= 10
            return f"{self.name} использует заклинание! Оставшаяся сила: {self.power}"
        else:
            return f"{self.name} не достаточно силы для удара!"

    def action(self):
        base_action1 = super().action()
        spell_result1 = self.cast_spell()
        return f"{base_action1} {spell_result1}"


def hero_action1(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())


tank = Tank("Барбос", 100, 100)

hero_action1(tank)
