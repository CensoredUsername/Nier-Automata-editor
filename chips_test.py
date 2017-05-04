import unittest
import chips


class TestChipsMapMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chips_map = chips.ChipsMap()

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
        exp_gain_up = self.chips_map[
            b"\xC7\x00\x00\x00\x40\x0C\x00\x00\x10\x00\x00\x00"]
        self.assertEqual(exp_gain_up, "EXP Gain Up")
        hud_mini_map = self.chips_map[
            b"\x27\x01\x00\x00\x11\x0D\x00\x00\x32\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00"]
        self.assertEqual(hud_mini_map, "HUD: Mini-map")

    def test_get_name_from_derived_bytes(self):
        overclock8 = self.chips_map[
            b"\xE1\x00\x00\x00\x7E\x0C\x00\x00\x16\x00\x00\x00"]
        self.assertEqual(overclock8, "Overclock +8")


class TestChipsRecordMethods(unittest.TestCase):

    def test_create_from_name(self):
        actual = chips.ChipsRecord.from_name("Drop Rate Up +6")
        self.assertEqual(actual.name, "Drop Rate Up +6")
        self.assertEqual(actual.level, 6)
        self.assertEqual(actual.type_id, 0x0F)
        self.assertEqual(actual.chip_id_1, 0x00C4)
        self.assertEqual(actual.chip_id_2, 0x0C3D)
        self.assertEqual(actual.size, chips.LEVEL_MINIMUMSIZE[6])
        self.assertEqual(actual.offset_a, -1)
        self.assertEqual(actual.offset_b, -1)
        self.assertEqual(actual.offset_b, -1)

    def test_unpack(self):
        actual = chips.ChipsRecord.unpack(
            b"\x27\x00\x00\x00\x4C\x0C\x00\x00\x11\x00\x00\x00\x03\x00\x00\x00\x10\x00\x00\x00\x05\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00")
        self.assertEqual(actual.name, "Shock Wave +3")
        self.assertEqual(actual.chip_id_1, 0x27)
        self.assertEqual(actual.chip_id_2, 0x0C4C)
        self.assertEqual(actual.type_id, 0x11)
        self.assertEqual(actual.level, 3)
        self.assertEqual(actual.size, 16)
        self.assertEqual(actual.offset_a, 0x05)
        self.assertEqual(actual.offset_b, -1)
        self.assertEqual(actual.offset_c, -1)

    def test_pack(self):
        actual = chips.ChipsRecord(
            "Damage Absorb +1", 0x92, 0x0C5C, 0x13, 1, 4, -1, 0x10, -1).pack()
        self.assertEqual(actual, b"\x92\x00\x00\x00\x5C\x0C\x00\x00\x13\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\xFF\xFF\xFF\xFF\x10\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00")


class TestChipsRecordManagerMethods(unittest.TestCase):

    @classmethod
    def setUp(cls):
        with open("./SlotData_0.dat","rb") as f:
            data = f.read()
        cls.target = chips.ChipsRecordManager(buf=data)

    def test_get_chip_at(self):
        actual = self.target.get_chip_at(0)
        self.assertEqual(actual.name, "OS Chip")

        with self.assertRaises(IndexError):
            self.target.get_chip_at(400)

    def test_export(self):
        actual = self.target.export()
        self.assertEqual(actual[:12], b"\x22\x01\x00\x00\x0A\x0D\x00\x00\x2A\x00\x00\x00")
        self.assertEqual(len(actual), chips.ChipsRecordManager.SAVE_DATA_CHIPS_SIZE)
    
    def test_set_chip_at(self):
        record = chips.ChipsRecord.from_name("Auto-use Item +4")
        self.target.set_chip_at(5, record)
        actual = self.target.export()
        self.assertEqual(actual[48*5:48*5+20], b"\xEF\x00\x00\x00\xB0\x0C\x00\x00\x1B\x00\x00\x00\x04\x00\x00\x00\x09\x00\x00\x00")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestChipsMapMethods))
    suite.addTests(loader.loadTestsFromTestCase(TestChipsRecordMethods))
    suite.addTests(loader.loadTestsFromTestCase(TestChipsRecordManagerMethods))
    unittest.TextTestRunner(verbosity=2).run(suite)
