import arcade


class PlayerShip(arcade.Sprite):
    def __init__(self, texture):
        super().__init__(texture)
        self.speed = 0.5

    def update(self, delta_time):
        self.strafe(self.speed)
        self.center_x += self.change_x
        self.center_y += self.change_y

    def accelerate(self):
        self.speed += 0.2

    def decelerate(self):
        self.speed -= 0.2
