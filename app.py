class Robot:
    def __init__(self):
        self.directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        self.direction_order = ['N', 'E', 'S', 'W']
        self.current_direction_index = 0
        self.position = [0, 0]
        self.move_forward_functions = {
            'N': lambda: self.position.__setitem__(1, self.position[1] + 1),
            'E': lambda: self.position.__setitem__(0, self.position[0] + 1),
            'S': lambda: self.position.__setitem__(1, self.position[1] - 1),
            'W': lambda: self.position.__setitem__(0, self.position[0] - 1)
        }
        self.rotate_function = lambda: self.__setattr__('current_direction_index', (self.current_direction_index + 1) % 4)

    def move_forward(self):
        self.move_forward_functions[self.direction_order[self.current_direction_index]]()

    def rotate(self):
        self.rotate_function()

    def process_input(self, instruction):
        {
            'F': self.move_forward,
            'R': self.rotate
        }.get(instruction, lambda: None)()


# Example usage with user input:
robot = Robot()

while True:
    instruction = input("Enter 'F' to move forward or 'R' to rotate or 'exit' to quit: ").upper()

    if instruction == 'EXIT':
        break

    # Process the instruction using the robot's method
    robot.process_input(instruction)
    print(f"After instruction {instruction}, position: {robot.position}")
