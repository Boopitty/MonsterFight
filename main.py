import random
import time
import battle_funcs

# This function allows the player to select 3 monsters from the available list

print("Hello, Monster Fighter!")

time.sleep(2) # delay each line for 2 seconds
print("Before you can start monster fighting, you need some monsters!")
time.sleep(2)
print("Each player needs 3 monsters to start battling.")
time.sleep(2)

battle_funcs.list_all_monsters() # Print the list of available monsters for the player to choose from

player_monsters = []
enemy_monsters = []

# Monster selection phase for both player and enemy
battle_funcs.player_monster_selection(player_monsters) # Player selects their monsters manually
time.sleep(2)

print("Now, the enemy is choosing their monsters...")
battle_funcs.enemy_monster_selection(enemy_monsters) # Enemy selects their monsters randomly
time.sleep(2)

# Set the first monster in each player's list as the active monster for the battle
active_friendly = player_monsters[0]
active_enemy = enemy_monsters[0]

print("Now that you have your monsters, you can start battling!")
time.sleep(2)
print(f"Your active monster is {active_friendly.name}.\n"
      f"The enemy's active monster is {active_enemy.name}.")

counter = 1
# Battle loop - this will continue until one player's team is completely defeated
while True:
    print(f"\n--- Round {counter} ---\n")
    counter += 1
    # Check if the player's active monster is alive, if not, prompt to switch
    if not active_friendly.alive:
        if all(not monster.alive for monster in player_monsters):
            print("All your monsters have been defeated! You lose!")
            break

        time.sleep(2)
        print("Please choose a new active monster from your team:")
        active_friendly = battle_funcs.player_switch_active_monster(active_friendly, player_monsters)
    
    # Check if the enemy's active monster is alive, if not, switch to a new one
    if not active_enemy.alive:
        if all(not monster.alive for monster in enemy_monsters):
            print("All enemy monsters have been defeated! You win!")
            break

        time.sleep(2)
        print("The enemy is choosing a new active monster...")
        time.sleep(2)
        active_enemy = battle_funcs.enemy_switch_active_monster(active_enemy, enemy_monsters)
    
    # Cooldown reduction phase - reduce cooldowns for all skills of both active monsters
    active_friendly.cooldown_abilities()
    active_enemy.cooldown_abilities()
    
    # Determine turn order based on speed and execute actions
    if active_friendly.speed > active_enemy.speed:
        result = battle_funcs.player_action(active_friendly, active_enemy, player_monsters)
        if result is not None:
            active_friendly = result
        battle_funcs.enemy_action(active_enemy, active_friendly)

    elif active_enemy.speed > active_friendly.speed:
        battle_funcs.enemy_action(active_enemy, active_friendly) 
        result = battle_funcs.player_action(active_friendly, active_enemy, player_monsters)
        if result is not None:
            active_friendly = result

    else:
        # If speeds are equal, randomly decide who goes first
        if random.choice([True, False]):
            result = battle_funcs.player_action(active_friendly, active_enemy, player_monsters)
            if result is not None:
                active_friendly = result
            battle_funcs.enemy_action(active_enemy, active_friendly)
        else:
            battle_funcs.enemy_action(active_enemy, active_friendly)  
            result = battle_funcs.player_action(active_friendly, active_enemy, player_monsters)
            if result is not None:
                active_friendly = result

print("Thanks for playing Monster Fight!")