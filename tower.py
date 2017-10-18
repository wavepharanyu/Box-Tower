import arcade
from models import World,Box
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
class TowerGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height,)
        self.background = None
        self.world = World(width,height)
        box = Box(self.world,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.speed = None
        self.score = 0

    def setup(self):
        self.background = arcade.load_texture('images/town.jpg')  

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.world.box.draw()
        arcade.draw_text(str("Score: ")+str(self.score),self.width - 150, self.height - 25,arcade.color.BLACK, 20)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.world.box.speed = 0
            self.world.box.change_y = -10 

   
    def update(self, delta):
        self.world.update(delta)
        if(self.world.box.center_y == 150):
             self.world.box.change_y = 0


if __name__ == '__main__':
    window = TowerGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()