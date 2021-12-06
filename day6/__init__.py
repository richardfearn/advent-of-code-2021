def simulation(fish, days):
    fish = [int(n) for n in fish.split(",")]
    counts = [fish.count(n) for n in range(9)]

    for _ in range(days):
        counts = counts[1:] + counts[:1]
        counts[6] += counts[-1]

    return sum(counts)
