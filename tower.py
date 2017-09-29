import arcade
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
 
class TowerGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture('images/town.jpg')

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        
 
if __name__ == '__main__':
    window = TowerGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()