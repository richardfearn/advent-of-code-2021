from collections import namedtuple
from itertools import cycle


def part_1_answer(lines):
    positions = parse_input(lines)
    scores = [0, 0]

    die = Part1Die()

    for player in cycle(range(2)):

        roll_total = sum(die.roll() for _ in range(3))

        positions[player] = new_position(positions[player], roll_total)
        scores[player] += positions[player]

        if scores[player] >= 1000:
            return min(scores) * die.get_total_rolls()

    return None


class Part1Die:

    def __init__(self):
        self.next = 1
        self.total_rolls = 0

    def roll(self):
        result = self.next
        self.next = 1 if (self.next == 100) else (self.next + 1)
        self.total_rolls += 1
        return result

    def get_total_rolls(self):
        return self.total_rolls


def new_position(old_position, roll):
    return ((old_position - 1 + roll) % 10) + 1


DiracDieRoll = namedtuple("DiracDieRoll", ["total", "count"])

PART_2_ROLLS = [DiracDieRoll(total, count) for (total, count) in [
    (3, 1),
    (4, 3),
    (5, 6),
    (6, 7),
    (7, 6),
    (8, 3),
    (9, 1),
]]

PART_2_NEW_POSITIONS = {
    start_pos: {
        roll: new_position(start_pos, roll) for roll in range(3, 10)
    } for start_pos in range(1, 11)
}


def part_2_answer(lines):
    starting_positions = parse_input(lines)
    wins = [0, 0]
    player_turn(positions=starting_positions, scores=[0, 0], wins=wins, player=0, count=1)
    return max(wins)


def player_turn(positions, scores, wins, player, count):
    for roll in PART_2_ROLLS:
        new_count = count * roll.count
        player_roll(positions, scores, wins, player, roll.total, new_count)


def player_roll(positions, scores, wins, player, roll_total, count):
    # pylint: disable=too-many-arguments
    positions = positions[::]
    scores = scores[::]

    positions[player] = PART_2_NEW_POSITIONS[positions[player]][roll_total]
    scores[player] += positions[player]

    if scores[player] >= 21:
        wins[player] += count
    else:
        other_player = 1 - player
        player_turn(positions, scores, wins, other_player, count)


def parse_input(lines):
    return [int(line.split(" ")[-1]) for line in lines]
