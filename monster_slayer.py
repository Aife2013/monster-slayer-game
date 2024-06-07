import random

class Player:
    def __init__(self):
        self.health = 100
        self.turn_count = 0
        self.is_healing_available = True
        self.is_strong_attack_available = True

    def attack(self, target):
        damage = random.randint(10, 20)
        target.health -= damage
        print(f"You attack the monster and deal {damage} damage.")

    def strong_attack(self, target):
        damage = random.randint(20, 30)
        target.health -= damage
        print(f"You use a strong attack and deal {damage} damage.")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health += heal_amount
        print(f"You heal yourself and recover {heal_amount} health.")

    def is_alive(self):
        return self.health > 0

class Monster:
    def __init__(self):
        self.health = 100

    def attack(self, target):
        damage = random.randint(5, 15)
        target.health -= damage
        print(f"The monster attacks you and deals {damage} damage.")

    def is_alive(self):
        return self.health > 0

def main():
    player = Player()
    monster = Monster()

    print("Welcome to Monster Slayer!")
    print("You'll be battling a fierce monster. Good luck!")
    print()

    while player.is_alive() and monster.is_alive():
        print(f"Player Health: {player.health}")
        print(f"Monster Health: {monster.health}")
        print()

        # Player's turn
        action = input("Enter 'attack', 'strong attack', or 'heal': ").lower()
        if action == 'attack':
            player.attack(monster)
        elif action == 'strong attack' and player.is_strong_attack_available:
            player.strong_attack(monster)
            player.is_strong_attack_available = False
        elif action == 'heal' and player.is_healing_available:
            player.heal()
            player.is_healing_available = False
        else:
            print("Invalid action. Try again.")

        # Monster's turn
        if monster.is_alive():
            monster.attack(player)
        print()

        # Increment turn count and reset special actions availability
        player.turn_count += 1
        if player.turn_count % 3 == 0:
            player.is_strong_attack_available = True
        if player.turn_count % 5 == 0:
            player.is_healing_available = True

    # Check battle outcome
    if player.is_alive():
        print("Congratulations! You defeated the monster!")
    else:
        print("Game over! The monster defeated you.")

    # Ask if the player wants to start a new game
    new_game = input("Do you want to start a new game? (yes/no): ").lower()
    if new_game == 'yes':
        main()
    else:
        print("Thanks for playing Monster Slayer!")

if __name__ == "__main__":
    main()
