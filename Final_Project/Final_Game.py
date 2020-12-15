#File I/O HighScore


#the actual game
#all imports
import pygame as p
import random
import time
from settings import *
from sprites import *
from os import path

class Game:
    
    def __init__(self):
        #start up game window
        #Setting up screen
        p.init()
        p.mixer.init()
        self.screen = p.display.set_mode((width,height))
        p.display.set_caption("Final Project")
        #I learned about using pygames time.Clock
        self.clock = p.time.Clock()
        self.running = True
        self.font_name = p.font.match_font(FONT_NAME)
        self.score = 0
        self.load_data()


    def load_data(self):
        #load High Score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir,HS_FILE),'w') as f:
            try:
                self.highscore = int(f.read()) 
            except:
                self.highscore = 0

    def new(self):
        #starting new game
        
        self.a_sprites = p.sprite.Group()
        self.mobs = p.sprite.Group()
        self.points = p.sprite.Group()
        self.player = Player()
        self.a_sprites.add(self.player)
        for i in range(10):
            m = Mob()
            self.a_sprites.add(m)
            self.mobs.add(m)
        for i in range(10):
            point = Mob2()
            self.a_sprites.add(point)
            self.points.add(point)
            
        self.run()
    
    def run(self):
        #Game loop
        #game speed
        self.clock.tick(frames)
        self.playing = True
        while self.playing:
            self.clock.tick(frames)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        #update
        self.a_sprites.update()

        #check for collision
        #Die
        hits = p.sprite.spritecollide(self.player,self.mobs, False)
        if hits:
            self.playing = False
            
        #Points
        contact = p.sprite.spritecollide(self.player,self.points, True)
        if contact:
            self.score +=10
            
    
    def events(self):
        #events
        for event in p.event.get():
        #Check for quit
            if event.type ==p.QUIT:
                if self.playing:
                    self.playing = False    
                self.running = False
    
    def draw(self):
        #draw
        self.screen.fill(BLACK)
        self.a_sprites.draw(self.screen)
        self.draw_text(str(self.score),22,WHITE,width/2,15)
        #final piece
        p.display.flip()
    
    def show_start_screen(self):
        #game start screen
        self.screen.fill(WHITE)
        self.draw_text(TITLE, 48, BLUE, width/2,height/2 - 60)
        self.draw_text("Dodge the Red, Collect the Green",22,BLUE, width/2,height * 5/8)
        self.draw_text("Press Any Key to Play",22,BLUE,width/2,height*3/4)
        self.draw_text("HighScore: " + str(self.highscore),22,BLUE, width/2, 15)
        p.display.flip()
        self.wait_for_key()
        
    
    def show_gameover_screen(self):
        #making a list and dict of respnses depending on how good you do
        responses = {'less_4' :["Better Luck Next Time","Good Try","You Can Do Better!","What was That?"],
                         'less_8' :["Almost Had It!","That Was Close!","Keep It Up!"],
                         'over_8' :["Amazing!","Incredible!","You're Unstoppable!"]}
        
        bad = random.choice(responses['less_4'])
        ok = random.choice(responses['less_8'])
        good = random.choice(responses['over_8'])
        
        #to allow you to still quit without going to the end screen
        if not self.running:
            return
        self.screen.fill(WHITE)
        self.draw_text("GAME OVER", 48, BLUE, width/2,height/2 - 60)
        self.draw_text("Score: " + str(self.score),22,BLUE, width/2,height * 5/8)
        self.draw_text("Press Any Key to Play Again",22,BLUE,width/2,height*3/4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!",28,BLUE,width/2,height/2 + 50)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("HighScore: " + str(self.highscore),28,BLUE, width/2, height/2+30)
        if self.score < 50:
            self.draw_text(bad, 28, BLUE, width/2,height/2 - 100)
        elif self.score < 90:
            self.draw_text(ok, 28, BLUE, width/2,height/2 - 100)
        else :
            self.draw_text(good, 28, BLUE, width/2,height/2 - 100)
        p.display.flip()
        self.wait_for_key()
        
    
    def draw_text(self, text, size, color, x, y):
        #to give us the ability to add text to the screen
        font = p.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop =(x,y)
        self.screen.blit(text_surface, text_rect)
        
    def wait_for_key(self):
        #to give a delay on the start and end screen
        waiting = True
        while waiting:
            self.clock.tick(frames)
            for event in p.event.get():
                if event.type == p.QUIT:
                    waiting = False
                    self.running = False
                if event.type == p.KEYUP:
                    waiting = False
                    self.score = 0
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameover_screen()
p.quit()
