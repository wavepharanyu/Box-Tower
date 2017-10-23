import random
import arcade.key

SPRITE_SCALING = 1

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 1000

BOX_SPEED = 5
SPEED = 7

class Box(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('images/box.png', SPRITE_SCALING / 2)
        self.half_width = self.width // 2
        self.half_height = self.height // 2
        self.center_x = x
        self.center_y = y
        self.is_kill = False

    def update(self):
        super().update()

        if self.center_y < -self.half_width:
            #print("KILL")
            self.is_kill = True
            self.kill()
       
class MyAppWindow(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Box Tower")

        # Sprite lists
        self.speed = SPEED
        self.all_sprites_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.stack_count = 0
        self.score_text = None

        self.player_sprite = Box(250, 925)
        self.new_box = None
        self.moving_all_box_down = False
        self.moving_down_size = 0    
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()

        self.player_sprite.draw()
        self.all_sprites_list.draw()

        output = f"Score: {self.score}"

        if not self.score_text or output != self.score_text.text:
            self.score_text = arcade.create_text(output, arcade.color.WHITE, 14)
        # Render the text
        arcade.render_text(self.score_text, 10, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if not self.new_box is None:
                return
            self.new_box = Box(self.player_sprite.center_x, self.player_sprite.center_y)
            self.new_box.change_y = -BOX_SPEED
            self.all_sprites_list.append(self.new_box)
    
    def update_player(self):
        self.player_sprite.update()

        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.speed *= -1

        if self.player_sprite.center_x < 0:
            self.speed *= -1
        
        self.player_sprite.set_position(self.player_sprite.center_x+self.speed, self.player_sprite.center_y)
 

    def update(self, delta_time):
        self.update_player()
        self.all_sprites_list.update()

        if self.moving_all_box_down:
            if self.moving_down_size >= self.player_sprite.height:
                for box in self.box_list:
                    box.change_y = 0
                self.moving_all_box_down = False
            self.moving_down_size += BOX_SPEED

        if not self.new_box is None:
            if self.new_box.is_kill: ## GAME OVER CHECKING
                self.new_box = None
                return

            if len(self.box_list) > 0:
                top_box = self.box_list[-1]
                if arcade.check_for_collision(self.new_box, top_box):
                    if abs(self.new_box.center_x - top_box.center_x) <= self.new_box.width * (2 / 3):
                        self.new_box.change_y = 0

                        self.stack_count += 1
                        self.box_list.append(self.new_box)

                    if self.stack_count > 4: ### STACKING SIZE LIMIT
                        for box in self.box_list:
                            box.change_y = -BOX_SPEED
                        self.moving_all_box_down = True
                        self.moving_down_size = 0
                        
                    self.new_box = None
               
def main():
    MyAppWindow()
    arcade.run()


if __name__ == "__main__":
    main()