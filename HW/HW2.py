from main import Hero

my_hero = Hero(name="ChocaLoca", health=100, power=100, damage=60)


class Tank(Hero):
    def __init__(self, name, health, power, damage, fatigue=100):
        super().__init__(name, health, power, damage)
        self.fatigue = fatigue

    def do_damage(self):
        if self.power <= 20:
            self.damage = 30
            self.fatigue -= 30
            return f"{self.name} делает слабый удар, нанося {self.damage} единиц урона из за количества сил: {self.power}, усталость: {self.fatigue}"
        elif self.power == 100:
            self.damage = 60
            self.fatigue -= 5
            return f"{self.name} делает сильный удар, нанося {self.damage} единиц урона из за количества сил: {self.power}, усталость: {self.fatigue}"
        else:
            self.fatigue -= 10
            return f"{self.name} делает обычный удар, нанося {self.damage} единиц урона. Усталость: {self.fatigue}"

    def action(self):
        if self.health <= 0:
            return f"{self.name} мертв и не может выполнять действия."
        base_action = super().action()
        damage_result = self.do_damage()
        return f"{base_action} {damage_result}"


def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())


tank = Tank("ChocaLoca", 100, 20, 50, 100)

hero_action(tank)


