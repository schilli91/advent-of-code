class Wire(object):

    def __init__(self, path_string):
        self.full_path = None
        self.path = [p.strip() for p in path_string.split(',')]

    def calculate_full_path(self):
        self.current = (0, 0)
        self.full_path = [self.current]

        for path_element in self.path:
            direction = path_element[0]
            steps = int(path_element[1:])

            for i in range(steps):
                if direction == 'R':
                    self.current = (self.current[0] + 1, self.current[1])
                if direction == 'U':
                    self.current = (self.current[0], self.current[1] + 1)
                if direction == 'L':
                    self.current = (self.current[0] - 1, self.current[1])
                if direction == 'D':
                    self.current = (self.current[0], self.current[1] - 1)

                self.full_path.append(self.current)

    def intersects_with(self, wire):
        if self.full_path is None:
            self.calculate_full_path()
        if wire.full_path is None:
            wire.calculate_full_path()

        intersections = set(self.full_path) & set(wire.full_path)
        intersections.remove((0, 0))
        return intersections


# def get_closest_intersection(intersections):
#     distance = None
#     for intersection in intersections:
#         if distance is None:
#             distance = intersection[0] + intersection[1]
#         candidate = intersection[0] + intersection[1]
#         if candidate < distance:
#             distance = candidate
#     return distance


if __name__ == '__main__':
    print('Test Wire.')
    wire = Wire('R8,U5,L5,D3')
    # wire = Wire('U4, R2 ,D2, L2')
    second_wire = Wire('U7,R6,D4,L4')
    wire.calculate_full_path()
    # print(wire.path)
    # print(wire.full_path)

    intersections = wire.intersects_with(second_wire)
    print('Intersections: {}'.format(intersections))
