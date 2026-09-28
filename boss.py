from enemy import Enemy
import random

cooldown = 0
class Beefcake(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 30

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)

    def megaSlash(self):
        return 40