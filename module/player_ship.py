import arcade


class PlayerShip(arcade.Sprite):
    def __init__(self, width, height, texture):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        super().__init__(texture, center_x=self.SCREEN_WIDTH / 2, center_y=self.SCREEN_HEIGHT / 5)
        self.speed = 1

        self.from_last_update = 0

    def update(self, delta_time):
        if self.from_last_update >= 0.5:
            self.strafe(self.speed)
            self.from_last_update = 0
        else:
            self.from_last_update += delta_time
            print(f"from_last_update = {self.from_last_update}")

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.bottom <= 0:
            self.top = self.SCREEN_HEIGHT
        elif self.SCREEN_HEIGHT <= self.top:
            self.bottom = 0

        if self.left <= 0:
            self.right = self.SCREEN_WIDTH
        elif self.SCREEN_WIDTH <= self.right:
            self.left = 0
