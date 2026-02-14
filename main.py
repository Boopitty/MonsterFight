import time
from battle_funcs import list_all_monsters, player_monster_selection, enemy_monster_selection

# This function allows the player to select 3 monsters from the available list

print("Hello, Monster Fighter!")

time.sleep(2) # delay each line for 2 seconds
print("Before you can start monster fighting, you need some monsters!")
time.sleep(2)
print("Each player needs 3 monsters to start battling.")
time.sleep(2)
print("Here are the available monsters:")
time.sleep(2)

list_all_monsters()

player_monsters = []
enemy_monsters = []

# Monster selection phase for both player and enemy
print("Select your monsters:")
player_monster_selection(player_monsters)
time.sleep(2)
print("Now, select the enemy's monsters:")
enemy_monster_selection(enemy_monsters)

# Set the first monster in each player's list as the active monster for the battle
active_friendly = player_monsters[0]
active_enemy = enemy_monsters[0]

time.sleep(2)
print("Now that you have your monsters, you can start battling!")