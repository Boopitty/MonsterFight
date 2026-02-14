import battle_funcs
import unittest
from unittest.mock import patch
from monster import Dragon, Golem, Unicorn, Automaton, Slime, Phoenix


class TestBattleFuncs(unittest.TestCase):
    def setUp(self):
        print("Setting up tests for Battle Functions...")
        self.dragon = Dragon()
        self.golem = Golem()
        self.unicorn = Unicorn()
        self.monster_team = [self.dragon, self.golem, self.unicorn]
        self.active_monster = self.monster_team[0]
    
    def test_print_monster_base_stats(self):
        print("Testing print monster base stats function...")
        battle_funcs.print_monster_base_stats(self.dragon)  # This should print the base stats of the dragon
        
    def test_print_monster_current_stats(self):
        print("Testing print monster current stats function...")
        # Change the dragon's stats to test current stats printing
        self.dragon.health = 10
        self.dragon.durability = 3
        self.dragon.spirit = 12
        self.dragon.speed = 1
        battle_funcs.print_monster_current_stats(self.dragon)  # This should print the current stats of the dragon

        # Restore the dragon's stats for further tests
        self.dragon.health = self.dragon.base_health
        self.dragon.durability = self.dragon.base_durability
        self.dragon.spirit = self.dragon.base_spirit
        self.dragon.speed = self.dragon.base_speed

    def test_player_switch_active_monster(self):
        print("Testing player switch active monster function...")
        # Simulate user input for switching active monster
        with patch('builtins.input', side_effect=['2']):
            new_active = battle_funcs.player_switch_active_monster(self.active_monster, self.monster_team)
            self.assertEqual(new_active, self.golem)

        # Test switching to a dead monster
        self.golem.alive = False  # Update alive status
        with patch('builtins.input', side_effect=['2', '3']):
            new_active = battle_funcs.player_switch_active_monster(self.active_monster, self.monster_team)
            self.assertEqual(new_active, self.unicorn)
        self.golem.alive = True  # Reset alive status for further tests
    
    def test_enemy_switch_active_monster(self):
        print("Testing enemy switch active monster function...")
        new_active = battle_funcs.enemy_switch_active_monster(self.active_monster, self.monster_team)
        self.assertIn(new_active, self.monster_team)
        self.assertNotEqual(new_active, self.active_monster)