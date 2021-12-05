import re
from itertools import chain

import utils


def part_1_answer(lines):
    drawn_numbers, boards = parse_lines(lines)

    for i in range(len(drawn_numbers)):  # pylint: disable=consider-using-enumerate
        numbers_drawn_so_far = set(drawn_numbers[:i + 1])
        for board in boards:
            if board_has_won(board, numbers_drawn_so_far):
                return final_score(board, numbers_drawn_so_far, drawn_numbers[i])

    return None


def part_2_answer(lines):
    drawn_numbers, boards = parse_lines(lines)

    winners = set()
    last_winner = None
    last_winner_drawn_numbers = None

    for i in range(len(drawn_numbers)):
        numbers_drawn_so_far = set(drawn_numbers[:i + 1])
        for board_num, board in enumerate(boards):
            if (board_num not in winners) and board_has_won(board, numbers_drawn_so_far):
                winners.add(board_num)
                last_winner = board
                last_winner_drawn_numbers = drawn_numbers[:i + 1]

    return final_score(last_winner, last_winner_drawn_numbers, last_winner_drawn_numbers[-1])


def board_has_won(board, numbers_drawn_so_far):
    for y in range(0, 5):
        row = set(board[y])
        if row.issubset(numbers_drawn_so_far):
            return True

    for x in range(0, 5):
        column = set(board[y][x] for y in range(0, 5))
        if column.issubset(numbers_drawn_so_far):
            return True

    return False


def final_score(board, drawn_numbers, last_drawn_number):
    all_nums_on_board = set(chain(*board))
    unmarked = all_nums_on_board.difference(drawn_numbers)
    return sum(unmarked) * last_drawn_number


def parse_lines(lines):
    drawn_numbers = [int(n) for n in lines[0].split(",")]

    boards = lines[2:]
    boards = utils.group_lines(boards)
    boards = [[re.findall(r'\d+', row) for row in board] for board in boards]
    boards = [[[int(n) for n in row] for row in board] for board in boards]

    return drawn_numbers, boards
