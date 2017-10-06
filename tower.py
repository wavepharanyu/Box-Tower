import arcade
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
vx = 10
vx1 = 10
class TowerGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture('images/town.jpg')
        self.box = arcade.Sprite('images/box.png')
        self.box1 = arcade.Sprite('images/box.png')
        self.box.set_position(500, 350)
        self.box1.set_position(500, 600)
        self.vx = vx
        self.vx1 = vx1
        self.score = 0
        self.status = 0
    def on_key_press(self, key, modifiers):
        box = self.box
        if key == arcade.key.SPACE:
            self.vx = 0
            self.box.set_position(self.box.center_x+self.vx, 350)
            self.status = 1
            self.score += 10

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.box.draw()
        if(self.status == 1):
            self.box1.draw()
        arcade.draw_text(str("Score: ")+str(self.score),self.width - 150, self.height - 25,arcade.color.BLACK, 20)
 
    def update(self, delta):
        box = self.box
        box1 = self.box1
        if box.center_x > SCREEN_WIDTH:
            self.vx *= -1
        
        if box.center_x < 0:
            self.vx *= -1
        self.box.set_position(self.box.center_x+self.vx, self.box.center_y)

        if box1.center_x > SCREEN_WIDTH:
            self.vx1 *= -1
        
        if box1.center_x < 0:
            self.vx1 *= -1
        self.box1.set_position(self.box1.center_x+self.vx1, self.box1.center_y)

 
if __name__ == '__main__':
    window = TowerGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()