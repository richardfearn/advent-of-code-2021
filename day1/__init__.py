def part_1_answer(depths):
    depths = [int(d) for d in depths]
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1
    return increases


def part_2_answer(depths):
    depths = [int(d) for d in depths]
    increases = 0
    for i in range(3, len(depths)):
        sum1 = depths[i - 3] + depths[i - 2] + depths[i - 1]
        sum2 = depths[i - 2] + depths[i - 1] + depths[i]
        if sum2 > sum1:
            increases += 1
    return increases
