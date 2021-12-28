import heapq

INFINITY = 99999999999


def total_risk(lines, expand=False):
    grid = [[int(n) for n in line] for line in lines]

    if expand:
        grid = expand_grid(grid)

    return find_total_risk(grid)


def find_total_risk(grid):
    width = len(grid[0])
    height = len(grid)

    dist = [[INFINITY for _ in range(width)] for _ in range(height)]

    dist[0][0] = 0

    node_heap = []
    heapq.heappush(node_heap, (0, (0, 0)))

    while len(node_heap) > 0:
        _, (uy, ux) = heapq.heappop(node_heap)
        for xn, yn in ((ux + 1, uy), (ux, uy + 1), (ux - 1, uy), (ux, uy - 1)):
            if (0 <= xn < width) and (0 <= yn < height):
                alt = dist[uy][ux] + grid[yn][xn]
                if alt < dist[yn][xn]:
                    dist[yn][xn] = alt
                    heapq.heappush(node_heap, (alt, (yn, xn)))

    return dist[height - 1][width - 1]


def expand_grid(grid):
    width = len(grid[0])
    height = len(grid)

    new_grid = []
    for ty in range(5):
        for y in range(height):
            new_grid.append([])
            for tx in range(5):
                for x in range(width):
                    new_grid[-1].append((grid[y][x] + tx + ty - 1) % 9 + 1)

    return new_grid
