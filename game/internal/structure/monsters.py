import game.internal.structure.skills as skills
import time

class Monster():

    def __init__(self, name, health, durability, spirit, speed):
        self.name = name
        self.base_health = health
        self.health = health

        self.base_durability = durability
        self.durability = durability

        self.base_spirit = spirit
        self.spirit = spirit

        self.base_speed = speed
        self.speed = speed

        self.alive = True
        self.abilities = []
    
    def get_ability(self, index):
        if 0 <= index < len(self.abilities):
            return self.abilities[index]
        return None
    
    def print_summary(self):
        print(f"\n{self.summary}\n")

    def take_damage(self, damage):
        if damage <= 0:
            print(f"{self.name} took no damage!")
            time.sleep(2)
            return
        
        print(f"{self.name} takes {damage} damage!")
        time.sleep(2)
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            self.alive = False

        # Check if the monster is still alive after taking damage
        if self.alive:
            print(f"{self.name} has {self.health} hp remaining.")
        else:
            self.alive = False
            print(f"{self.name} has been defeated!")
        time.sleep(2)

    def full_revive(self):
        if not self.alive:
            self.health = self.base_health
            self.alive = True
            print(f"{self.name} has been fully revived with {self.health} hp!")
        else:
            print(f"{self.name} is already alive and cannot be revived.")

    def revive(self):
        if not self.alive:
            self.health = 1
            self.alive = True
            print(f"{self.name} has been revived with {self.health} hp!")
        else:
            print(f"{self.name} is already alive and cannot be revived.")

    def full_heal(self):
        if self.alive:
            if self.health == self.base_health:
                print(f"{self.name} is already at full health and cannot be healed.")
                return
            self.health = self.base_health
            print(f"{self.name} has been fully healed!")
        else:
            print(f"{self.name} cannot be healed because it is defeated.")

    def heal(self, amount):
        
        if self.alive:   
            if self.health == self.base_health:
                print(f"{self.name} is already at full health and cannot be healed.")
                return
            
            if amount <= 0:
                print(f"{self.name} recovers no health.")
                return
            
            self.health += amount
            amount_healed = amount

            if self.health > self.base_health:
                amount_healed = self.base_health - (self.health - amount)
                self.health = self.base_health

            print(f"{self.name} recovered {amount_healed} hp and now has {self.health} hp!")

        else:
            print(f"{self.name} cannot be healed because it is defeated.")
        
    def cooldown_abilities(self):
        # Reduce cooldown of all moves
        for ability in self.abilities:
            # Pass self as arg if the move is a utility
            if ability.SkillType.name == "UTILITY":
                ability.reduce_cooldown(self)
            else:
                ability.reduce_cooldown()
            
class Dragon(Monster):
    def __init__(self):
        super().__init__(name="Dragon", health=15, durability=6, spirit=6, speed=4)
        self.summary = "A powerful and durable monster, but not very fast."
        self.abilities = [skills.Tackle(), skills.ClawSwipe(), skills.TailWhip(), skills.FireBreath()]

class Golem(Monster):
    def __init__(self):
        super().__init__(name="Golem", health=20, durability=7, spirit=4, speed=3)
        self.summary = "A very durable monster, but not very fast."
        self.abilities = [skills.Tackle(), skills.Slam(), skills.Barrier()]

class Unicorn(Monster):
    def __init__(self):
        super().__init__(name="Unicorn", health=15, durability=4, spirit=7, speed=8)
        self.summary = "A fast and agile monster with moderate durability. Has a special ability to heal itself."
        self.abilities = [skills.Tackle(), skills.Slam(), skills.TailWhip(), skills.Heal()]

class Automaton(Monster):
    def __init__(self):
        super().__init__(name="Automaton", health=13, durability=5, spirit=5, speed=6)
        self.summary = "A balanced monster with moderate stats in all areas. Can temporarily overcharge itself."
        self.abilities = [skills.Tackle(), skills.MagicBolt(), skills.Overdrive()]

class Slime(Monster):
    def __init__(self):
        super().__init__(name="Slime", health=35, durability=1, spirit=1, speed=1)
        self.summary = "Low offence, durability and speed. However, it can regenerate its already massive health pool."
        self.abilities = [skills.Splat(), skills.Heal()]

class Phoenix(Monster):
    def __init__(self):
        super().__init__(name="Phoenix", health=10, durability=2, spirit=7, speed=10)
        self.summary = "A very fast monster with low health and durability. Can resurrect itself once per battle."
        self.abilities = [skills.Tackle(), skills.ClawSwipe(), skills.FireBreath()]