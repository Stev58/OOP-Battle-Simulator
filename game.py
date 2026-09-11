from goblin import Goblin


ARENA_NAME = "The Salty Spitoon"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")


    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    print(f"{goblin.name} and {goblin2.name} enter the arena with {goblin.health} health and {goblin2.health} respectively.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
