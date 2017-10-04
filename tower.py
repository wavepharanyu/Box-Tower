import arcade
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
vx = 10
class TowerGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture('images/town.jpg')
        self.box = arcade.Sprite('images/box1.png')
        self.box.set_position(500, 350)
        self.vx = vx

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.box.draw()

    def on_key_press(self, key, modifiers):
        box = self.box
        
        if key == arcade.key.SPACE:
            self.vx = 0
            self.box.set_position(self.box.center_x+self.vx, 350)

    def update(self, delta):
        box = self.box

        if box.center_x > SCREEN_WIDTH:
            self.vx *= -1
        
        if box.center_x < 0:
            self.vx *= -1
        self.box.set_position(self.box.center_x+self.vx, self.box.center_y)

 
if __name__ == '__main__':
    window = TowerGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()