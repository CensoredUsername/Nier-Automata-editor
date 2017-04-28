import unittest
import Chips


class TestChipsMapMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chips_map = Chips.ChipsMap()

    def test_get_bytes_from_preset_name(self):
        fast_cooldown = self.chips_map["Fast Cooldown"]
        self.assertEqual(
            fast_cooldown, b"\xA3\x00\x00\x00\xDD\x0B\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00")
        hud_objectives = self.chips_map["HUD: Objectives"]
        self.assertEqual(
            hud_objectives, b"\x28\x01\x00\x00\x15\x0D\x00\x00\x36\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00")

    def test_get_byte_from_derived_name(self):
        moving_speed_up5 = self.chips_map["Moving Speed Up +5"]
        self.assertEqual(
            moving_speed_up5, b"\xBA\x00\x00\x00\x33\x0C\x00\x00\x0E\x00\x00\x00\x05\x00\x00\x00\x0B\x00\x00\x00")

    def test_get_name_from_preset_bytes(self):
        exp_gain_up = self.chips_map[b"\xC7\x00\x00\x00\x40\x0C\x00\x00\x10\x00\x00\x00"]
        self.assertEqual(exp_gain_up, "EXP Gain Up")
        hud_mini_map = self.chips_map[b"\x27\x01\x00\x00\x11\x0D\x00\x00\x32\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00"]
        self.assertEqual(hud_mini_map, "HUD: Mini-map")

    def test_get_name_from_derived_bytes(self):
        overclock8 = self.chips_map[b"\xE1\x00\x00\x00\x7E\x0C\x00\x00\x16\x00\x00\x00"]
        self.assertEqual(overclock8, "Overclock +8")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestChipsMapMethods)
    
    unittest.TextTestRunner(verbosity=2).run(suite)
