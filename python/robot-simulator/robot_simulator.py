# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot:
    def __init__(self, direction: tuple[int, int] = NORTH, x_pos: int = 0, y_pos: int = 0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'A':
                self.coordinates = (
                    self.coordinates[0] + self.direction[0],
                    self.coordinates[1] + self.direction[1],
                )
            else:
                self.turn(instruction)
        
    def turn(self, side):
        flip = -1 if side == 'L' else 1
        self.direction = (
            flip * self.direction[1] if self.direction[1] else 0,
            -1 * flip * self.direction[0] if self.direction[0] else 0
        )
