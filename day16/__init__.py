import math
from abc import ABC, abstractmethod


def parse(line):
    return parse_binary(to_binary(line), 0)


def to_binary(line):
    return "".join(bin(int(c, 16))[2:].zfill(4) for c in line)


def parse_binary(binary, pos):
    type_id = int(binary[pos + 3:pos + 6], 2)
    if type_id == 4:
        return LiteralValue(binary, pos)
    return Operator(binary, pos)


class Packet(ABC):
    def __init__(self, binary, start):
        self.version = int(binary[start:start + 3], 2)
        self.type_id = int(binary[start + 3:start + 6], 2)

    @abstractmethod
    def version_sum(self):
        pass

    @abstractmethod
    def get_value(self):
        pass


class LiteralValue(Packet):
    def __init__(self, binary, start):
        super().__init__(binary, start)

        pos = start + 6
        groups = []
        keep_reading = True
        while keep_reading:
            group = binary[pos:pos + 5]
            pos += 5
            groups.append(group[1:])
            if group[0] == "0":
                keep_reading = False
        self.end = pos
        self.value = int("".join(groups), 2)

    def version_sum(self):
        return self.version

    def get_value(self):
        return self.value

    def __repr__(self):
        return "LiteralValue[version=%d, value=%d]" % (self.version, self.value)


class Operator(Packet):
    def __init__(self, binary, start):
        super().__init__(binary, start)
        self.subpackets = []

        pos = start + 6
        length_type_id = int(binary[pos])
        pos += 1

        if length_type_id == 0:
            subpackets_length = int(binary[pos:pos + 15], 2)
            pos += 15
            subpackets_end = pos + subpackets_length
            while pos < subpackets_end:
                subpacket = parse_binary(binary, pos)
                self.subpackets.append(subpacket)
                pos = subpacket.end

        else:
            num_subpackets = int(binary[pos:pos + 11], 2)
            pos += 11
            for _ in range(num_subpackets):
                subpacket = parse_binary(binary, pos)
                self.subpackets.append(subpacket)
                pos = subpacket.end

        self.end = pos

    def version_sum(self):
        return self.version + sum(p.version_sum() for p in self.subpackets)

    def get_value(self):
        # pylint: disable=too-many-return-statements

        subpacket_values = [p.get_value() for p in self.subpackets]

        if self.type_id == 0:
            return sum(subpacket_values)

        if self.type_id == 1:
            return math.prod(subpacket_values)

        if self.type_id == 2:
            return min(subpacket_values)

        if self.type_id == 3:
            return max(subpacket_values)

        if self.type_id == 5:
            return 1 if subpacket_values[0] > subpacket_values[1] else 0

        if self.type_id == 6:
            return 1 if subpacket_values[0] < subpacket_values[1] else 0

        if self.type_id == 7:
            return 1 if subpacket_values[0] == subpacket_values[1] else 0

        raise Exception("Unknown type %d" % self.type_id)

    def __repr__(self):
        return "Operator[version=%d, subpackets=%s]" % (self.version, self.subpackets)
