import random
import arcade.key

SPRITE_SCALING = 1

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

BULLET_SPEED = 5
SPEED = 7


class Bullet(arcade.Sprite):
    def update(self):
        if self.center_y < 75:
            self.change_y = 0
        else:
            self.center_y -= BULLET_SPEED

class MyAppWindow(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Bullets Demo")

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.speed = SPEED
        self.all_sprites_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.bullet_hit_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.count = 0
        self.score_text = None
        self.player_sprite = arcade.Sprite("images/box.png", SPRITE_SCALING/2)
        
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 925
        self.all_sprites_list.append(self.player_sprite)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()

        self.bullet_list.draw()
        self.bullet_hit_list.draw()
        self.player_sprite.draw()

        output = f"Score: {self.score}"

        if not self.score_text or output != self.score_text.text:
            self.score_text = arcade.create_text(output, arcade.color.WHITE, 14)
        # Render the text
        arcade.render_text(self.score_text, 10, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.bullet = Bullet("images/box.png", SPRITE_SCALING/2)
            self.bullet.center_x = self.player_sprite.center_x
            self.bullet.top = self.player_sprite.bottom

            self.all_sprites_list.append(self.bullet)
            self.bullet_list.append(self.bullet)

    def update(self, delta_time):

        self.bullet_list.update()
        self.bullet_hit_list.update()
        self.all_sprites_list.update()

        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.speed *= -1

        if self.player_sprite.center_x < 0:
            self.speed *= -1
        
        self.player_sprite.set_position(self.player_sprite.center_x+self.speed, self.player_sprite.center_y)
 
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet,self.bullet_hit_list)
            if self.count == 0:
                self.bullet_hit_list.append(bullet)
            self.count += 1 
            for bullet2 in hit_list:
                if len(hit_list) > 0:
                    bullet.center_y += 0
                    self.bullet_hit_list.remove(bullet2)
                    self.bullet_hit_list.append(bullet)
                    self.score = 10



def main():
    MyAppWindow()
    arcade.run()


if __name__ == "__main__":
    main()