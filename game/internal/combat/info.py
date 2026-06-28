def print_monster_info(monster):
    print(f"  {monster.summary}" \
          f"\n  Health: {monster.base_health}" \
          f"\n  Durability: {monster.base_durability}" \
          f"\n  Spirit: {monster.base_spirit}" \
          f"\n  Speed: {monster.base_speed}")

def print_monster_current_stats(monster):
    print(f"{monster.name}'s current stats:" \
          f"\nHealth: {monster.health}/{monster.base_health}" \
          f"\nDurability: {monster.durability}/{monster.base_durability}" \
          f"\nSpirit: {monster.spirit}/{monster.base_spirit}" \
          f"\nSpeed: {monster.speed}/{monster.base_speed}")