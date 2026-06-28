import internal.structure.monsters as monsters
import internal.combat.info as info
import random
import time
    
def player_monster_selection(monster_list):
    mons = ["Dragon", "Golem", "Unicorn", "Automaton", "Slime", "Phoenix"]

    while len(monster_list) < 3:
        # Print the list of available monsters for the player to choose from
        print("\nAvailable monsters:")
        for i, mon in enumerate(mons):
            print(f"{i + 1}. {mon}")

        choice = (input("Select a monster(Enter its number or 'i' for info): ")).strip()
        
        # If input if "i" print info for all available monsters
        if choice == "i":
            print("\nHere are the available monsters and their base stats:")
            for i, mon in enumerate(mons):
                print(f"\n{i + 1}. {mon}:")

                match mon:
                    case "Dragon":
                        info.print_monster_info(monsters.Dragon())
                    case "Golem":
                        info.print_monster_info(monsters.Golem())
                    case "Unicorn":
                        info.print_monster_info(monsters.Unicorn())
                    case "Automaton":
                        info.print_monster_info(monsters.Automaton())
                    case "Slime":
                        info.print_monster_info(monsters.Slime())
                    case "Phoenix":
                        info.print_monster_info(monsters.Phoenix())
        
        # Check if input is a number with a corresponding monster
        elif choice.isdigit() and 1 <= int(choice) <= len(mons):
            # Remove chosen monster from the list, and check if it has already been chosen
            name = mons.pop(int(choice) - 1)

            if name not in [monster.name for monster in monster_list]:
                match name:
                    case "Dragon":
                        monster_instance = monsters.Dragon()
                    case "Golem":
                        monster_instance = monsters.Golem()
                    case "Unicorn":
                        monster_instance = monsters.Unicorn()
                    case "Automaton":
                        monster_instance = monsters.Automaton()
                    case "Slime":
                        monster_instance = monsters.Slime()
                    case "Phoenix":
                        monster_instance = monsters.Phoenix()
                        
                monster_list.append(monster_instance)
                print(f"You have chosen {name}!")

            else:
                print("You have already chosen that monster. Please choose a different one.")
        else:
            print("Invalid input.")

    print("\nGreat! The monsters you have chosen are:")
    for mon in monster_list:
        print(f"- {mon.name}")
    
    return monster_list

def enemy_monster_selection(monster_list):
    mons = ["Dragon", "Golem", "Unicorn", "Automaton", "Slime", "Phoenix"]
    while len(monster_list) < 3:
        choice = random.choice(mons)
        if choice not in [monster.name for monster in monster_list]:
            match choice:
                case "Dragon":
                    monster_instance = monsters.Dragon()
                case "Golem":
                    monster_instance = monsters.Golem()
                case "Unicorn":
                    monster_instance = monsters.Unicorn()
                case "Automaton":
                    monster_instance = monsters.Automaton()
                case "Slime":
                    monster_instance = monsters.Slime()
                case "Phoenix":
                    monster_instance = monsters.Phoenix()
            monster_list.append(monster_instance)
    time.sleep(2)
    
    print("The enemy has chosen the following monsters:")
    for monster in monster_list:
        print(f"- {monster.name}")
    time.sleep(2)
    return monster_list