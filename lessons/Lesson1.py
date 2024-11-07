class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduse(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в городе {self.city}."

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"Имя: {self.name}\n Возраст: {self.age}\n Город: {self.city}"


person_1 = Person("Aziret", 17,"Bishkek")
person_2 = Person("Aliya", 20, "Bishkek")
person_3 = Person("Nurayim", 22, "Bishkek")
person_4 = Person("Almaz", 50, "Bishkek")

print(person_1.introduse())
print(person_2.introduse())
print(person_3.introduse())
print(person_4.introduse())

print(person_1.is_adult())
print(person_3.is_adult())
print(person_3.is_adult())
print(person_4.is_adult())

print(person_1)
print(person_2)
print(person_3)
print(person_4)

t = []