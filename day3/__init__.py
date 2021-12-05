def part_1_answer(report):
    transposed = [[int(number[i]) for number in report] for i in range(0, len(report[0]))]

    most_common_bits = [most_common_bit(bits) for bits in transposed]
    gamma_rate = int("".join(str(bit) for bit in most_common_bits), 2)

    least_common_bits = [least_common_bit(bits) for bits in transposed]
    epsilon_rate = int("".join(str(bit) for bit in least_common_bits), 2)

    return gamma_rate * epsilon_rate


def part_2_answer(report):
    oxygen_generator_rating = find_part_2_value(report, most_common_bit)
    co2_scrubber_rating = find_part_2_value(report, least_common_bit)
    return oxygen_generator_rating * co2_scrubber_rating


def find_part_2_value(report, to_keep_fn):
    remaining = report
    index = 0
    while len(remaining) > 1:
        bits = [int(number[index]) for number in remaining]
        value_to_keep = to_keep_fn(bits)
        remaining = [number for number in remaining if int(number[index]) == value_to_keep]
        index += 1
    return int(remaining[0], 2)


def most_common_bit(bits):
    counts = [bits.count(0), bits.count(1)]
    return 1 if (counts[1] >= counts[0]) else 0


def least_common_bit(bits):
    counts = [bits.count(0), bits.count(1)]
    return 0 if (counts[0] <= counts[1]) else 1
