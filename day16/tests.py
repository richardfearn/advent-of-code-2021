import unittest

import day16
import utils


class Part1Tests(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(2021, day16.parse("D2FE28").get_value())
        self.assertEqual(16, day16.parse("8A004A801A8002F478").version_sum())
        self.assertEqual(12, day16.parse("620080001611562C8802118E34").version_sum())
        self.assertEqual(23, day16.parse("C0015000016115A2E0802F182340").version_sum())
        self.assertEqual(31, day16.parse("A0016C880162017C3686B18A3D4780").version_sum())

    def test_with_input(self):
        self.assertEqual(927, day16.parse(utils.read_input(16)).version_sum())


class Part2Tests(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(3, day16.parse("C200B40A82").get_value())
        self.assertEqual(54, day16.parse("04005AC33890").get_value())
        self.assertEqual(7, day16.parse("880086C3E88112").get_value())
        self.assertEqual(9, day16.parse("CE00C43D881120").get_value())
        self.assertEqual(1, day16.parse("D8005AC2A8F0").get_value())
        self.assertEqual(0, day16.parse("F600BC2D8F").get_value())
        self.assertEqual(0, day16.parse("9C005AC2F8F0").get_value())
        self.assertEqual(1, day16.parse("9C0141080250320F1802104A08").get_value())

    def test_with_input(self):
        self.assertEqual(1725277876501, day16.parse(utils.read_input(16)).get_value())
