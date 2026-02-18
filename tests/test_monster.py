import monster
import unittest

class TestMonster(unittest.TestCase):

    def setUp(self):
        print("Setting up tests for Monster class...")
        self.dragon = monster.Dragon()
        self.golem = monster.Golem()
    
    def test_print_summary(self):
        print("Testing print summary function...")
        self.dragon.print_summary()  # This should print the summary of the dragon

    def test_get_ability(self):
        print("Testing get ability function...")
        ability = self.dragon.get_ability(0)  # This should return the first ability
        self.assertIsNotNone(ability)
        self.assertEqual(ability.name, self.dragon.abilities[0].name)

        ability = self.dragon.get_ability(1)  # This should return the second ability
        self.assertIsNotNone(ability)
        self.assertEqual(ability.name, self.dragon.abilities[1].name)

        ability = self.dragon.get_ability(2)  # This should return the third ability
        self.assertIsNotNone(ability)
        self.assertEqual(ability.name, self.dragon.abilities[2].name)

        ability = self.dragon.get_ability(4)  # This should return None since there are only 4 abilities
        self.assertIsNone(ability)
    
    def test_heal(self):
        print("Testing heal function...")

        # Test healing a monster and ensuring it does not exceed base health
        self.dragon.heal(1) # This should not change health since it's already at base health
        self.assertEqual(self.dragon.health, self.dragon.base_health)

        self.dragon.health = 1
        self.dragon.heal(3) # This should heal 3 hp, resulting in 4 hp
        self.assertEqual(self.dragon.health, 4)

        self.dragon.health = self.dragon.base_health
        self.dragon.heal(1)  # This should not exceed base health
        self.assertEqual(self.dragon.health, self.dragon.base_health)

    def test_full_heal(self):
        print("Testing full heal function...")

        # Test the full heal function to ensure it restores health to base health
        self.dragon.full_heal() # Heal should fail and print a different message
        self.assertEqual(self.dragon.health, self.dragon.base_health)

        self.dragon.health = 1
        self.dragon.full_heal()
        self.assertEqual(self.dragon.health, self.dragon.base_health)

    def test_revive(self):
        print("Testing revive function...")

        # Test the revive function to ensure it revives a defeated monster
        self.dragon.health = 0
        self.dragon.alive = False
        self.dragon.revive()

        self.assertTrue(self.dragon.alive)
        self.assertEqual(self.dragon.health, 1)  # Revive should set health to 1

        self.dragon.health = self.dragon.base_health  # Reset health for further tests
    
    def test_full_revive(self):
        print("Testing full revive function...")

        # Test the full revive function to ensure it fully revives a defeated monster
        self.dragon.health = 0
        self.dragon.alive = False
        self.dragon.full_revive()

        self.assertTrue(self.dragon.alive)
        self.assertEqual(self.dragon.health, self.dragon.base_health)  # Full revive should set health to base health

        # Ensure dragon's stats are recovered in case of failure 
        # This is to not interfere with later tests
        self.dragon.health = self.dragon.base_health
        self.dragon.alive = True

    def test_take_damage(self):
        print("Testing take damage function...")

        # Test taking damage and checking if the monster is still alive
        self.dragon.take_damage(5)
        self.assertEqual(self.dragon.health, 10)
        self.assertTrue(self.dragon.alive)

        # Test taking damage that would reduce health to zero or below
        self.dragon.take_damage(10)
        self.assertEqual(self.dragon.health, 0)
        self.assertFalse(self.dragon.alive)
    
        self.dragon.health = self.dragon.base_health  # Reset health for further tests