from boss import Beefcake
from hero import Hero

ARENA_NAME = "The Iron fung"

def battle(hero: Hero, enemy: Beefcake):
    global cooldown
    cooldown = 0
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        print(f"{hero.name} strikes! {hero.name} dealt " + str(hero_damage) + " damage!" )
        if enemy.is_alive():
            if cooldown == 1:
                enemy_damage = enemy.attack()
                print(f"{enemy.name} retaliates! {enemy.name} dealt " + str(enemy_damage) + " damage!")
                hero.take_damage(enemy_damage)
                cooldown = 0
            elif cooldown == 0:
                enemy_damage = enemy.megaSlash()
                print(f"{enemy.name} Uses their Ultimate Attack! {enemy.name} dealt " + str(enemy_damage) + " damage!")
                hero.take_damage(enemy_damage)
                cooldown = 1
                print(cooldown)
            
             
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Beefcake("Boogle")
    hero = Hero("Axzyl")


    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{hero.name} approches with {hero.health} HP of their own")

    battle(hero, goblin)
if __name__ == "__main__":
    main()
