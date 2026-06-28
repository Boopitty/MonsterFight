import random

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