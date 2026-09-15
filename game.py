from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Lung"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        print(f"{hero.name} strikes! {hero.name} dealt " + str(hero_damage) + " damage!" )

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
            print(f"{enemy.name} retaliates! {enemy.name} dealt " + str(enemy_damage) + " damage!") 
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    hero = Hero("Axzyl")


    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{hero.name} approches with {hero.health} HP of their own")

    battle(hero, goblin)
if __name__ == "__main__":
    main()
