import random



class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 5
    def attack(self):
        # Attacks with multiple daggers as a Rouge
        damageBuildup = 0
        for i in range(5):
            damageBuildup += random.randint(1, self.attack_power)
        return damageBuildup
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} points of damage, Health: {self.health}")
    def is_alive(self):
        return self.health > 0