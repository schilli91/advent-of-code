from day_3.day_three_data import *
from day_3.wire import Wire


def get_closest_intersection_distance(first_wire, second_wire):
    intersections = first_wire.intersects_with(second_wire)
    distance = None
    for intersection in intersections:
        if distance is None:
            distance = abs(intersection[0]) + abs(intersection[1])
        candidate = abs(intersection[0]) + abs(intersection[1])
        if candidate < distance:
            distance = candidate
    return distance


def get_shortest_path(first_wire, second_wire):
    intersections = first_wire.intersects_with(second_wire)
    first_steps = _get_steps_per_intersection(first_wire, intersections)
    second_steps = _get_steps_per_intersection(second_wire, intersections)

    shortest_path = None
    for intersection in intersections:
        if shortest_path is None:
            shortest_path = first_steps[intersection] + second_steps[intersection]
            continue
        candidate = first_steps[intersection] + second_steps[intersection]
        if candidate < shortest_path:
            shortest_path = candidate
    return shortest_path


def _get_steps_per_intersection(wire, intersections):
    steps_to_intersection = {}
    steps = 0
    duplicate_positions = _get_duplicates(wire.full_path)
    duplicate_steps = {}

    for position in wire.full_path:
        # Reset steps, in case position was already visited.

        if position in duplicate_positions:
            if position not in duplicate_steps:
                duplicate_steps[position] = steps
            else:
                # For some reason this check is not necessary,
                # although it's mentions in part two.
                # steps = duplicate_steps[position]
                pass

        if position in intersections:
            if position not in steps_to_intersection:
                steps_to_intersection[position] = steps
        steps += 1
    return steps_to_intersection


def _get_duplicates(list_with_duplicates):
    seen = {}
    duplicates = []

    for item in list_with_duplicates:
        if item not in seen:
            seen[item] = 1
            continue

        if seen[item] == 1:
            duplicates.append(item)
        seen[item] += 1
    return duplicates


def test_part_one_samples():
    for sample in test_path_samples:
        first_wire = Wire(sample['paths'][0])
        second_wire = Wire(sample['paths'][1])

        distance = get_closest_intersection_distance(first_wire, second_wire)
        if distance == sample['distance']:
            print('✅ Test successful.')
        else:
            print('❌ Test not successful.')
            print('{} (expected {})'.format(distance, sample['distance']))
        print('')


def test_part_two_samples():
    for sample in test_path_samples:
        first_wire = Wire(sample['paths'][0])
        second_wire = Wire(sample['paths'][1])

        steps = get_shortest_path(first_wire, second_wire)
        if steps == sample['steps']:
            print('✅ Test successful.')
            print(steps)
        else:
            print('❌ Test not successful.')
            print('{} (expected {})'.format(steps, sample['steps']))
        print('')


def process_part_one():
    first_wire = Wire(input_paths[0])
    second_wire = Wire(input_paths[1])
    distance = get_closest_intersection_distance(first_wire, second_wire)
    print('The clostest intersection is {} Manhattan distance points away from the central port.'.format(distance))


def process_part_two():
    first_wire = Wire(input_paths[0])
    second_wire = Wire(input_paths[1])
    steps = get_shortest_path(first_wire, second_wire)
    print('The clostest intersection in terms of steps is {} steps away from central port.'.format(steps))
    print('First attempt of 14104 steps is too low.')


if __name__ == '__main__':
    print('Day 3\n')

    print('1️⃣ Part One')

    print('Running test samples.\n')
    test_part_one_samples()
    process_part_one()

    print('\n===============================================================\n')

    print('2️⃣ Part Two')

    print('Running test samples.\n')
    # test_part_two_samples()
    process_part_two()
