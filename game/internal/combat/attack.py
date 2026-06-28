import random
import time

def battle(attacker, defender):
    # Select an ability to use and call other functions to calculate damage
    print(f"{attacker.name} has the following abilities:")
    for i, ability in enumerate(attacker.abilities):
        print(f"  {i + 1}. {ability.name}")
        
    # Get user input for which ability to use
    while True:
        choice = input("Select an ability(Type its number or 'i' for info): ").strip().lower()

        if choice == "i":
            # Print info for each ability
            for i, ability in enumerate(attacker.abilities):
                print(f"\n{i + 1}. {ability.name}:")
                ability.print_info()
            print("\n")

        elif choice.isdigit() and 1 <= int(choice) <= len(attacker.abilities):
            # Get the ability and use it on the target
            ability = attacker.abilities[int(choice) - 1]

            if ability.is_available(attacker.name):
                time.sleep(2)
                match ability.SkillType.name:

                    case "ATTACK":
                        damage = ability.use(user = attacker, target = defender)
                        time.sleep(2)
                        defender.take_damage(damage)
                        time.sleep(2)

                    case "HEAL":
                        heal_amount = ability.use(user = attacker)
                        attacker.heal(heal_amount)
                        time.sleep(2)

                    case "UTILITY":
                        # Utility skills do not affect target health
                        ability.use(user = attacker, target = defender)
                        time.sleep(2)
                break
                
        else:
            choice = input("Invalid input. Please try again. ")

def random_battle(attacker, defender):
    while True:
        # Pick a random attack.
        ability = random.choice(attacker.abilities)

        # If the attack chosen is on cooldown, pick again until one with no cooldown if found
        # All monsters should have a move with no cooldown to prevent infinite looping.
        if ability.is_available():
            print(f"{attacker.name} uses {ability.name}!")
            time.sleep(2)

            match ability.SkillType.name:
                case "ATTACK":
                    damage = ability.use(user = attacker, target = defender)
                    time.sleep(2)
                    defender.take_damage(damage)

                case "HEAL":
                    heal_amount = ability.use(user = attacker)
                    attacker.heal(heal_amount)
                    time.sleep(2)

                case "UTILITY":
                    # Utility skills do not affect target health
                    ability.use(user = attacker, target = defender)
                    time.sleep(2)
            break

