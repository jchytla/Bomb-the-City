
import random
import arcade
import PIL

"""scailing constants"""
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_BOMB = 0.05
SPRITE_SCALING_BUILDING = 3
SPRITE_SCALING_EXPLOSION = 0.2
SPRITE_SCALING_LETTERS = 1

"""other constants and global variables"""
HIGHSCORE = 0
SCORE = 0
BUILDING_COUNT = 10
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
DIFFICULTY = 20


class Bomb(arcade.Sprite):
    """Bomb class that makes them fall"""
    
    def update(self):
        
        self.center_y -= 4
        

class Explosion(arcade.Sprite):
    """Explosion class that makes an animation of explosion"""
    
    def __init__(self, texture_list):
        
        super().__init__()
        self.current_texture = 0
        self.textures = texture_list
 
    def update(self):

        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()


class MenuView(arcade.View):
    """Main menu view"""
    
    def on_show(self):
        """Add clicking sound, background and set the place for title"""
        
        self.click_sound = arcade.load_sound("sound/click.ogg")
        self.background = arcade.load_texture("images/background.png")
        
        self.title = None
        self.title = arcade.SpriteList()
        title = "BOMB THE CITY"
        x=200
        for i in range (len(title)):
            if i != 4 and i != 8:
                image = PIL.Image.open("images/Letters/letter{}.png".format(title[i]))
                letter = arcade.Sprite("images/Letters/letter{}.png".format(title[i]), SPRITE_SCALING_LETTERS)
                width,height = image.size
                x+= width/2
                letter.center_x = x
                x+= width/2
                letter.center_y = 450
                self.title.append(letter)
            else:
                x+=20

    def on_draw(self):
        """Draw background, title and options"""
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background)
        arcade.draw_text("Press ENTER to play", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press I for info", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press ESC to quit", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-125, arcade.color.BLACK, font_size=20, anchor_x="center")
        self.title.draw()

    def on_key_press(self, key, modifiers):
        """Methods that show other views or close the game"""
        
        if key == arcade.key.ENTER:
            arcade.play_sound(self.click_sound)
            select_view = SelectView()
            self.window.show_view(select_view)
        elif key == arcade.key.I:
            arcade.play_sound(self.click_sound)
            instructions_view = InstructionView()
            self.window.show_view(instructions_view)
        elif key == arcade.key.ESCAPE:
            arcade.play_sound(self.click_sound)
            arcade.close_window()

            
class SelectView(arcade.View):
    """Options menu view"""
        
    def on_show(self):
        """Add clicking sound, background and set the place for difficulties"""
        
        self.click_sound = arcade.load_sound("sound/click.ogg")
        self.background = arcade.load_texture("images/background.png")
        #EASY
        self.title1 = None
        self.title1 = arcade.SpriteList()
        title1 = "EASY"
        x = 400
        for i in range (len(title1)):
            image = PIL.Image.open("images/Letters/letter{}.png".format(title1[i]))
            letter = arcade.Sprite("images/Letters/letter{}.png".format(title1[i]), SPRITE_SCALING_LETTERS)
            width,height = image.size
            x+= width/2
            letter.center_x = x
            x+= width/2
            letter.center_y = 450
            self.title1.append(letter)
        #MEDIUM
        self.title2 = None
        self.title2 = arcade.SpriteList()
        title2 = "MEDIUM"
        x = 355
        for i in range (len(title2)):
            image = PIL.Image.open("images/Letters/letter{}.png".format(title2[i]))
            letter = arcade.Sprite("images/Letters/letter{}.png".format(title2[i]), SPRITE_SCALING_LETTERS)
            width,height = image.size
            x+= width/2
            letter.center_x = x
            x+= width/2
            letter.center_y = 450
            self.title2.append(letter)
        #HARD
        self.title3 = None
        self.title3 = arcade.SpriteList()
        title3 = "HARD"
        x = 393
        for i in range (len(title3)):
            image = PIL.Image.open("images/Letters/letter{}.png".format(title3[i]))
            letter = arcade.Sprite("images/Letters/letter{}.png".format(title3[i]), SPRITE_SCALING_LETTERS)
            width,height=image.size
            x+= width/2
            letter.center_x = x
            x+= width/2
            letter.center_y = 450
            self.title3.append(letter)
           

    def on_draw(self):
        """Draw background, options and selected difficulty"""

        arcade.start_render()   
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background)
        
        if DIFFICULTY == 20:
            self.title1.draw()
        elif DIFFICULTY == 16:
            self.title2.draw()
        else:
            self.title3.draw()
            
        arcade.draw_text("Press ENTER to play", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press SPACE to change difficulty", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100,arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press M to go to the menu", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-125,arcade.color.BLACK, font_size=20, anchor_x="center")
       
    def on_key_press(self, key, modifiers):
        """Methods that show other views or change difficuly"""
        
        global DIFFICULTY
        if key == arcade.key.ENTER:
            arcade.play_sound(self.click_sound)
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)    
        elif key == arcade.key.SPACE:
            arcade.play_sound(self.click_sound)
            DIFFICULTY-= 4
            DIFFICULTY = (DIFFICULTY)%12+12
        elif key == arcade.key.M:
            arcade.play_sound(self.click_sound)
            menu_view = MenuView()
            self.window.show_view(menu_view)
            
class InstructionView(arcade.View):
    """Info view"""

    def on_show(self):
        """Add clicking sound, background"""
        
        self.click_sound=arcade.load_sound("sound/click.ogg")
        self.background = arcade.load_texture("images/background.png")

    def on_draw(self):
        """Draw background, info and option"""
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background)
        arcade.draw_text("Info", SCREEN_WIDTH/2, SCREEN_HEIGHT/2+100,
                         arcade.color.RED, font_size=50, anchor_x="center")
        arcade.draw_text("""Destroy all the buildings to win, but be careful not to run out of the amunition.
The plane is flying lower and lower and if you hit the building, you lose.
To get higher score, destory the buildings faster, using less bombs and play on harder difficulties.
Use SPACE to drop a bomb.

This game is written by Jakub Chytła and is based on Blitz.""", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50,
                         arcade.color.RED, font_size=20, anchor_x="center")
        arcade.draw_text("Press M to go to the menu", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-125,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """Method that shows other view """
        
        if key == arcade.key.M:
            arcade.play_sound(self.click_sound)
            menu_view = MenuView()
            self.window.show_view(menu_view)
            

class GameOverView(arcade.View):
    """Game lost view"""
    
    def on_show(self):
        """Add clicking sound, background, check scores and set place for title"""
        
        global HIGHSCORE
        self.click_sound = arcade.load_sound("sound/click.ogg")
        self.background = arcade.load_texture("images/background.png")
        
        self.title = None
        self.title = arcade.SpriteList()
        title="YOU LOST"
        if SCORE >= HIGHSCORE:
            HIGHSCORE = SCORE
        x = 300
        for i in range (len(title)):
            if i != 3:
                image = PIL.Image.open("images/Letters/letter{}.png".format(title[i]))
                letter = arcade.Sprite("images/Letters/letter{}.png".format(title[i]), SPRITE_SCALING_LETTERS)
                width,height=image.size
                x+= width/2
                letter.center_x = x
                x+= width/2
                letter.center_y = 450
                self.title.append(letter)
            else:
                x+= 20

    def on_draw(self):
        """Draw background, options and scores"""
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background)
        arcade.draw_text(f"Your score:{SCORE}", SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2, arcade.color.RED, 20,anchor_x="center")
        arcade.draw_text(f"Highest score:{HIGHSCORE}", SCREEN_WIDTH/2+200, SCREEN_HEIGHT/2, arcade.color.RED, 20,anchor_x="center")
        arcade.draw_text("Press M to go to the menu", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75, arcade.color.BLACK, 20,anchor_x="center")
        arcade.draw_text("Press R to retry", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100, arcade.color.BLACK, 20,anchor_x="center")
        arcade.draw_text("Press ESC to quit",SCREEN_WIDTH/2, SCREEN_HEIGHT/2-125, arcade.color.BLACK, 20,anchor_x="center")
        self.title.draw()
        if HIGHSCORE == SCORE:
            arcade.draw_text("New highest score!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-40, arcade.color.RED, 20,anchor_x="center")

    def on_key_press(self, key, modifiers):
        """Method that shows other views or close the game"""
        
        if key == arcade.key.R:
            arcade.play_sound(self.click_sound)
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
            
        if key == arcade.key.M:
            arcade.play_sound(self.click_sound)
            menu_view = MenuView()
            self.window.show_view(menu_view)

        if key == arcade.key.ESCAPE:
            arcade.play_sound(self.click_sound)
            arcade.close_window()


class GameWonView(arcade.View):
    """Game won view"""
    
    def on_show(self):
        """Add clicking sound, background, check scores and set place for title"""

        global HIGHSCORE
        self.click_sound = arcade.load_sound("sound/click.ogg")
        self.background = arcade.load_texture("images/background.png")
        
        self.title = None
        self.title = arcade.SpriteList()
        title = "YOU WON"
        if SCORE >= HIGHSCORE:
            HIGHSCORE = SCORE
        x = 310
        for i in range (len(title)):
            if i != 3:
                image = PIL.Image.open("images/Letters/letter{}.png".format(title[i]))
                letter = arcade.Sprite("images/Letters/letter{}.png".format(title[i]), SPRITE_SCALING_LETTERS)
                width,height = image.size
                x+= width/2
                letter.center_x = x
                x+= width/2
                letter.center_y = 450
                self.title.append(letter)
            else:
                x+= 20

    def on_draw(self):
        """Draw background, options and scores"""
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background)
        arcade.draw_text(f"Your score:{SCORE}", SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2, arcade.color.RED, 20,anchor_x="center")
        arcade.draw_text(f"Highest score:{HIGHSCORE}", SCREEN_WIDTH/2+200, SCREEN_HEIGHT/2, arcade.color.RED, 20,anchor_x="center")
        arcade.draw_text("Press M to go to the menu", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75, arcade.color.BLACK, 20,anchor_x="center")
        arcade.draw_text("Press R to retry", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100, arcade.color.BLACK, 20,anchor_x="center")
        arcade.draw_text("Press ESC to quit",SCREEN_WIDTH/2, SCREEN_HEIGHT/2-125, arcade.color.BLACK, 20,anchor_x="center")
        self.title.draw()
        if HIGHSCORE == SCORE:
            arcade.draw_text("New highest score!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-40, arcade.color.RED, 20,anchor_x="center")

    def on_key_press(self, key, modifiers):
        """Methods that show other views"""
        
        if key == arcade.key.R:
            arcade.play_sound(self.click_sound)
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        elif key == arcade.key.M:
            arcade.play_sound(self.click_sound)
            menu_view = MenuView()
            self.window.show_view(menu_view)
        elif key == arcade.key.ESCAPE:
            arcade.play_sound(self.click_sound)
            arcade.close_window()
 
class GameView(arcade.View):
    """Main game view"""

    def __init__(self):
        """Add sounds, explosion, set score"""
        
        global SCORE
        super().__init__()    
        self.player_list = None
        self.bomb_list = None
        self.building_list=None
        self.explosion_list= None
        self.background = None
        self.player_sprite = None
        self.building = None
        self.title = None
        self.amunition = None
        SCORE=1400-60*DIFFICULTY
        self.explosion_sound = arcade.load_sound("sound/explode2.wav")
        self.whistle_sound = arcade.load_sound("sound/whistle.ogg")
        self.click_sound = arcade.load_sound("sound/click.ogg")
        self.win_sound = arcade.load_sound("sound/win.ogg")
        self.lose_sound = arcade.load_sound("sound/lose.ogg")
        self.explosion_texture_list = []
        columns = 32
        count = 32
        sprite_width = 256
        sprite_height = 256
        file_name = "images/explosion.png"
        self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)

    def setup(self):
        """Add buildings, background, plane, amunition, lists of spirtes, and set place for title"""
        
        self.player_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.building_list = arcade.SpriteList()
        self.explosion_list = arcade.SpriteList()
        self.background = arcade.load_texture("images/background.png")
        self.title = arcade.SpriteList()
        self.amunition = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("images/planeRed1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = -200
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

        #buildings
        for i in range(BUILDING_COUNT):
            outfit = random.randrange(1,7)
            size = random.randrange(2,7)
            for j in range(size):
                block=str(outfit)
                if outfit == 3 or outfit == 6:
                    block+= random.choice(['a','b'])
                self.building = arcade.Sprite("images/tiles/building{}.png".format(block), SPRITE_SCALING_BUILDING)
                self.building.center_x = 230+i*60
                self.building.center_y = 20+j*48
                self.building_list.append(self.building)
                block = str(outfit)
            if outfit<3:
                block+= random.choice(['a','b','c'])
            self.building = arcade.Sprite("images/tiles/roof{}.png".format(block), SPRITE_SCALING_BUILDING)
            self.building.center_x = 230+i*60
            self.building.center_y = 20+size*48
            self.building_list.append(self.building)
            
        #title
        title = "BOMB THE CITY"
        x = 200
        for i in range (len(title)):
            if i != 4 and i != 8:
                image = PIL.Image.open("images/Letters/letter{}.png".format(title[i]))
                letter = arcade.Sprite("images/Letters/letter{}.png".format(title[i]), SPRITE_SCALING_LETTERS)
                width,height = image.size
                x+= width/2
                letter.center_x = x
                x+= width/2
                letter.center_y = 450
                self.title.append(letter)
            else:
                x+= 20

        #amunition        
        x = 205
        for i in range(DIFFICULTY):
            bomb = arcade.Sprite("images/bomb.png", SPRITE_SCALING_BOMB)
            width,height=image.size
            bomb.center_x=x
            x+=20
            bomb.center_y=550
            self.amunition.append(bomb)
            
        #set first explosion and bomb (first bomb and explosion sometimes lags)
        bomb = Bomb("images/bomb.png", SPRITE_SCALING_BOMB)
        bomb.center_x = self.player_sprite.center_x
        bomb.center_y = self.player_sprite.center_y
        self.bomb_list.append(bomb)
        explosion = Explosion(self.explosion_texture_list)
        explosion.center_x = self.player_sprite.center_x
        explosion.center_y = self.player_sprite.center_y
        explosion.update()
        self.explosion_list.append(explosion)
                
    def on_key_press(self, key, modifiers):
        """Method that drops a bomb"""
        
        if key == arcade.key.SPACE:
            if self.player_sprite.center_x-self.bomb_list[-1].center_x>200 and len(self.amunition)!=0:
                bomb = Bomb("images/bomb.png", SPRITE_SCALING_BOMB)
                bomb.center_x = self.player_sprite.center_x
                bomb.center_y = self.player_sprite.center_y
                arcade.play_sound(self.whistle_sound)
                self.bomb_list.append(bomb)
                self.amunition[-1].remove_from_sprite_lists()

    def on_draw(self):
        """Draw background, plane, bombs, explosions, amunition, title, buildings and score"""
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background)
        self.title.draw()
        self.bomb_list.draw()
        self.player_list.draw()
        self.building_list.draw()
        self.explosion_list.draw()
        self.amunition.draw()
        arcade.draw_text(f"Score: {SCORE}", 10, 20, arcade.color.BLACK, 14)

    def update(self, delta_time):
        """Make plane move, change scores, check for colisions, remove bombed buildings, show other view if game is finished"""
        
        global SCORE
        self.bomb_list.update()
        self.building_list.update()
        self.explosion_list.update()
        #check for bombed buildings 
        for bomb in self.bomb_list:
            hit_list = arcade.check_for_collision_with_list(bomb,self.building_list)
            for building in hit_list:
                explosion=Explosion(self.explosion_texture_list)
                explosion.center_x = building.center_x
                explosion.center_y = building.center_y
                explosion.update()
                self.explosion_list.append(explosion)
                SCORE += 40
                arcade.play_sound(self.explosion_sound)
                building.remove_from_sprite_lists()
        #move plane
        self.player_sprite.center_x += 15-DIFFICULTY/2
        SCORE -= 1
        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.player_sprite.center_y -= 48
            self.player_sprite.center_x = 0
            SCORE -= 100
            bomb = Bomb("images/bomb.png", SPRITE_SCALING_BOMB)
            bomb.center_x = -200
            bomb.center_y = 0
            self.bomb_list.append(bomb)
        #check if game is finished
        if len(self.building_list) == 0:
            arcade.play_sound(self.win_sound)
            SCORE+= 600//(DIFFICULTY-10)*(len(self.amunition))
            view = GameWonView()
            self.window.show_view(view)
        elif arcade.check_for_collision_with_list(self.player_sprite, self.building_list):
            arcade.play_sound(self.lose_sound)
            view = GameOverView()
            self.window.show_view(view)

            
def main():
    
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Bomb the City")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()



if __name__ == "__main__":
    
    main()

