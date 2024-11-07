class Hero:
    def __init__(self, name, health, power, damage):
        self.name = name
        self.health = health
        self.power = power
        self.damage = damage

    def introduce(self):
        return f"Я {self.name}, мой уровень здоровья {self.health}, мой уровень силы {self.power}" \
               f" и я наношу по {self.damage} единиц урона"

    def rest(self):
        if self.health <= 0:
            return f"{self.name} уже мертв и не может отдыхать!"
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.health}"

    def action(self):
        return f"{self.name} выполняет базовое действие!\n"