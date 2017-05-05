import struct
from io import BytesIO

COMMON_CHIPS = {
    "Weapon Attack Up": b"\x00\x00\x00\x00\xB9\x0B\x00\x00\x01\x00\x00\x00",
    "Down-Attack Up": b"\x09\x00\x00\x00\xC2\x0B\x00\x00\x02\x00\x00\x00",
    "Critical Up": b"\x12\x00\x00\x00\xCB\x0B\x00\x00\x03\x00\x00\x00",
    "Ranged Attack Up": b"\x1B\x00\x00\x00\xD4\x0B\x00\x00\x04\x00\x00\x00",
    "Fast Cooldown": b"\xA3\x00\x00\x00\xDD\x0B\x00\x00\x05\x00\x00\x00",
    "Melee Defence Up": b"\x49\x00\x00\x00\xE6\x0B\x00\x00\x06\x00\x00\x00",
    "Ranged Defence Up": b"\x52\x00\x00\x00\xEF\x0B\x00\x00\x07\x00\x00\x00",
    "Anti Chain Damage": b"\x5B\x00\x00\x00\xF8\x0B\x00\x00\x08\x00\x00\x00",
    "Max HP Up": b"\x6D\x00\x00\x00\x01\x0C\x00\x00\x09\x00\x00\x00",
    "Offensive Heal": b"\x76\x00\x00\x00\x0A\x0C\x00\x00\x0A\x00\x00\x00",
    "Deadly Heal": b"\x7F\x00\x00\x00\x13\x0C\x00\x00\x0B\x00\x00\x00",
    "Auto-Heal": b"\x88\x00\x00\x00\x1C\x0C\x00\x00\x0C\x00\x00\x00",
    "Evade Range Up": b"\xAC\x00\x00\x00\x25\x0C\x00\x00\x0D\x00\x00\x00",
    "Moving Speed Up": b"\xB5\x00\x00\x00\x2E\x0C\x00\x00\x0E\x00\x00\x00",
    "Drop Rate Up": b"\xBE\x00\x00\x00\x37\x0C\x00\x00\x0F\x00\x00\x00",
    "EXP Gain Up": b"\xC7\x00\x00\x00\x40\x0C\x00\x00\x10\x00\x00\x00",
    "Shock Wave": b"\x24\x00\x00\x00\x49\x0C\x00\x00\x11\x00\x00\x00",
    "Last Stand": b"\x2D\x00\x00\x00\x52\x0C\x00\x00\x12\x00\x00\x00",
    "Damage Absorb": b"\x91\x00\x00\x00\x5B\x0C\x00\x00\x13\x00\x00\x00",
    "Vengeance": b"\xD0\x00\x00\x00\x64\x0C\x00\x00\x14\x00\x00\x00",
    "Reset": b"\x9A\x00\x00\x00\x6D\x0C\x00\x00\x15\x00\x00\x00",
    "Overclock": b"\xD9\x00\x00\x00\x76\x0C\x00\x00\x16\x00\x00\x00",
    "Resilience": b"\x64\x00\x00\x00\x7F\x0C\x00\x00\x17\x00\x00\x00",
    "Counter": b"\x36\x00\x00\x00\x91\x0C\x00\x00\x18\x00\x00\x00",
    "Taunt Up": b"\xE2\x00\x00\x00\x9A\x0C\x00\x00\x19\x00\x00\x00",
    "Charge Attack": b"\x3F\x00\x00\x00\xA3\x0C\x00\x00\x1A\x00\x00\x00",
    "Auto-use Item": b"\xEB\x00\x00\x00\xAC\x0C\x00\x00\x1B\x00\x00\x00",
    "Hijack Boost": b"\xFD\x00\x00\x00\xBE\x0C\x00\x00\x1D\x00\x00\x00",
    "Stun": b"\x06\x01\x00\x00\xD9\x0C\x00\x00\x1E\x00\x00\x00",
    "Combust": b"\x0F\x01\x00\x00\xE2\x0C\x00\x00\x1F\x00\x00\x00",
    "Heal Drops Up": b"\x18\x01\x00\x00\xFD\x0C\x00\x00\x22\x00\x00\x00"
}

LEVEL_MINIMUMSIZE = {
    0: 4,
    1: 5,
    2: 6,
    3: 7,
    4: 9,
    5: 11,
    6: 14,
    7: 17,
    8: 21
}

UNIQUE_CHIPS = {
    "Item Scan": b"\xF5\x00\x00\x00\x88\x0C\x00\x00\x23\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00",
    "Death Rattle": b"\x21\x01\x00\x00\x06\x0D\x00\x00\x26\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00",
    "HUD: HP Gauge": b"\x23\x01\x00\x00\x07\x0D\x00\x00\x27\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00",
    "HUD: Sound Waves": b"\x2D\x01\x00\x00\x08\x0D\x00\x00\x28\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00",
    "HUD: Enemy Data": b"\x26\x01\x00\x00\x09\x0D\x00\x00\x29\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00",
    "OS Chip": b"\x22\x01\x00\x00\x0A\x0D\x00\x00\x2A\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00",
    "Evasive System": b"\xF6\x00\x00\x00\x0B\x0D\x00\x00\x2C\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00",
    "Continuous Combo": b"\x48\x00\x00\x00\x0C\x0D\x00\x00\x2D\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00",
    "Bullet Detonation": b"\xF7\x00\x00\x00\x0D\x0D\x00\x00\x2E\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00",
    "Auto-collect Items": b"\xF4\x00\x00\x00\x0E\x0D\x00\x00\x2F\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00",
    "HUD: Skill Gauge": b"\x25\x01\x00\x00\x0F\x0D\x00\x00\x30\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00",
    "HUD: Text Log": b"\x29\x01\x00\x00\x10\x0D\x00\x00\x31\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00",
    "HUD: Mini-map": b"\x27\x01\x00\x00\x11\x0D\x00\x00\x32\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00",
    "HUD: EXP Gauge": b"\x24\x01\x00\x00\x12\x0D\x00\x00\x33\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00",
    "HUD: Save Points": b"\x2A\x01\x00\x00\x13\x0D\x00\x00\x34\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00",
    "HUD: Damage Values": b"\x2C\x01\x00\x00\x14\x0D\x00\x00\x35\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00",
    "HUD: Objectives": b"\x28\x01\x00\x00\x15\x0D\x00\x00\x36\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00",
    "HUD: Control": b"\x2E\x01\x00\x00\x16\x0D\x00\x00\x37\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00",
    "HUD: Fishing Spots": b"\x2B\x01\x00\x00\x19\x0D\x00\x00\x3A\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00",
    "Auto-Attack": b"\xF8\x00\x00\x00\x1A\x0D\x00\x00\x3B\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00",
    "Auto-Fire": b"\xF9\x00\x00\x00\x1B\x0D\x00\x00\x3C\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00",
    "Auto-Evade": b"\xFA\x00\x00\x00\x1C\x0D\x00\x00\x3D\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00",
    "Auto-Program": b"\xFB\x00\x00\x00\x1D\x0D\x00\x00\x3E\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00",
    "Auto-Weapon Switch": b"\xFC\x00\x00\x00\x1E\x0D\x00\x00\x3F\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00",
}


class ChipsMap(object):
    def __init__(self):
        self.name_to_bytes_map = dict()
        for k, v in COMMON_CHIPS.items():
            self.name_to_bytes_map[k] = v + struct.pack("<2i", 0, 4)
            r = struct.unpack("<3i", v)
            for i in range(1, 9):
                nv = struct.pack("<3i", r[0] + i, r[1] + i, r[2])
                self.name_to_bytes_map[k + " +" +
                                       str(i)] = nv + struct.pack("<2i", i, LEVEL_MINIMUMSIZE[i])
        for k, v in UNIQUE_CHIPS.items():
            self.name_to_bytes_map[k] = v

        self.bytes_to_name_map = dict()
        for k, v in COMMON_CHIPS.items():
            self.bytes_to_name_map[v] = k
            r = struct.unpack("<3i", v)
            for i in range(1, 9):
                nv = struct.pack("<3i", r[0] + i, r[1] + i, r[2])
                self.bytes_to_name_map[nv] = k + " +" + str(i)
        for k, v in UNIQUE_CHIPS.items():
            self.bytes_to_name_map[v[:12]] = k

    def __getitem__(self, key):
        if isinstance(key, bytes) or isinstance(key, bytearray):
            return self.bytes_to_name_map.get(bytes(key)[:12], "Invalid Chip")
        elif isinstance(key, str):
            return self.name_to_bytes_map.get(key, b"\xFF" * 44 + b"\x00" * 4)


class ChipsRecord(object):
    """Represent a chip record"""
    CHIPS_MAP = ChipsMap()
    AVAILABLE_CHIPS = tuple(CHIPS_MAP.name_to_bytes_map.keys())
    EMPTY_RECORD = -1

    def __init__(self, name, chip_id_1, chip_id_2, type_id, level, size, offset_a=-1, offset_b=-1, offset_c=-1):
        self.name = name
        self.chip_id_1 = chip_id_1
        self.chip_id_2 = chip_id_2
        self.type_id = type_id
        self.level = level
        self.size = size
        self.offset_a = offset_a
        self.offset_b = offset_b
        self.offset_c = offset_c

    def __str__(self):
        return "<ChipsRecord name:{0} level:{1} size:{2} offset:{3:X} {4:X} {5:X}>".format(self.name, self.level,
                                                                                           self.size, self.offset_a,
                                                                                           self.offset_b, self.offset_c)

    def pack(self):
        """Convert to bytes"""
        return struct.pack("<12i", self.chip_id_1, self.chip_id_2, self.type_id, self.level, self.size, self.offset_a,
                           self.offset_b, self.offset_c, -1, -1, -1, 0)

    @staticmethod
    def unpack(bs):
        """ Convert from bytes """
        name = ChipsRecord.CHIPS_MAP[bs]
        record = struct.unpack("<12i", bs)
        if record[0] == record[1] == record[2] == -1:
            return ChipsRecord.EMPTY_RECORD
        return ChipsRecord(name, *record[:-4])

    @classmethod
    def from_name(cls, name):
        bs = cls.CHIPS_MAP[name]
        record = struct.unpack("<5i", bs)
        return cls(name, *record)


class ChipsRecordManager(object):
    SAVE_DATA_CHIPS_OFFSET = 0x324BC
    SAVE_DATA_CHIPS_OFFSET_END = 0x35CFC
    SAVE_DATA_CHIPS_SIZE = SAVE_DATA_CHIPS_OFFSET_END - SAVE_DATA_CHIPS_OFFSET
    SAVE_DATA_CHIPS_COUNT = SAVE_DATA_CHIPS_SIZE // 48

    def __init__(self, buf=None):
        if buf is not None:
            self.blocks = bytearray(
                buf[ChipsRecordManager.SAVE_DATA_CHIPS_OFFSET:ChipsRecordManager.SAVE_DATA_CHIPS_OFFSET_END])
        else:
            self.blocks = bytearray(ChipsRecordManager.SAVE_DATA_CHIPS_SIZE * 48)
            self.blocks[0:48] = b"\x22\x01\x00\x00\x0A\x0D\x00\x00\x2A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    def export(self):
        return bytes(self.blocks)

    def get_all_chips(self):
        for i in range(self.SAVE_DATA_CHIPS_COUNT):
            yield ChipsRecord.unpack(self.blocks[i * 48: (i + 1) * 48])

    def get_chip_at(self, index):
        if not 0 <= index < ChipsRecordManager.SAVE_DATA_CHIPS_COUNT:
            raise IndexError
        return ChipsRecord.unpack(self.blocks[index * 48: (index + 1) * 48])

    def set_chip_at(self, index, record):
        if not 0 <= index < ChipsRecordManager.SAVE_DATA_CHIPS_COUNT:
            raise IndexError
        if record == ChipsRecord.EMPTY_RECORD:
            self.blocks[index * 48: (index + 1) * 48] = b"\xFF" * 44 + b"\x00" * 4
        else:
            self.blocks[index * 48: (index + 1) * 48] = record.pack()

    def __getitem__(self, index):
        return self.get_chip_at(index)

    def __setitem__(self, index, item):
        self.set_chip_at(index, item)
