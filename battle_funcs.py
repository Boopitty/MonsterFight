from monster import Dragon, Golem, Unicorn, Automaton, Slime, Phoenix
import random

def list_all_monsters():
    monsters = ["Dragon", "Golem", "Unicorn", "Automaton", "Slime", "Phoenix"]
    print("Here are the available monsters:")

    for i, monster in enumerate(monsters, 1):
        print(f"{i}. {monster}")

def player_monster_selection(monster_list):
    monsters = ["Dragon", "Golem", "Unicorn", "Automaton", "Slime", "Phoenix"]

    while len(monster_list) < 3:
        choice = (input("Select a monster(enter its Number): ")).strip()
        
        # check if the input is a valid number
        if choice.isdigit() and 1 <= int(choice) <= len(monsters):
            monster_choice = monsters[int(choice) - 1]

            # check if the monster has already been chosen
            if monster_choice not in monster_list:
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
                monster_list.append(monster_instance)
                print(f"You have chosen {monster_choice}!")

            else:
                print("You have already chosen that monster. Please choose a different one.")
        else:
            print("Not a valid choice.")

    print("Great! The monsters you have chosen are:")
    for monster in monster_list:
        print(f"- {monster.name}")
    
    return monster_list

def enemy_monster_selection(monster_list):
    monsters = ["Dragon", "Golem", "Unicorn", "Automaton", "Slime", "Phoenix"]
    while len(monster_list) < 3:
        monster_choice = random.choice(monsters)
        if monster_choice not in [monster.name for monster in monster_list]:
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
            monster_list.append(monster_instance)
    
    print("The enemy has chosen the following monsters:")
    for monster in monster_list:
        print(f"- {monster.name}")
    
    return monster_list

def player_switch_active_monster(current_active, monster_team):
    print("Your current active monster is:", current_active.name)
    print("Your team is:")
    for i, monster in enumerate(monster_team, 1):
        print(f"{i}. {monster.name}")
    
    while True:
        choice = input("Choose a new active monster (enter its number): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(monster_team):
            new_active = monster_team[int(choice) - 1]
            if new_active.alive: # Check if the new active monster is alive
                if new_active != current_active: # Check if the new active monster is different from the current one
                    print(f"You switched to {new_active.name}!")
                    return new_active
                else:
                    print(f"This {new_active.name} is already active.")
            else:
                print(f"This {new_active.name} is dead and cannot be switched in.")
        else:
            print("Invalid number.")

def enemy_switch_active_monster(current_active, monster_team):
    while True:
        new_active = random.choice(monster_team)
        if (new_active != current_active) and new_active.alive:
            print(f"The enemy switched to {new_active.name}!")
            return new_active
        
def print_monster_base_stats(monster):
    print(f"{monster.name}'s stats:" \
          f"\nHealth: {monster.base_health}" \
          f"\nDurability: {monster.base_durability}" \
          f"\nSpirit: {monster.base_spirit}" \
          f"\nSpeed: {monster.base_speed}")

def print_monster_current_stats(monster):
    print(f"{monster.name}'s current stats:" \
          f"\nHealth: {monster.health}/{monster.base_health}" \
          f"\nDurability: {monster.durability}/{monster.base_durability}" \
          f"\nSpirit: {monster.spirit}/{monster.base_spirit}" \
          f"\nSpeed: {monster.speed}/{monster.base_speed}")