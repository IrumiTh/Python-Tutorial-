class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
point2 = Point(20,80)
point1.move()
point1.draw()
point1.x =50
print(point1.x)
print(point2.move())
