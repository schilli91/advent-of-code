from aoc2020.day_5.boarding_passes import BOARDING_PASSES


def calculate_maximum_seat_id():
    max_seat_id = -1
    for boarding_pass in BOARDING_PASSES.splitlines():
        current = decode_boarding_pass(boarding_pass)
        if current > max_seat_id:
            max_seat_id = current
    return max_seat_id


def calculate_seat():
    booked_seats = [decode_boarding_pass(boarding_pass) for boarding_pass in BOARDING_PASSES.splitlines()]
    available_seats = [id for id in range(calculate_maximum_seat_id()) if id not in booked_seats]

    for i in range(len(available_seats)):
        if available_seats[i] - available_seats[i - 1] == 1:
            continue
        if i + 1 == len(available_seats):
            return available_seats[i]
        if available_seats[i + 1] - available_seats[i] == 1:
            continue
        return available_seats[i]
    return False


def decode_boarding_pass(boarding_pass):
    row = decode_row(boarding_pass)
    column = decode_column(boarding_pass)
    seat_id = row * 8 + column
    return seat_id


def decode_row(boarding_pass):
    path = boarding_pass[:7]
    return _get_binary_path(path, "F")


def decode_column(boarding_pass):
    path = boarding_pass[7:]
    return _get_binary_path(path, "L")


def _get_binary_path(path: str, lower_key: str):
    binary_path_list = ["0" if str(l).upper() == lower_key.upper() else "1" for l in path]
    binary_path = "".join(binary_path_list)
    return int(binary_path, 2)


if __name__ == '__main__':
    print("Day 5")
    max_seat_id = calculate_maximum_seat_id()
    print(f"The highest seat ID is {max_seat_id}.")
    seat_id = calculate_seat()
    print(f"The seat ID is {seat_id}.")
