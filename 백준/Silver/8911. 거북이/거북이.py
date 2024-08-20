class Turtle:
    def __init__(self):
        self.x = self.y = self.di = 0
        self.min_x = self.min_y = self.max_x = self.max_y = 0

    def move(self, dist):
        dx, dy = [(-1, 0), (0, 1), (1, 0), (0, -1)][self.di]
        self.x, self.y = self.x + dx * dist, self.y + dy * dist
        self.min_x, self.max_x = min(self.min_x, self.x), max(self.max_x, self.x)
        self.min_y, self.max_y = min(self.min_y, self.y), max(self.max_y, self.y)

    def turn(self, how):
        self.di = (self.di + 4 + how) % 4

    def calculateSize(self):
        return (self.max_x - self.min_x) * (self.max_y - self.min_y)


for _ in range(int(input())):
    turtle = Turtle()
    for cmd in input():
        turtle.move(1 if cmd == 'F' else -1 if cmd == 'B' else 0)
        turtle.turn(1 if cmd == 'R' else -1 if cmd == 'L' else 0)
    print(turtle.calculateSize())