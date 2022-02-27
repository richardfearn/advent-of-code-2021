import itertools
from collections import namedtuple
from math import prod

Cuboid = namedtuple("Cuboid", ["x", "y", "z"])
RebootStep = namedtuple("RebootStep", ["state", "cuboid"])


def part_1_answer(lines):
    steps = parse_input(lines)

    on_cubes = set()
    for step in steps:
        for x in initialization_region_subset(step.cuboid.x):
            for y in initialization_region_subset(step.cuboid.y):
                for z in initialization_region_subset(step.cuboid.z):
                    cube = (x, y, z)
                    if step.state == "on":
                        on_cubes.add(cube)
                    else:
                        on_cubes.discard(cube)

    return len(on_cubes)


def initialization_region_subset(val_range):
    low = max(val_range.start, -50)
    high = min(val_range.stop, 51)
    return range(low, high)


def part_2_answer(lines):
    steps = parse_input(lines)

    on_cuboids = set()

    for step in steps:
        new_on_cuboids = set()

        for on_cuboid in on_cuboids:

            if cuboids_intersect(on_cuboid, step.cuboid):

                # Add the sub-cuboids that were already on, but not the ones that overlap with the
                # cuboid beingturned on/off in this step.

                # If this step is turning a cuboid off, this has the effect of turning off any
                # affected sub-cuboids.

                # If the step is turning a cuboid on, we turn that entire cuboid on in one go
                # later, so overlapping sub-cuboids do not need to be added here.

                for sub_cuboid in sub_cuboids(on_cuboid, step.cuboid):
                    if cuboids_intersect(sub_cuboid, on_cuboid) \
                            and not cuboids_intersect(sub_cuboid, step.cuboid):
                        new_on_cuboids.add(sub_cuboid)

            else:
                # Existing cuboid that was turned on is not affected by the cuboid now being
                # turned on/off, so leave it on
                new_on_cuboids.add(on_cuboid)

        if step.state == "on":
            new_on_cuboids.add(step.cuboid)

        on_cuboids = new_on_cuboids

    return sum(volume(cuboid) for cuboid in on_cuboids)


def cuboids_intersect(cuboid1, cuboid2):
    return \
        ranges_overlap(cuboid1.x, cuboid2.x) and \
        ranges_overlap(cuboid1.y, cuboid2.y) and \
        ranges_overlap(cuboid1.z, cuboid2.z)


def ranges_overlap(range1, range2):
    return (range1.start in range2) or (range2.start in range1)


def sub_cuboids(cuboid1, cuboid2):
    """
    Take the cuboid occupied by cuboid1/cuboid2, and split it into smaller cuboids that are either
    (a) empty, or (b) fully occupied by one of those cuboids, (c) fully occupied by both of them.

    e.g. two identical cuboids - will yield 1 sub-cuboid.

    e.g. one large cuboid with a smaller cuboid in one of its corners - will yield 8 sub-cuboids.

    e.g. one large cuboid with a smaller cuboid contained within it, not touching the larger one
    on any of its 6 faces - will yield 27 sub-cuboids.
    """
    all_axis_ranges = [axis_ranges(cuboid1, cuboid2, axis) for axis in range(3)]
    for x, y, z in itertools.product(*all_axis_ranges):
        yield Cuboid(x, y, z)


def axis_ranges(cuboid1, cuboid2, axis):
    # will be 2/3/4 points, depending on how the cuboids overlap
    transition_points = sorted({
        cuboid1[axis].start, cuboid1[axis].stop,
        cuboid2[axis].start, cuboid2[axis].stop})

    # will be 1/2/3 ranges, depending on how the cuboids overlap
    return [range(*pair) for pair in pairwise(transition_points)]


def pairwise(values):
    """
    Like https://docs.python.org/3/library/itertools.html#itertools.pairwise
    """
    for i in range(len(values) - 1):
        yield values[i], values[i + 1]


def volume(cuboid):
    return prod((axis.stop - axis.start) for axis in cuboid)


def parse_input(lines):
    return [parse_line(line) for line in lines]


def parse_line(line):
    state, xyz = line.split(" ")
    xyz = xyz.split(",")
    xyz = [s[2:].split("..") for s in xyz]
    xyz = [[int(n) for n in val] for val in xyz]
    xyz = [range(val[0], val[1] + 1) for val in xyz]
    xyz = Cuboid(*xyz)
    return RebootStep(state, xyz)
