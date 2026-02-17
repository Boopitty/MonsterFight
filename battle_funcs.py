from monster import Dragon, Golem, Unicorn, Automaton, Slime, Phoenix
import random
import time

def list_all_monsters():
    monsters = ["Dragon", "Golem", "Unicorn", "Automaton", "Slime", "Phoenix"]
    print("Here are the available monsters:")

    for i, monster in enumerate(monsters, 1):
        print(f"{i}. {monster}")

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
    
def player_monster_selection(monster_list):
    monsters = ["Dragon", "Golem", "Unicorn", "Automaton", "Slime", "Phoenix"]

    while len(monster_list) < 3:
        choice = (input("Select a monster(enter its Number): ")).strip()
        
        # check if the input is a valid number
        if choice.isdigit() and 1 <= int(choice) <= len(monsters):
            monster_choice = monsters[int(choice) - 1]

            # check if the monster has already been chosen
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
    time.sleep(2)
    return monster_list

def player_switch_active_monster(current_active, monster_team):
    print(f"Your current active monster is: {current_active.name}")
    print("Your team is:")

    # List the monsters in the player's team with their corresponding numbers
    for i, monster in enumerate(monster_team, 1):
        print(f"{i}. {monster.name}: {monster.health}/{monster.base_health} hp" if monster.alive else f"{i}. {monster.name}: Defeated")
    
    while True:
        choice = input("Choose a new active monster (enter its number): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(monster_team): # Check for valid input
            selection = monster_team[int(choice) - 1]

            if selection.alive: # Check if the new active monster is alive

                if selection != current_active: # Check if the new active monster is different from the current one
                    print(f"Switching to {selection.name}!")
                    return selection
                else:
                    print(f"This {selection.name} is already active.")
            else:
                print(f"This {selection.name} is dead and cannot be switched in.")
        else:
            print("Invalid number.")

def enemy_switch_active_monster(current_active, monster_team):
    while True:
        selection = random.choice(monster_team)
        if (selection != current_active) and selection.alive:
            print(f"The enemy switched to {selection.name}!")
            return selection
         
def player_action(active_friendly, active_enemy, player_monsters):
    if not active_friendly.alive:
        print(f"Your {active_friendly.name} is defeated and cannot take action!")
        return None
    
    while True:
        action = input("\nType in an action (attack, switch, stats, surrender): ").strip().lower()
        match action:
            case "attack":
                # player selects an ability to attack the enemy's active monster
                active_friendly.attack(active_enemy) 
                return None
            case "switch":
                # player swaps their active monster with another monster in their team
                active_friendly = player_switch_active_monster(active_friendly, player_monsters)
                time.sleep(2)
                return active_friendly
            case "surrender":
                print("You have surrendered! You lose!")
                time.sleep(2)
                print("Thanks for playing Monster Fight!")
                exit()
                return None
            case "stats":
                print(f"\n---- Your monster's stats: ----")
                print_monster_current_stats(active_friendly)
                print(f"\n---- Enemy monster's stats: ----")
                print_monster_current_stats(active_enemy)
            case _:
                print("Invalid action. Please type 'attack', 'switch', or 'surrender'.")

def enemy_action(active_enemy, active_friendly):
    if not active_enemy.alive:
        print(f"The enemy's {active_enemy.name} is defeated and cannot take action!")
        return
    
    print("\nThe enemy is taking their turn...")
    time.sleep(2)
    # For simplicity, the enemy will always attack
    active_enemy.random_attack(active_friendly)