class Journey:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.travelled_distance = 0
        self.checkpoint = [(x, y)]

    def move(self, dx, dy, distance):
        self.x += dx
        self.y += dy
        self.travelled_distance += distance
        self.checkpoint.append((self.x, self.y))
        return self
    
    def up(self, dist):
        return self.move(dist, 0, dist)
    
    def down(self, dist):
        return self.move(dist, 0, -dist)
    
    def left(self, dist):
        return self.move(0, -dist, dist)
    
    def right(self, dist):
        return self.move(0, dist, dist)
    
journey = Journey(1, 1)
journey.up(6).right(2).down(6).right(4).up(2).left(2).up(4).right(2).down(2)