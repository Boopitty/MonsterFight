from enum import Enum

class SkillType(Enum):
    ATTACK = 1
    HEAL = 2
    UTILITY = 3

class skill():
    def __init__(self, name, physical, power, cooldown):
        self.name = name
        self.physical = physical
        self.power = power
        self.current_cooldown = 0
        self.cooldown = cooldown
        self.description = ""
        self.effect = ""
    
    def start_cooldown(self):
        self.current_cooldown = self.cooldown
    
    def reduce_cooldown(self, user_monster=None):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
    
    def is_available(self, user_name=None):
        # If user_name is provided, print a message about the skill being used or on cooldown
        if self.current_cooldown > 0:
            if user_name:
                print(f"{self.name} is on cooldown for {self.current_cooldown} more turns.")
            return False
        if user_name:
            print(f"{user_name} uses {self.name}!")
        return True
    
    def use(self, user=None, target=None):
        self.start_cooldown()

        match self.SkillType.name:
            case "ATTACK":
                # Calculate damage if the skill is an attack
                return self.get_damage(target)

            case "HEAL":
                # The healing amount of a move is its power
                return self.power
            
            case "UTILITY":
                # Apply the utiliy move's unique effect
                self.use_utility(user, target)
                return     

    def get_damage(self, target):
        if self.physical:
            damage = self.power - target.durability
            if damage <= 0:
                print(f"{target.name}'s durability is too high!")
        else:
            damage = self.power - target.spirit
            if damage <= 0:
                print(f"{target.name}'s spirit is too high!")
        if damage > 0:
            print(f"The attack is successful!")
        return damage

    def use_utility(self, user, target=None):
        # Placeholder for utility skill effects 
        return 0
    
    def end_utility(self, user):
        # Placeholder for ending utility skill effects
        return
    
    def print_info(self):
        print(f"\n  {self.description}"\
              f"\n  Type: {self.SkillType.name}")

        match self.SkillType:
            case SkillType.ATTACK:
                print(f"  Power: {self.power}")

            case SkillType.HEAL:
                print(f"  Heal Amount: {self.power}")

            case SkillType.UTILITY:
                print(f"  Effect: {self.effect}")
                print(f"  Duration: {self.duration} turns")

        print(f"  Cooldown: {self.cooldown} turns")
        
###### Attack skills ######
class Tackle(skill):
    def __init__(self):
        super().__init__(name="Tackle", physical=True, power=5, cooldown=0)
        self.SkillType = SkillType.ATTACK
        self.description = "A basic physical attack with no cooldown."

class FireBreath(skill):
    def __init__(self):
        super().__init__(name="Fire Breath", physical=False, power=10, cooldown=3)
        self.SkillType = SkillType.ATTACK
        self.description = "A powerful fire attack with a moderate cooldown."

class ClawSwipe(skill):
    def __init__(self):
        super().__init__(name="Claw Swipe", physical=True, power=6, cooldown=2)
        self.SkillType = SkillType.ATTACK
        self.description = "A quick physical attack with a short cooldown."

class TailWhip(skill):
    def __init__(self):
        super().__init__(name="Tail Whip", physical=True, power=7, cooldown=2)
        self.SkillType = SkillType.ATTACK
        self.description = "A strong physical attack with a short cooldown."

class MagicBolt(skill):
    def __init__(self):
        super().__init__(name="Magic Bolt", physical=False, power=7, cooldown=2)
        self.SkillType = SkillType.ATTACK
        self.description = "A strong magic attack with a short cooldown."

class Slam(skill):
    def __init__(self):
        super().__init__(name="Slam", physical=True, power=10, cooldown=3)
        self.SkillType = SkillType.ATTACK
        self.description = "A powerful physical attack with a moderate cooldown."

class Splat(skill):
    def __init__(self):
        super().__init__(name="Splat", physical=True, power=4, cooldown=0)
        self.SkillType = SkillType.ATTACK
        self.description = "A pathetic strike with no cooldown."

###### Heal skills ######
class Heal(skill):
    def __init__(self):
        super().__init__(name="Heal", physical=False, power=3, cooldown=2)
        self.SkillType = SkillType.HEAL
        self.description = "Basic healing ability with a short cooldown."

###### Utility skills ######
class Overdrive(skill):
    def __init__(self):
        super().__init__(name="Overdrive", physical=False, power=0, cooldown=5)
        self.SkillType = SkillType.UTILITY
        self.duration = 3
        self.description = "Temporary boost to user's offence."
        self.effect = "Power and speed increased by 3 for 3 turns."

    def use_utility(self, user, target):
        print(f"{user.name}'s speed and power increased for 3 turns!")
        
        user.speed += 3
        for ability in user.abilities:
            if ability.SkillType == SkillType.ATTACK:
                ability.power += 3
    
    def end_utility(self, user):
        print(f"{user.name}'s Overdrive has ended. Speed and power returned to normal.")

        user.speed -= 3
        for ability in user.abilities:
            if ability.SkillType == SkillType.ATTACK:
                ability.power -= 3
        
    def reduce_cooldown(self, user):
        super().reduce_cooldown()
        
        # The duration of a utility move's effect is tied to it's cooldown
        if self.current_cooldown == self.cooldown - self.duration:
            self.end_utility(user)

class Barrier(skill):
    def __init__(self):
        super().__init__(name="Barrier", physical=False, power=0, cooldown=5)
        self.SkillType = SkillType.UTILITY
        self.duration = 3
        self.description = "Temporary boost to user's defences."
        self.effect = "Durability and spirit increased by 3 for 3 turns."
    
    def use_utility(self, user, target):
        print(f"{user.name}'s durability increased for 3 turns!")
        user.durability += 3
        user.spirit += 3
    
    def end_utility(self, user):
        print(f"{user.name}'s barrier has ended. Durability returned to normal.")
        user.durability -= 3
        user.spirit -= 3
    
    def reduce_cooldown(self, user):
        super().reduce_cooldown()
        if self.current_cooldown == self.cooldown - self.duration:
            self.end_utility(user)