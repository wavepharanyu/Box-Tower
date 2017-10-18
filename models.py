import arcade
SPEED = 10
class Box(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__('images/box.png')
        self.world = world
        self.center_x = x
        self.center_y = y
        self.speed = SPEED

    def update(self,delta):
        super().update()
        if self.center_x > self.world.SCREEN_WIDTH:
            self.speed *= -1

        if self.center_x < 0:
            self.speed *= -1
        
        self.box.set_position(self.box.center_x+self.speed, self.box.center_y)

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.box = Box(self, 500, 150)
      
        
    def update(self,delta):
        self.alien.update(delta)
