import arcade


class PlayerShip:
    def __init__(self, width, height):
        self.time_from_last_position_update = 0
        self.center_x = width / 2
        self.center_y = height / 5
        self.change_x = 0
        self.change_y = 0
        self.angle = 0
        self.speed = 1
        self.texture = ":resources:images/space_shooter/playerShip1_blue.png"
        self.player_ship_sprite = arcade.Sprite(self.texture, center_x=self.center_x, center_y=self.center_y,
                                                angle=self.angle)

    def update_position(self, delta_time):
        self.time_from_last_position_update += delta_time
        if self.time_from_last_position_update >= 1000:
            self.player_ship_sprite.strafe(self.speed)
            self.center_x += self.player_ship_sprite.change_x
            self.center_y += self.player_ship_sprite.change_y

    def on_draw(self):
        self.player_ship_sprite.draw()

    def on_update(self, delta_time):
        self.update_position(delta_time)
        self.player_ship_sprite.center_x = self.center_x
        self.player_ship_sprite.center_y = self.center_y

    def turn_left(self):
        self.player_ship_sprite.turn_left(15)

    def turn_right(self):
        self.player_ship_sprite.turn_right(15)
