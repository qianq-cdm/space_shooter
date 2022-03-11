import arcade
import math


class Laser(arcade.Sprite):
    def __init__(self, center_x, center_y, angle):
        super().__init__(":resources:images/space_shooter/laserBlue01.png",
                         center_x=center_x, center_y=center_y, angle=angle)
        self.speed = 5

        self.from_last_update = 0

    def strafe(self, speed: float = 1.0):
        """
        Set a sprites position perpendicular to its angle by speed
        :param speed: speed factor
        """
        angle_correction = 270
        print(f"angle = {self.angle + angle_correction}")
        self.change_x = math.cos(self.angle + angle_correction) * speed
        self.change_y = math.sin(self.angle + angle_correction) * speed

    def update(self):
        self.strafe(self.speed)
        self.center_x += self.change_x
        self.center_y += self.change_y
