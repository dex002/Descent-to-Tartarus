"""Unit tests to test functionality of project.
"""

import unittest

from module import calculate_damage, Aphros, Aspirda, Doros, Lusios, Enemy
##
##

class TestCalculateDamage(unittest.TestCase):

    def test_calculate_damage(self):
        attacker = Aphros("attacker")
        target = Aspirda("target")
        damage = calculate_damage(attacker, target)
        self.assertEqual(damage, (attacker.damage - target.defense))

    def test_damage_minimum_zero(self):
        attacker = Aphros("attacker")
        target = Aspirda("target")
        target.defense = 100
        damage = calculate_damage(attacker, target)
        self.assertTrue(damage == 0)

class TestHeroSkills(unittest.TestCase):

    def test_alluring_kiss_heal(self):
        aphros = Aphros("healer")
        target = Aphros("target")
        starting_hp = target.hp
        aphros.alluring_kiss(target)
        self.assertEqual(target.hp, (starting_hp + 2))

    def test_bulwark_buff(self):
        aspirda = Aspirda("buffer")
        starting_def = aspirda.defense
        aspirda.bulwark()
        self.assertEqual(aspirda.defense, (starting_def + 3))

    def test_deathbound_damage(self):
        doros = Doros("attacker")
        target = Aspirda("target")
        starting_hp = target.hp
        doros.deathbound(target)
        self.assertEqual(target.hp, (starting_hp - ((doros.damage * 3) - target.defense)))

    def test_sly_heal(self):
        doros = Doros("attacker")
        target = Aspirda("target")
        starting_hp = doros.hp
        doros.sly(target)
        stolen = doros.damage - target.defense
        if stolen < 0:
            stolen = 0
        self.assertEqual(doros.hp, (starting_hp + stolen))
        

    

                 
    