
import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_BOMB = 0.05
SPRITE_SCALING_BUILDING = 3
SPRITE_SCALING_EXPLOSION = 0.2

BUILDING_COUNT = 10

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


class Bomb(arcade.Sprite):

    def update(self):
        self.center_y -= 4
        
class MyGame(arcade.Window):

    def __init__(self):
        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Bomb the City")
        
        self.player_list = None
        self.bomb_list = None
        self.building_list=None
        self.explosion_list= None

        self.player_sprite = None
        self.building=None


        arcade.set_background_color(arcade.color.AQUA)

    def setup(self):
        
        self.player_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.building_list=arcade.SpriteList()
        self.explosion_list=arcade.SpriteList()

        self.player_sprite = arcade.Sprite("images/planeRed1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = -SCREEN_WIDTH/2
        self.player_sprite.center_y = 550
        self.player_list.append(self.player_sprite)
        
        for i in range(BUILDING_COUNT):
            outfit=random.randrange(1,7)
            size=random.randrange(2,7)
            for j in range(size):
                block=str(outfit)
                if outfit==3 or outfit==6:
                    block+=random.choice(['a','b'])
                self.building = arcade.Sprite("images/tiles/building{}.png".format(block), SPRITE_SCALING_BUILDING)
                self.building.center_x=200+i*60
                self.building.center_y=20+j*48
                self.building_list.append(self.building)
                
            block=str(outfit)
            if outfit<3:
                block+=random.choice(['a','b','c'])
            self.building = arcade.Sprite("images/tiles/roof{}.png".format(block), SPRITE_SCALING_BUILDING)
            self.building.center_x=200+i*60
            self.building.center_y=20+size*48
            
            self.building_list.append(self.building)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            bomb = Bomb("images/bomb.png", SPRITE_SCALING_BOMB)

            bomb.center_x = self.player_sprite.center_x
            bomb.center_y = self.player_sprite.center_y

            self.bomb_list.append(bomb)

    def on_draw(self):
        arcade.start_render()
        self.bomb_list.draw()
        self.player_list.draw()
        self.building_list.draw()
        self.explosion_list.draw()


    def update(self, delta_time):
        self.bomb_list.update()
        self.building_list.update()

        
        for bomb in self.bomb_list:
            hit_list = arcade.check_for_collision_with_list(bomb,self.building_list)

            for building in hit_list:
                explosion=arcade.Sprite("images/explosion04.png",SPRITE_SCALING_EXPLOSION)
                explosion.center_x = building.center_x
                explosion.center_y = building.center_y
                self.explosion_list.append(explosion)
                building.remove_from_sprite_lists()
                explosion.remove_from_sprite_lists()
        
        self.player_sprite.center_x += 6
        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.player_sprite.center_y -=48
            self.player_sprite.center_x = 0
def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
