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
        self.count = 0
        self.check = True
        self.score_text = None
        self.point_x1 = 0
        self.point_x2 = 0
        self.point_y1 = 0
        self.point_y2 = 0
        self.player_sprite = arcade.Sprite("images/box.png", SPRITE_SCALING/2)
        
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 925
        self.all_sprites_list.append(self.player_sprite)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()

        self.box_list.draw()
        self.box_hit_list.draw()
        self.player_sprite.draw()

        output = f"Score: {self.score}"

        if not self.score_text or output != self.score_text.text:
            self.score_text = arcade.create_text(output, arcade.color.WHITE, 14)
        # Render the text
        arcade.render_text(self.score_text, 10, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.box = arcade.Sprite("images/box.png", SPRITE_SCALING/2)
            self.box.center_x = self.player_sprite.center_x
            self.box.top = self.player_sprite.bottom
            self.all_sprites_list.append(self.box)
            self.box_list.append(self.box)

    def update(self, delta_time):

        self.box_list.update()
        self.box_hit_list.update()
        self.all_sprites_list.update()

        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.speed *= -1

        if self.player_sprite.center_x < 0:
            self.speed *= -1
        
        self.player_sprite.set_position(self.player_sprite.center_x+self.speed, self.player_sprite.center_y)
 
        for box in self.box_list:
            if(self.count == 0):
                if(box.center_y < 65):
                    box.change = 0
                    self.point_x1 = box.center_x +55
                    self.point_x2 = box.center_x -55
                    self.point_y1 = box.center_y +130
                    self.box_hit_list.append(box)
                    self.box_list.remove(box)
                    self.count += 1
                else:
                    box.center_y -= BOX_SPEED

            elif self.count > 4:
                    for boxx in self.box_hit_list:
                        self.box_hit_list.remove(boxx)
                        break
                    for boxxx in self.box_hit_list:
                        boxxx.center_y -= 130
                    self.point_y1 -= 130
                    self.count = 4

            else:
                box.center_y -= BOX_SPEED
                if(box.center_x >= self.point_x2 and box.center_x <= self.point_x1 and box.center_y <= self.point_y1):   
                #if box.top < 130+(self.count*130):
                    box.change_y = 0
                    self.point_x1 = box.center_x +55
                    self.point_x2 = box.center_x -55
                    self.point_y1 = box.center_y +130
                    self.box_hit_list.append(box)
                    self.box_list.remove(box)
                    self.count += 1
                    self.score += 10
                else:
                    self.count += 0
               
def main():
    MyAppWindow()
    arcade.run()


if __name__ == "__main__":
    main()