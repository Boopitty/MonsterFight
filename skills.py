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
    
    def use(self, user, target=None):
        if self.current_cooldown > 0:
            print(f"{self.name} is on cooldown for {self.current_cooldown} more turns.")
            return -1
        self.start_cooldown()

        match self.SkillType.name:
            case "ATTACK":
                damage = self.get_damage(target)
            case "HEAL":
                return self.power
            case "UTILITY":
                self.use_utility(user, target)
                return 0
        return damage

    def get_damage(self, target):
        if self.physical:
            damage = self.power - target.durability
        else:
            damage = self.power - target.spirit
        return damage

    def use_utility(self, user, target):
        # Placeholder for utility skill effects 
        return 0
        
        
###### Attack skills ######
class FireBreath(skill):
    def __init__(self):
        super().__init__(name="Fire Breath", physical=False, power=10, cooldown=3)
        self.SkillType = SkillType.ATTACK

class ClawSwipe(skill):
    def __init__(self):
        super().__init__(name="Claw Swipe", physical=True, power=5, cooldown=1)
        self.SkillType = SkillType.ATTACK

class TailWhip(skill):
    def __init__(self):
        super().__init__(name="Tail Whip", physical=True, power=7, cooldown=2)
        self.SkillType = SkillType.ATTACK

class MagicBolt(skill):
    def __init__(self):
        super().__init__(name="Magic Bolt", physical=False, power=7, cooldown=2)
        self.SkillType = SkillType.ATTACK

# skill to test 0 power and 0 cooldown
class Tap(skill):
    def __init__(self):
        super().__init__(name="Tap", physical=True, power=0, cooldown=0)
        self.SkillType = SkillType.ATTACK

###### Heal skills ######
class Heal(skill):
    def __init__(self):
        super().__init__(name="Heal", physical=False, power=5, cooldown=3)
        self.SkillType = SkillType.HEAL
    
    def use(self, user):
        if not self.is_available(user.name):
            print(f"{self.name} is on cooldown for {self.current_cooldown} more turns.")
            return False

        self.start_cooldown()
        return self.power

###### Utility skills ######
class Overdrive(skill):
    def __init__(self):
        super().__init__(name="Overdrive", physical=False, power=0, cooldown=5)
        self.SkillType = SkillType.UTILITY
        self.duration = 3

    def use_utility(self, user, target):
        print(f"{user.name} is in Overdrive! Speed and power increased for 3 turns!")
        
        user.speed *= 1.5
        for ability in user.abilities:
            if ability.SkillType == SkillType.ATTACK:
                ability.power *= 1.5
    
    def end_utility(self, user):
        print(f"{user.name}'s Overdrive has ended. Speed and power returned to normal.")

        user.speed /= 1.5
        for ability in user.abilities:
            if ability.SkillType == SkillType.ATTACK:
                ability.power /= 1.5
        
    def reduce_cooldown(self, user_monster):
        super().reduce_cooldown(user_monster)
        if self.current_cooldown == self.cooldown - self.duration:
            self.end_utility(user_monster)