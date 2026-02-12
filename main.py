import time
from monster import Dragon, Golem, Unicorn, Automaton, Slime, Phoenix

print("Hello, Monster Fighter!")

# delay each line for 2 seconds
time.sleep(2)
print("Before you can start monster fighting, you need some monsters!")
time.sleep(2)
print("You need 3 monsters to start to begin.")
time.sleep(2)
print("Here are the available monsters:")
time.sleep(2)

monsters = ["Dragon", "Golem", "Unicorn", "Automaton", "Slime", "Phoenix"]
for i, monster in enumerate(monsters, 1):
    print(f"{i}. {monster}")

player_monsters = []
while len(player_monsters) < 3:
    choice = (input("Enter the number of the monster you want to choose: ")).strip()
    
    # check if the input is a valid number
    if choice.isdigit() and 1 <= int(choice) <= len(monsters):
        monster_choice = monsters[int(choice) - 1]

        # check if the monster has already been chosen
        if monster_choice not in player_monsters:
            match monster_choice:
                case "Dragon":
                    monster_instance = Dragon()
                case "Golem":
                    monster_instance = Golem()
                case "Unicorn":
                    monster_instance = Unicorn()
                case "Automaton":
                    monster_instance = Automaton()
                case "Slime":
                    monster_instance = Slime()
                case "Phoenix":
                    monster_instance = Phoenix()
            player_monsters.append(monster_instance)
            print(f"You have chosen {monster_choice}!")

        else:
            print("You have already chosen that monster. Please choose a different one.")
    else:
        print("Not a valid choice.")

print("Great! The monsters you have chosen are:")
for monster in player_monsters:
    print(f"- {monster.name}")

active_friendly = player_monsters[0]
active_enemy = player_monsters[1]

time.sleep(2)
print("Now that you have your monsters, you can start battling!")
time.sleep(2)
print(f"For now, lets have your first monster, the {active_friendly.name}, attack the second monster, the {active_enemy.name}.")
time.sleep(2)

while active_friendly.is_alive() and active_enemy.is_alive():
    active_friendly.attack(active_enemy)
    if not active_enemy.is_alive():
        print(f"{active_enemy.name} has been defeated!")
        break
    if not active_friendly.is_alive():
        print(f"{active_friendly.name} has been defeated!")
        break
print("Thanks for playing Monster Fighter! More features will be added soon!")