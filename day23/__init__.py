from collections import defaultdict
from typing import Optional

HALLWAY_POSITIONS = (0, 1, 3, 5, 7, 9, 10)

HALLWAY_ROOM_POSITIONS = {
    0: 2,
    1: 4,
    2: 6,
    3: 8
}

AMPHIPOD_ENERGIES = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}


def part_1_answer(lines):
    initial_state = parse_input_lines(lines)
    final_state = ('...........', ('AA', 'BB', 'CC', 'DD'))
    return find_min_energy(initial_state, final_state)


def part_2_answer(lines):
    initial_state = parse_input_lines(lines)
    final_state = ('...........', ('AAAA', 'BBBB', 'CCCC', 'DDDD'))
    return find_min_energy(initial_state, final_state)


def find_min_energy(initial_state, final_state):
    nodes = set()
    nodes.add(initial_state)
    edges = defaultdict(set)

    search(nodes, edges, final_state, state=initial_state)

    if final_state not in nodes:
        raise Exception("final state not in nodes")

    return shortest_path(nodes, edges, initial_state, final_state)


def search(nodes, edges, final_state, state):
    if state == final_state:
        return

    for new_state, energy_used in find_new_states(state):

        edges[state].add((new_state, energy_used))
        edges[new_state].add((state, energy_used))

        if new_state not in nodes:
            nodes.add(new_state)
            search(nodes, edges, final_state, new_state)


def find_new_states(state):
    yield from find_new_states_room_to_room(state)
    yield from find_new_states_room_to_hallway(state)
    yield from find_new_states_hallway_to_room(state)


def find_new_states_room_to_room(state):
    hallway, rooms = state

    for old_room in range(4):

        correct_for_old_room = "ABCD"[old_room]

        old_pos = find_amphipod_that_can_leave_room(rooms[old_room], correct_for_old_room)
        if old_pos is not None:

            # Found an amphipod that can move out of the room it is in
            amphipod_being_moved = rooms[old_room][old_pos]

            # See if it could move to its destination room
            dest_room = "ABCD".index(amphipod_being_moved)

            new_room_pos = find_room_position_for_amphipod(amphipod_being_moved, rooms[dest_room])
            if new_room_pos is not None:

                # See if the hallway is empty between the two rooms
                left, right = sorted([HALLWAY_ROOM_POSITIONS[old_room],
                                      HALLWAY_ROOM_POSITIONS[dest_room]])
                hallway_path = hallway[left:right + 1]

                if set(hallway_path) == {'.'}:
                    # No other amphipods in that section of the hallway, so the amphipod can move
                    yield room_to_room(state, old_room, old_pos, dest_room, new_room_pos)


def find_new_states_room_to_hallway(state):
    hallway, rooms = state

    for room in range(4):

        correct_for_room = "ABCD"[room]

        room_pos = find_amphipod_that_can_leave_room(rooms[room], correct_for_room)
        if room_pos is not None:

            # Found an amphipod that can move out of the room it is in

            # See if it could move to any of the positions in the hallway
            for hallway_pos in HALLWAY_POSITIONS:
                if hallway[hallway_pos] == ".":

                    # Found an empty position that the amphipod could move to
                    # (if no other amphipods are in the way in the hallway)

                    # Get the section of the hallway that the amphipod will move through - from
                    # where they exit the room into the hallway, to their final position in the
                    # hallway
                    left, right = sorted([HALLWAY_ROOM_POSITIONS[room], hallway_pos])
                    # Don't include the amphipod's final position
                    if left == hallway_pos:
                        left += 1
                    if right == hallway_pos:
                        right -= 1
                    hallway_path = hallway[left:right + 1]

                    if set(hallway_path) == {'.'}:
                        # No other amphipods in that section of the hallway, so the amphipod can
                        # move to that position
                        yield room_to_hallway(state, room, room_pos, hallway_pos)


def find_new_states_hallway_to_room(state):
    hallway, rooms = state

    for hallway_pos in HALLWAY_POSITIONS:
        if hallway[hallway_pos] != ".":

            # There is an amphipod in that position in the hallway
            amphipod_in_hallway = hallway[hallway_pos]

            # Find out if it there is a suitable position for it in its destination room
            dest_room = "ABCD".index(amphipod_in_hallway)
            room_pos = find_room_position_for_amphipod(amphipod_in_hallway, rooms[dest_room])
            if room_pos is not None:

                # The amphipod could move from the hallway into their destination room - if no
                # other amphipods are in the way in the hallway

                # Get the section of the hallway that the amphipod will move through -
                # from their current position in the hallway, to the position where they
                # will enter the room
                left, right = sorted([HALLWAY_ROOM_POSITIONS[dest_room], hallway_pos])
                # Don't include the amphipod's current position
                if left == hallway_pos:
                    left += 1
                if right == hallway_pos:
                    right -= 1
                hallway_path = hallway[left:right + 1]

                if set(hallway_path) == {'.'}:
                    # No other amphipods in that section of the hallway, so the amphipod can
                    # move into the room
                    yield hallway_to_room(state, hallway_pos, dest_room, room_pos)


def find_amphipod_that_can_leave_room(room, correct_for_room):
    if set(room) == {"."}:
        # Room is empty
        return None

    if set(room) == {correct_for_room}:
        # Room is fully occupied with the correct amphipods
        return None

    # Find first occupied position in the room
    room_pos = 0
    while room[room_pos] == ".":
        room_pos += 1

    if room[room_pos] != correct_for_room:
        # Amphipod is in wrong room - must move out
        return room_pos

    below = set(room[room_pos + 1:])

    if len(below) == 0:
        # Amphipod is in the correct room, with no others below it
        return None

    if below == {correct_for_room}:
        # Amphipod is in the correct room, with other correct ones under it
        return None

    # Amphipod is in the correct room, but has others below it that shouldn't be there
    return room_pos


def find_room_position_for_amphipod(amphipod, room):
    if "." not in set(room):
        # Room is full
        return None

    if set(room) == {"."}:
        # Room is empty
        return len(room) - 1

    # Find first occupied position in the room
    room_pos = 0
    while room[room_pos] == ".":
        room_pos += 1

    # If room is only occupied by amphipods of the same type,
    # amphipod can enter the room
    if set(room[room_pos:]) == {amphipod}:
        return room_pos - 1

    # Room is occupied by amphipod(s) that shouldn't be there, so the correct amphipod
    # cannot move into the room yet
    return None


def room_to_room(state, old_room, old_room_pos, new_room, new_room_pos):
    hallway, rooms = state

    amphipod_being_moved = rooms[old_room][old_room_pos]

    # Update the rooms with the amphipod moved from the old to the new position
    new_rooms = list(rooms)
    new_rooms[old_room] = list(new_rooms[old_room])
    new_rooms[new_room] = list(new_rooms[new_room])
    new_rooms[old_room][old_room_pos] = "."
    new_rooms[new_room][new_room_pos] = amphipod_being_moved
    new_rooms[old_room] = "".join(new_rooms[old_room])
    new_rooms[new_room] = "".join(new_rooms[new_room])
    new_rooms = tuple(new_rooms)

    # Find how much energy the amphipod used
    steps = \
        (old_room_pos + 1) + \
        abs(HALLWAY_ROOM_POSITIONS[old_room] - HALLWAY_ROOM_POSITIONS[new_room]) + \
        (new_room_pos + 1)
    energy_used = steps * AMPHIPOD_ENERGIES[amphipod_being_moved]

    return (hallway, new_rooms), energy_used


def room_to_hallway(state, room, room_pos, hallway_pos):
    hallway, rooms = state

    amphipod_being_moved = rooms[room][room_pos]

    # Update the hallway with the moved amphipod in its new position
    new_hallway = list(hallway)
    new_hallway[hallway_pos] = amphipod_being_moved
    new_hallway = "".join(new_hallway)

    # Update the rooms with the moved amphipod no longer in the room
    new_rooms = list(rooms)
    new_rooms[room] = list(new_rooms[room])
    new_rooms[room][room_pos] = "."
    new_rooms[room] = "".join(new_rooms[room])
    new_rooms = tuple(new_rooms)

    # Find how much energy the amphipod used
    steps = (room_pos + 1) + abs(hallway_pos - HALLWAY_ROOM_POSITIONS[room])
    energy_used = steps * AMPHIPOD_ENERGIES[amphipod_being_moved]

    return (new_hallway, new_rooms), energy_used


def hallway_to_room(state, hallway_pos, room, room_pos):
    hallway, rooms = state

    amphipod_being_moved = hallway[hallway_pos]

    # Update the hallway to remove the amphipod that has moved into the room
    new_hallway = list(hallway)
    new_hallway[hallway_pos] = "."
    new_hallway = "".join(new_hallway)

    # Update the rooms with the amphipod now in its destination room
    new_rooms = list(rooms)
    new_rooms[room] = list(new_rooms[room])
    new_rooms[room][room_pos] = amphipod_being_moved
    new_rooms[room] = "".join(new_rooms[room])
    new_rooms = tuple(new_rooms)

    # Find how much energy the amphipod used
    steps = abs(HALLWAY_ROOM_POSITIONS[room] - hallway_pos) + (room_pos + 1)
    energy_used = steps * AMPHIPOD_ENERGIES[amphipod_being_moved]

    return (new_hallway, new_rooms), energy_used


def shortest_path(nodes, edges, initial_state, final_state):
    num_to_node = list(nodes)
    node_to_num = {}
    for i, node in enumerate(num_to_node):
        node_to_num[node] = i

    new_edges = defaultdict(set)
    for source_node in edges.keys():
        for dest_node, cost in edges[source_node]:
            new_edges[node_to_num[source_node]].add((node_to_num[dest_node], cost))

    new_nodes = set(node_to_num.values())

    new_initial_state = node_to_num[initial_state]
    new_final_state = node_to_num[final_state]

    return shortest_path_2(new_nodes, new_edges, new_initial_state, new_final_state)


def shortest_path_2(nodes, edges, initial_state, final_state):
    print("%d nodes" % len(nodes))

    Q = set()
    dist: list[Optional[int]] = [None] * len(nodes)
    prev: list[Optional[int]] = [None] * len(nodes)

    for v in nodes:
        dist[v] = 99999999999999
        prev[v] = None
        Q.add(v)
    dist[initial_state] = 0

    while len(Q) > 0:

        if (len(Q) % 1000) == 0:
            print("Remaining: %d" % len(Q))

        u = None
        for q in Q:
            if (u is None) or (dist[q] < dist[u]):
                u = q

        Q.remove(u)

        for v, cost in edges[u]:
            if v in Q:
                alt = dist[u] + cost
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return dist[final_state]


def manual_part_1_example(lines):
    state = parse_input_lines(lines)

    total = 0

    state, energy = room_to_hallway(state, 2, 0, 3)
    total += energy
    print(state, energy)
    state, energy = room_to_room(state, 1, 0, 2, 0)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 1, 1, 5)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 3, 1, 1)
    total += energy
    print(state, energy)
    state, energy = room_to_room(state, 0, 0, 1, 0)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 3, 0, 7)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 3, 1, 9)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 7, 3, 1)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 5, 3, 0)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 9, 0, 0)
    total += energy
    print(state, energy)

    return total


def manual_part_2_example(lines):
    # pylint: disable=too-many-statements

    state = parse_input_lines(lines)

    total = 0

    state, energy = room_to_hallway(state, 3, 0, 10)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 3, 1, 0)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 2, 0, 9)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 2, 1, 7)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 2, 2, 1)
    total += energy
    print(state, energy)
    state, energy = room_to_room(state, 1, 0, 2, 2)
    total += energy
    print(state, energy)
    state, energy = room_to_room(state, 1, 1, 2, 1)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 1, 2, 5)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 1, 3, 3)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 5, 1, 3)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 7, 1, 2)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 9, 1, 1)
    total += energy
    print(state, energy)
    state, energy = room_to_room(state, 3, 2, 2, 0)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 3, 3, 9)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 3, 3, 3)
    total += energy
    print(state, energy)
    state, energy = room_to_room(state, 0, 0, 1, 0)
    total += energy
    print(state, energy)
    state, energy = room_to_room(state, 0, 1, 3, 2)
    total += energy
    print(state, energy)
    state, energy = room_to_hallway(state, 0, 2, 3)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 1, 0, 2)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 0, 0, 1)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 3, 3, 1)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 9, 0, 0)
    total += energy
    print(state, energy)
    state, energy = hallway_to_room(state, 10, 3, 0)
    total += energy
    print(state, energy)

    return total


def parse_input_lines(lines):
    hallway = lines[1][1:-1]
    rooms = tuple("".join(lines[y][x] for y in range(2, len(lines) - 1)) for x in (3, 5, 7, 9))
    return hallway, rooms
