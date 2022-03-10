import arcade

class PlayerShip(arcade.Sprite):
    def __init__(self, center_x, center_y, texture):
        super().__init__(texture, center_x=center_x, center_y=center_y)
        self.speed = 0.1

    def update(self, delta_time):
        self.strafe(self.speed)
        self.center_x += self.change_x
        self.center_y += self.change_y

    def accelerate(self):
        self.speed += 0.01

    def decelerate(self):
        self.speed -= 0.01
