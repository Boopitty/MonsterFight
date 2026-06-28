import time
import internal.combat.attack as attack, internal.combat.info as info, internal.combat.switch as switch

def player_action(friendly, enemy, player_monsters):
    if not friendly.alive:
        print(f"Your {friendly.name} is defeated and cannot take action!")
        time.sleep(2)
        return None
    
    print("\nIt's your turn!")
    time.sleep(2)

    while True:
        print("\nWhat would you like to do?"\
          "\n1. Attack"\
          "\n2. Switch active monster"\
          "\n3. View Status"\
          "\n4. Surrender")
        action = input("\nType in an action(Type the number): ").strip().lower()

        if action.isdigit():
            match int(action):
                case 1:
                    # player selects an ability to attack the enemy's active monster
                    attack.battle(friendly, enemy) 
                    return None
                
                case 2:
                    # player swaps their active monster with another monster in their team
                    friendly = switch.player_switch_active_monster(friendly, player_monsters)
                    time.sleep(2)
                    return friendly
                
                case 3:
                    print(f"\n---- Your monster's stats: ----")
                    info.print_monster_current_stats(friendly)
                    print(f"\n---- Enemy monster's stats: ----")
                    info.print_monster_current_stats(enemy)

                case 4:
                    print("You have surrendered! You lose!")
                    time.sleep(2)
                    print("Thanks for playing Monster Fight!")
                    exit()
                    return None
                
                case _:
                    print("Invalid number.")
        else:
            print("Invalid input.")

def enemy_action(enemy, friendly):
    if not enemy.alive:
        print(f"The enemy's {enemy.name} is defeated and cannot take action!")
        time.sleep(2)
        return
    
    print("\nThe enemy is taking their turn...")
    time.sleep(2)
    # For simplicity, the enemy will always attack
    attack.random_battle(enemy, friendly)