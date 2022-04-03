from random import *
from math import*
from re import X
from tkinter import CENTER
from tkinter.tix import Balloon
from matplotlib.pyplot import polar
import pygame
from pygame import *

from random import choice
import random
import datetime



pygame.init()


screen = pygame.display.set_mode((1535, 800))
pygame.display.set_caption("WAR")
BLACK = (0, 0, 0)  # RGB
RED = (255, 0, 0)
ORANGE = (255, 75,75)
GREEN = (0, 255, 0)
BLUE=(0,181,226)
BLUE2=(0,0,255)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
step = 5
screen_width = 1535
screen_height = 800
explosion=pygame.image.load("Objects\powerb.png").convert_alpha()
# startingimg=pygame.image.load("hero\startingimg.png").convert_alpha()
bg = pygame.image.load("Objects\\bg2.png").convert_alpha()
block1=pygame.image.load("Objects\\bg.block.png").convert_alpha()
block5=pygame.image.load("Objects\\bg.5blocks.png").convert_alpha()
ballAlien= pygame.image.load("Alien\darkgray__powerball.png").convert_alpha()
ballAlienDestroyed=[pygame.image.load("Alien\darkgray__BulletEx2.png").convert_alpha(),pygame.image.load("Alien\darkgray__BulletEx3.png").convert_alpha()]
ballsuperAlien= [pygame.image.load("Alien\\aliendropping0001-removebg-preview.png").convert_alpha(),pygame.image.load("Alien\\aliendropping0002-removebg-preview.png").convert_alpha(),pygame.image.load("Alien\\aliendropping0003-removebg-preview.png").convert_alpha(),pygame.image.load("Alien\\aliendropping0004-removebg-preview.png").convert_alpha(),pygame.image.load("Alien\\aliendropping0005-removebg-preview.png").convert_alpha(),pygame.image.load("Alien\\aliendropping0006-removebg-preview.png").convert_alpha(),pygame.image.load("Alien\\aliendropping0007-removebg-preview.png").convert_alpha(),pygame.image.load("Alien\\aliendropping0008-removebg-preview.png").convert_alpha(),pygame.image.load("Alien\\aliendropping0009-removebg-preview.png").convert_alpha()]
ballAlienSign=pygame.image.load("Alien\darkgray__BulletSign.png").convert_alpha()
 
# ballR= pygame.image.load("hero\\ballRight.png").convert_alpha()
Lightning=[pygame.image.load("Objects\_Pngtree_light_effect_of_lightning_blue_6183369_Down-removebg-preview.png").convert_alpha(),pygame.image.load("Objects\_Pngtree_light_effect_of_lightning_blue_6183369_Right-removebg-preview.png").convert_alpha(),pygame.image.load("Objects\_Pngtree_light_effect_of_lightning_blue_6183369_UP-removebg-preview.png").convert_alpha(),pygame.image.load("Objects\_Pngtree_light_effect_of_lightning_blue_6183369_Lift-removebg-preview.png").convert_alpha()]

stamina= pygame.image.load("Objects\stamina.png").convert_alpha()

heart= pygame.image.load("Objects\imgbin_health-video-game-pixel-art-bar-png1-removebg-preview.png").convert_alpha()
boot= pygame.image.load("Objects\jumping_boot-removebg-preview.png").convert_alpha()

fireball1=[pygame.image.load("enemy\\nesak1.png").convert_alpha(),pygame.image.load("enemy\\nesak2.png").convert_alpha()]

fireball=[pygame.image.load("enemy\Fireball_Effect_01.png").convert_alpha(),pygame.image.load("enemy\Fireball_Effect_02.png").convert_alpha(),pygame.image.load("enemy\Fireball_Effect_03.png").convert_alpha(),pygame.image.load("enemy\Fireball_Effect_04.png").convert_alpha(),pygame.image.load("enemy\Fireball_Effect_05.png").convert_alpha()]


    
move__alien=[pygame.image.load("Alien\\armor__0006_walk_1.png").convert_alpha().convert_alpha(),pygame.image.load("Alien\\armor__0007_walk_2.png").convert_alpha(),pygame.image.load("Alien\\armor__0008_walk_3.png").convert_alpha(),pygame.image.load("Alien\\armor__0009_walk_4.png").convert_alpha(),pygame.image.load("Alien\\armor__0010_walk_5.png").convert_alpha(),pygame.image.load("Alien\\armor__0011_walk_6.png").convert_alpha()]
run__alien=[pygame.image.load("Alien\\armor__0012_run_1.png").convert_alpha(),pygame.image.load("Alien\\armor__0013_run_2.png").convert_alpha(),pygame.image.load("Alien\\armor__0014_run_3.png").convert_alpha(),pygame.image.load("Alien\\armor__0015_run_4.png").convert_alpha(),pygame.image.load("Alien\\armor__0016_run_5.png").convert_alpha(),pygame.image.load("Alien\\armor__0017_run_6.png").convert_alpha()]
idle__alien=[pygame.image.load("Alien\\armor__0000_idle_1.png").convert_alpha(),pygame.image.load("Alien\\armor__0001_idle_2.png").convert_alpha(),pygame.image.load("Alien\\armor__0002_idle_3.png").convert_alpha()]
fire__alien=[pygame.image.load("Alien\\armor__0035_fire_1.png").convert_alpha(),pygame.image.load("Alien\\armor__0036_fire_2.png").convert_alpha(),pygame.image.load("Alien\\armor__0037_fire_3.png").convert_alpha(),pygame.image.load("Alien\\armor__0038_fire_4.png").convert_alpha(),pygame.image.load("Alien\\armor__0039_fire_5.png").convert_alpha(),pygame.image.load("Alien\\armor__0040_fire_6.png").convert_alpha(),pygame.image.load("Alien\\armor__0041_fire_7.png").convert_alpha(),pygame.image.load("Alien\\armor__0042_fire_8.png").convert_alpha(),pygame.image.load("Alien\\armor__0043_fire_9.png").convert_alpha(),pygame.image.load("Alien\\armor__0044_fire_10.png").convert_alpha(),pygame.image.load("Alien\\armor__0045_fire_11.png").convert_alpha()]
attack__alien=[pygame.image.load("Alien\\armor__0031_attack_1.png").convert_alpha(),pygame.image.load("Alien\\armor__0032_attack_2.png").convert_alpha(),pygame.image.load("Alien\\armor__0033_attack_3.png").convert_alpha(),pygame.image.load("Alien\\armor__0034_attack_4.png").convert_alpha()]
hurt__alien=[pygame.image.load("Alien\\armor__0018_hurt_1.png").convert_alpha(),pygame.image.load("Alien\\armor__0019_hurt_2.png").convert_alpha(),pygame.image.load("Alien\\armor__0020_hurt_3.png").convert_alpha(),pygame.image.load("Alien\\armor__0021_hurt_4.png").convert_alpha()]
# jump__alien=[pygame.image.load("Alien\\armor__0027_jump_1.png").convert_alpha(),pygame.image.load("Alien\\armor__0028_jump_2.png").convert_alpha(),pygame.image.load("Alien\\armor__0029_jump_3.png").convert_alpha(),pygame.image.load("Alien\\armor__0030_jump_4.png").convert_alpha(),]
colors=[RED,BLUE2]
score = 0
healths=[]
destroyedBullets=[]
vector=Vector2()
Players=[]
blocks=[]

bullets=[]





ballAlienDestroyed2=[]
for i in range(len(ballAlienDestroyed)):
    ballAlienDestroyed2.append(pygame.transform.rotozoom(ballAlienDestroyed[i],0,5))

for i in range(len(ballAlienDestroyed)):
    ballAlienDestroyed[i]=pygame.transform.rotozoom(ballAlienDestroyed[i],0,1.2)

ballAlienSign=pygame.transform.rotozoom(ballAlienSign,0,0.75)
move2__alien=[]
for i in range(len(move__alien)):
    move2__alien.append(pygame.transform.flip(move__alien[i],True,False))
   
idle2__alien=[]
for i in range(len(idle__alien)):
    idle2__alien.append(pygame.transform.flip(idle__alien[i],True,False))
    

attack2__alien=[]
for i in range(len(attack__alien)):attack2__alien.append(pygame.transform.flip(attack__alien[i],True,False))
fire2__alien=[]
for i in range(len(fire__alien)):fire2__alien.append(pygame.transform.flip(fire__alien[i],True,False))
hurt2__alien=[]
for i in range(len(hurt__alien)):hurt2__alien.append(pygame.transform.flip(hurt__alien[i],True,False))

for i in range(len(ballsuperAlien)):
    ballsuperAlien[i]=pygame.transform.rotozoom(ballsuperAlien[i],90,1)

        # pygame.draw.rect(screen, RED, self.hitbox, 2)
class Alien:
    def __init__(self,index, x, y, health,width, height,id):
        self.index=index
        self.position,self.velocity=pygame.math.Vector2(x,y),0
        self.startX=180
        self.width = width
        self.height = height
        self.step = 7
        self.step2=-7
        self.left = False
        self.right = False
        self.LEFT_KEY=False
        self.RIGHT_KEY=False
        self.stop=1
        

        self.moves = 0
        
        self.is_jumping = False
        self.standing = True
        self.hitbox = (self.position[0]+20, self.position[1]+10, self.width-40, self.height-10)
        self.start_x = x
        self.start_y = y
        self.health = health
        self.startHealth=health
        self.stamina=15
        self.startStamina=50
        self.visible = True
        self.boot=0
        self.increase=self.startX+180*self.right-2*self.right*self.startX
        self.vec=Vector2()
        self.vec2=Vector2()
        self.speed = 10
        self.speed2 = 12
        self.JumpCount=0
        self.idleC=0
        self.attackC=0
        self.hitbox = (self.position[0]+20, self.position[1]+20, self.width-40, self.height-20)
        self.attackhitbox = (0,0,0,0)
        self.Attack=0
        self.Shoot=0
        self.Fire=0
        self.fireC=0
        self.move1=move2__alien
        self.move2=move__alien
        self.attack1=attack__alien
        self.attack2=attack2__alien
        self.idle1=idle__alien
        self.idle2=idle2__alien
        self.fire1=fire__alien
        self.fire2=fire2__alien
        self.hurt1=hurt2__alien
        self.hurt2=hurt__alien
        self.hurt=0
        self.hurtC=0
        self.ball=ballAlien
        self.direction=1*self.right-1*self.left
        self.id=id
        self.canmove=1
        self.bullets=[]
        self.superBullets=[]
        self.gravity,self.friction=1.24,-0.12
        self.acceleration=pygame.math.Vector2(0,self.gravity)
        self.max_vel=15
        self.direction=-1*self.left+1*self.right
        self.on_ground=False
        self.x_mid=(self.hitbox[0]+self.hitbox[0]+self.hitbox[2])//2
        self.y_mid=(self.hitbox[1]+self.hitbox[1]+self.hitbox[3])//2
        self.rect=Vector2(self.x_mid,self.y_mid)
        self.cooldownBullet=pygame.time.get_ticks()
        self.attackId=0
        self.onBlock=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.onBlockheight=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.xbullet=0
        self.superCooldown=pygame.time.get_ticks()
        self.canFire=1
#         # self.name = name
#         # self.price = price+20
#         self.amount = amount
    def Ypalance(self):
        # if self.position[1]>self.start_y:
        #     self.position[1]=self.start_y
 
        if self.position[0]+self.width>screen_width:
                self.position[0]=screen_width-self.width
               
        if self.position[0]<0:
            self.position[0]=0
    
    def update(self):
        
        if self.health>self.startHealth:
            self.health=self.startHealth
        if self.stamina>self.startStamina:
            self.stamina=self.startStamina
        self.draw(screen)
        self.vertical_movement(dt)
        self.checkAttack()
        self.Ypalance()
    def checkAttack(self):
        if(self.Attack==0):
            self.attackhitbox=(0,0,0,0)
        if self.canFire==0:
            supernewcooldown=pygame.time.get_ticks()
            if supernewcooldown-self.superCooldown>=15000:
                    self.canFire=1
                    self.superCooldown=supernewcooldown
    def draw(self, screen):
        self.rect=Vector2(self.x_mid,self.y_mid)
        
        self.hitbox = (self.position[0]+11, self.position[1]+20, self.width-25, self.height-21)

        self.x_mid=(self.hitbox[0]+self.hitbox[0]+self.hitbox[2])//2
        self.y_mid=(self.hitbox[1]+self.hitbox[1]+self.hitbox[3])//2
        self.direction=1*(-1*self.right+1*self.left)

        self.increase=self.startX+180*self.right-2*self.right*self.startX
        self.vec.from_polar((40,self.increase))
        self.vec2.from_polar((10,self.increase))
        if self.visible:
            if self.hurt==1:
                if self.left:
                        screen.blit(self.hurt1[self.hurtC//2], (self.position[0], self.position[1]))
                        self.hurtC += 1
                        if self.hurtC == 8:
                           
                            self.hurtc=0
                            self.hurt=0


                elif self.right:
                        screen.blit(self.hurt2[self.hurtC//2], (self.position[0], self.position[1]))
                        self.hurtC += 1
                        if self.hurtC == 8:
                            self.hurtC = 0
                            self.hurt=0
            else:    
                if not self.Attack:
                    if not self.Fire:
                           
                            if not self.standing:
                                if self.left:
                                    screen.blit(self.move1[self.moves//3], (self.position[0], self.position[1]))
                                    self.moves += 1
                                    if self.moves == 18:
                                        self.moves = 0

                                elif self.right:
                                    screen.blit(self.move2[self.moves//3], (self.position[0], self.position[1]))
                                    self.moves += 1
                                    if self.moves == 18:
                                        self.moves = 0

                            else:
                                
                                if self.right:
                                    screen.blit(self.idle1[self.idleC//18], (self.position[0], self.position[1]))
                                    self.idleC += 1
                                    if self.idleC == 54:
                                        self.idleC = 0
                                else:
                                    screen.blit(self.idle2[self.idleC//18], (self.position[0], self.position[1]))
                                    self.idleC += 1
                                    if self.idleC == 54:
                                            self.idleC = 0
                    else:
                            # self.step=1
                            # self.step2=-1
                            if self.right:
                                    screen.blit(self.fire1[self.fireC//1], (self.position[0], self.position[1]))
                                    self.fireC += 1
                                    
                                    if self.fireC==9:
                                            self.fireN()
                                    if self.fireC == 11:
                                        self.fireC = 0
                                        self.Fire=0
                                        
                                    
                            else:
                                    screen.blit(self.fire2[self.fireC//1], (self.position[0]-47, self.position[1]))
                                    self.fireC += 1
                                    if self.fireC==9:
                                            self.fireN()
                                    if self.fireC == 11:
                                            self.fireC = 0
                                            self.Fire=0

                else:                      
                                # self.step=1
                                # self.step2=-1
                                if self.right:
                                        screen.blit(self.attack1[self.attackC//2], (self.position[0], self.position[1]))
                                        self.attackC += 1
                                        if self.attackC>=2:
                                                    
                                            self.attackhitbox = (self.position[0]+60, self.position[1]+73, self.width+25, self.height-135)
                                            # pygame.draw.rect(screen, WHITE, self.attackhitbox, 2)

                                        if self.attackC == 8:
                                            self.attackC = 0
                                            self.Attack=0
                                            # self.step=5
                                            # self.step2=-5
                                        
                                else:
                                        screen.blit(self.attack2[self.attackC//2], (self.position[0]-89, self.position[1]))
                                        self.attackC += 1
                                        if self.attackC>=2:
                                            self.attackhitbox = (self.position[0]-85, self.position[1]+73, self.width+25, self.height-135)
                                            # pygame.draw.rect(screen, WHITE, self.attackhitbox, 2)

                                        if self.attackC == 8:
                                            self.attackC = 0
                                            self.Attack=0
                                            # self.step=5
                                            # self.step2=-5

                         
    

                
            pygame.draw.rect(
                screen, BLACK, (self.index-5, 13, self.startHealth*8+10, 40))
            pygame.draw.rect(
                screen, RED, (self.index-3, 15, self.startHealth*8+6, 36))
            pygame.draw.rect(
                screen, BLACK, (self.index-2, 16, self.startHealth*8+4, 34))
            pygame.draw.rect(
                screen, RED, (self.index, 18, self.startHealth*8, 30))
            pygame.draw.rect(
                screen, GREEN, (self.index, 18, self.health*8, 30))
    

            pygame.draw.rect(
                screen, BLACK, (self.index-5, 53, self.startStamina*8+10, 20))
            pygame.draw.rect(
                screen, WHITE, (self.index-3, 55, self.startStamina*8+6, 16))
            pygame.draw.rect(
                screen, BLACK, (self.index-2,56 , self.startStamina*8+4, 14))
            pygame.draw.rect(
                screen, RED, (self.index, 58, self.startStamina*8, 10))
            pygame.draw.rect(
                screen, BLUE, (self.index, 58, self.stamina*8, 10))
            fontHealth = pygame.font.Font("ComicNeue-Regular.ttf", 40)
            
            # text = fontHealth.render("Health", 1,WHITE)
            # screen.blit(text, (self.index-190, 35))
            # pygame.draw.line(screen, (200, 0, 0), self.position+(32,40)+self.vec, self.position+(32,40)+self.vec+self.vec2, 1)
            # pygame.draw.line(screen, (200, 0, 0), self.position+(32,40)+self.vec+self.vec2*3, self.position+(32,40)+self.vec+self.vec2*4, 1)

            font1 = pygame.font.Font("ComicNeue-Bold.ttf", 23)
            font2 = pygame.font.Font("ComicNeue-Bold.ttf", 70)
            font3 = pygame.font.Font("ComicNeue-Bold.ttf", 75)
            
            textP = font1.render(f"{self.id+1}", 1, colors[self.id])
            textP2 = font2.render(f"{self.id+1}", 1, colors[self.id])
            textPx = font3.render(f"{self.id+1}", 1, BLACK)

            screen.blit(textP, self.rect)
            
            screen.blit(textPx, (self.index-60,5))
            screen.blit(textP2, (self.index-60,7))

            if self.canFire==0:
                screen.blit(ballAlienSign,(self.index+420,30))
            # pygame.draw.rect(screen, RED, self.hitbox, 2)
            # pygame.draw.circle(screen,RED,(self.x_mid,self.y_mid),3)
        
    def attack(self):
          
        self.Attack=1
    def fire(self,x):
       
        self.Fire=1
        self.xbullet=x
    def fireN(self,bullet=0):

        if self.xbullet==0:
            self.bullets.append(AlienBullet(round(self.position[0]-60*self.direction+self.width//2),
                                           round(self.position[1]-13+self.height*2//3), self.direction, 20,self.increase,self.ball,1-self.id))
        if self.xbullet==1:
          
                if  bullet.destroyed==1:
                    for i in range(choice([13,14,15,16,17,18])):
                        self.bullets.append(AlienBullet(round(bullet.position2[0]+choice([80,-80,100,-100,50,-50])),  
                                     round(bullet.position[1]+choice([80,-80,100,-100,50,-50])), bullet.direction, 20,self.increase,self.ball,1-self.id))
                    self.destroyed=0
                    self.xbullet=0               
                    self.superBullets.remove(bullet)
        if self.xbullet==10:
            if self.stamina>=25:
                self.stamina-=25
                self.position[0]+=100*self.direction

                self.superBullets.append(AlienSuperBullet(round(self.position[0]-60*self.direction+self.width//2),
                                                round(self.position[1]-13+self.height*2//3), self.direction, 20,self.increase,self.ball,1-self.id))
  
    def shoot(self):
        self.Shoot=1
    def hit(self,x,position):
            self.hurtC=0
            self.hurt=1
      
            if x==0:
                if self.right and self.position[0]>position or self.left and self.position[0]<position:
                    self.canmove=0
                    
                    self.position[0] = self.position[0]-300*self.direction
                    self.canmove=1  
                    self.step=7
                    self.step2=-7
                else:
                    self.canmove=0
                    self.position[0] = self.position[0]+300*self.direction
                    self.canmove=1
                    self.step=7
                    self.step2=-7
                self.health-=choice([2.5,2.75,3,3.25,3.5])
            elif x==100:
                if self.right and self.position[0]>position:

                    self.position[0] = self.position[0]-10*self.direction
                else:
                     self.position[0] = self.position[0]+10*self.direction
              
            
                self.health-=choice([1,0.75,0.5])
            elif x==1000:
                
                if self.right and self.position[0]>position:

                    self.position[0] = self.position[0]-30*self.direction
                else:
                     self.position[0] = self.position[0]+30*self.direction
               
                self.health-=3
            elif x==101:
                if self.right and self.position[0]>position:

                    self.position[0] = self.position[0]-100*self.direction
                    self.position[1] = self.position[1]-100*self.direction


                else:
                     self.position[0] = self.position[0]+100*self.direction
                     self.position[1] = self.position[1]+100*self.direction
                self.canFire=0
                self.superCooldown=pygame.time.get_ticks()
                # screen.blit(explosion,self.rect)
                # screen.blit(explosion,self.rect)
                # screen.blit(explosion,self.rect)
                self.health-=choice([14,13.5,13,14.5,15,14])
              
                    

            self.moves = 0
        

            if self.health <= 0:
                self.visible = False
                self.hitbox = (0, 0, 0, 0)
                font1 = pygame.font.Font("ComicNeue-Bold.ttf", 130)
                screen.fill(BLACK)
                text = font1.render(f"Player {(1-self.id)+1} Won!", 1, RED)
                screen.blit(text, (400, 200))
         
                pygame.display.update()
                i = 0
                while i < 150:
                    i += 1
                    pygame.time.delay(20)
                quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
    def vertical_movement(self,dt):
        
        self.velocity+=self.acceleration.y*dt
        if self.velocity>7:self.velocity=7
        self.position.y+=self.velocity*dt+(self.acceleration.y*.5)*(dt*dt)
        for i in range(len(self.onBlock)-1):
            if self.position.y>585 or self.onBlock[i]==1:
                self.on_ground=True
                self.velocity=0
                    

                if self.onBlock[i]:
                    
                    self.position.y=self.onBlockheight[i]-self.height
                else:    

                    self.position.y=585
            elif self.position.y<80:
                self.velocity=0
            # self.rect.bottom=self.position.y
    def jump(self):
        
        if self.on_ground:
            self.is_jumping=True
            self.velocity-=23
            self.on_ground=False
class Bullet:
    def __init__(self, x, y, direction, step,sX,ball):
        self.position=Vector2(x,y)
        self.vec=Vector2()
        self.vec.from_polar((20,sX))
        self.color = BLACK
        self.direction = direction
        self.step = step*direction
        self.counter=0
        self.sX=sX
        self.id=100
        self.image=ball
        self.damage=1
        self.bunch=10
        self.view=1
        self.destroyed=0
    def draw(self, screen):
      
        #ball=pygame.transform.scale(ball,(25,25))
        if self.destroyed==0:
            rotated_image = pygame.transform.rotozoom(self.image, -self.sX,.5)
            new_rect = rotated_image.get_rect(center = self.image.get_rect(topleft = (self.position[0]-35,self.position[1]-32)).center)
            if self.view==1:
                screen.blit(rotated_image, new_rect)
        

        # pygame.draw.circle(screen, self.color, (self.position[0], self.position[1]), 7)
        # if self.direction>0:
        #     screen.blit(ballR,(self.position[0],self.position[1]-10))
        # else: 
        #     screen.blit(ballL,(self.position[0],self.position[1]-10))
    # def move(self):
    #     for i in Players:
    #         for bullet in i.bullets:
    #                 if i.id!=self.id:
    #                     if bullet.position[0] > i.hitbox[0] and bullet.position[0] < i.hitbox[0]+i.hitbox[2]:
    #                         if bullet.position[1] > i.hitbox[1] and bullet.position[1] < i.hitbox[1]+i.hitbox[3]:
    #                             i.hit()
    #                             i.bullets.remove(bullet)
    #                     if bullet.position[0] < screen_width and bullet.position[0] > 0:
    #                             bullet.position += bullet.vec
    #                             bullet.counter+=1
    #                     else:
    #                         i.bullets.remove(bullet)
class AlienBullet(Bullet):
    def __init__(self, x, y, direction, step,sX,ball,Id):
        Bullet.__init__(self, x, y, direction, step,sX,ball)
        super().__init__(x,y,direction,step,sX,ball)
        self.id=Id
        self.vel=pygame.Vector2()
        self.vec=pygame.Vector2()
        self.vec.from_polar((16,sX))
        self.cooldown=pygame.time.get_ticks()
        self.trace=1
        self.count=0
        
    def draw(self,screen):
        # self.position += self.vel
        # self.rect.center = self.position
        if self.trace==1:
            if abs(self.position.x-Players[self.id].position.x)<=500:
                if abs(self.position.y-Players[self.id].position.y)<=200:
                    _, self.sX = ((Players[self.id].rect)-self.position).as_polar()
        newcooldown=pygame.time.get_ticks()

        if newcooldown-self.cooldown>=choice([300,400,500,200,100,300,300,300]):
          self.trace=0  

          if abs(self.position.x-Players[self.id].position.x)<=500:
              if abs(self.position.y-Players[self.id].position.y)<=200:
                   _, self.sX = ((Players[self.id].rect)-self.position).as_polar()
          self.cooldown=newcooldown
        self.vec.from_polar((choice([14,13,12,11]), self.sX))
        rotated_image = pygame.transform.rotozoom(self.image, -self.sX,.5)
        new_rect = rotated_image.get_rect(center = self.image.get_rect(topleft = (self.position[0]-35,self.position[1]-32)).center)
        if self.view==1:
                if self.destroyed==0:

                    screen.blit(rotated_image, new_rect)
        # else:   
        #         if self.destroyed==0:
        #           screen.blit(ballAlienDestroyed[self.count//2],new_rect)
        #           self.count+=1
        #           if self.count==6:
        #               self.count=0
        #               self.destroyed=0
class AlienDestroyed():
    def __init__(self,position,image):
        self.position=position
        self.counter=0
        self.image=image
        self.rect=self.image[0].get_rect()
    def draw(self,screen):
        self.rect.center=self.position
        screen.blit(self.image[self.counter//5],self.rect)
        self.counter+=1
        if self.counter==10:
            self.counter=0
            destroyedBullets.remove(self)

class AlienSuperBullet(AlienBullet):
    def __init__(self, x, y, direction, step,sX,ball,Id):
        AlienBullet.__init__(self, x, y, direction, step,sX,ball,Id)
        super().__init__( x, y, direction, step,sX,ball,Id)
        self.image=[]
        self.image=ballsuperAlien
        self.rect=self.image[0].get_rect()
        self.position2=Vector2(x,y)
        self.xvec=Vector2()
        self.destroyed=0
    def draw(self, screen):
        self.rect=self.image[0].get_rect()
        
        self.rect.center=self.position2
        self.position=self.position2+self.vec*2
        _, self.sX = ((Players[self.id].rect)-self.position2).as_polar()
        newcooldown=pygame.time.get_ticks()

        if newcooldown-self.cooldown>=20:
           


            _, self.sX = ((Players[self.id].rect)-self.position2).as_polar()
            self.cooldown=newcooldown
        self.vec.from_polar((15, self.sX))
        
        
            
        rotated_image = pygame.transform.rotozoom(self.image[self.count], -self.sX,1)
       
        # if self.view==1:
        screen.blit(rotated_image, self.rect)
        self.count+=1
        if self.count==9:
            self.count=0
        # pygame.draw.circle(screen ,BLUE2,self.position2+self.vec*2,5)
        # self.hitbox=(self.position[0]-30,self.position[1]-25,120,50)
        # self.hitbox=pygame.transform.rotozoom(self.hitbox,-self.sX,1)
        # pygame.draw.rect(screen,RED,self.hitbox,2)
        
class Block:
    def __init__(self,x,y,image,height,width,first,last,step,code):
         self.position=Vector2(x,y)
         self.image=pygame.transform.rotozoom(image,0,.5)
         self.rect=self.image.get_rect()
         self.step=step
         self.height=height
         self.width=width
         self.first=first
         self.last=last
         self.code=code
         self.hitbox=0
    def draw(self,screen):

        self.rect.center=self.position
        self.hitbox=(self.position.x-self.width//2,self.position.y-self.height//2,self.width,self.height)

        screen.blit(self.image,self.rect)
    def update(self):
       
        
        self.move(Players)
        self.Break(Players)
        # pygame.draw.circle(screen,(0,0,0),(self.position.x,self.position.y),2)
        # pygame.draw.circle(screen,(0,0,0),(self.position.x,self.position.y-40),2)
        # pygame.draw.circle(screen,(0,0,0),(man2.rect[0],man2.rect[1]+man2.height//2-10),5)
    def Break(self,Players):
        bloCk=[0,1]

        for i in bloCk:
            for bullet in Players[i].bullets:
                if bullet.position.x>self.position.x-self.width//2 and bullet.position.x<self.position.x+self.width//2:
                    if bullet.position.y>self.position.y-self.height//2 and bullet.position.y<self.position.y+self.height//2:
                        if len(Players[i].bullets)>=1:
                            Players[i].bullets.remove(bullet)
                        else:
                            pass
            for bullet in Players[i].superBullets:
                if bullet.position.x>self.position.x-self.width//2 and bullet.position.x<self.position.x+self.width//2 and  bullet.position.y>self.position.y-self.height//2 and bullet.position.y<self.position.y+self.height//2:
                        if len(Players[i].superBullets)>=1:
                            bullet.destroyed=1
                            Players[i].fire(1)
                            Players[i].fireN(bullet)
                            

                            
                        else:
                            pass
    def move(self,Players):
        self.position.y+=self.step
        if self.position.y>=self.last:
            self.step*=-1
        if self.position.y<=self.first:
          self.step*=-1
        bloCk=[0,1]
        for i in bloCk:
        #     height=i.height//2
            if  self.position.y-20+abs(self.step)*2<(Players[i].rect[1]+Players[i].height//2-10) and self.position.y+7>(Players[i].rect[1]+Players[i].height//2-10) and Players[i].rect[0]>self.position.x-self.width//2-3 and Players[i].rect[0] <self.position.x+self.width//2+3:
                        Players[i].onBlock[self.code]=1
                        if self.step==0:
                             Players[i].onBlockheight[self.code]=self.position.y-19
                        else:

                            Players[i].onBlockheight[self.code]=self.position.y-25
                        
                        
                        # man2.on_ground=True
            else:
                        
                        Players[i].onBlock[self.code]=0
        # if  self.position.y-20.<(man.rect[1]+man.height//2-10) and self.position.y>(man.rect[1]+man.height//2-10) and man.rect[0]>self.position.x-self.width//2 and man.rect[0] <self.position.x+self.width//2:
        #             man.onBlock=1
        #             man.onBlockheight=self.position.y-25
                    
        #             # man2.on_ground=True
        # else:
        #             man.onBlock=0
# class Block2(Block):
#     def __init__(self,x,y,image,height,width,first,step):
#         Block.__init__(self,x,y,image,height,width,first,step)
#         super().__init__(x,y,image,height,width,first,step)
        
class FireBall:
    def __init__(self, y, step):
        self.x = (choice([randint(10,1390),randint(1100,1390),randint(10,300)]))
        self.y = y
        self.moves=0
        self.moves2=0
        self.visible=1
        self.die=0
        self.step = step

    def draw(self, screen):
        if self.visible==1:
        # pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            # screen.blit(fireball[self.moves],(self.x,self.y-10))
            pygame.draw.circle(screen,BLACK,(self.x,self.y),10)

            screen.blit(fireball1[self.moves],(self.x-29,self.y-173))
            # screen.blit(fireball[self.moves],(self.x,self.y))
            self.moves+=1
            if self.moves==1:
                self.moves=0
        elif self.visible==0:
         
           screen.blit(Lightning[self.moves2//1],(self.x-88,self.y-200))
           self.moves2+=1
           if self.moves2==4:
             self.die=1
             self.moves2=0
  
class Sword():
    def __init__(self,x1=Alien):
        self.pole=x1.position
        self.vec=Vector2()
        self.c=x1.direction
        self.vec.from_polar((50,60*self.c))
    def draw(self,screen):
        self.vec.from_polar((50,300+((self.c+1)*(90-300))))
        
        # pygame.draw.line(screen,(0,0,0),(self.pole[0]+30,self.pole[1]+45),(self.pole[0]+30,self.pole[1]+50)+self.vec,4)
        # pygame.draw.line(screen,(0,0,0),(self.pole[0]+30,self.pole[1]+45),(self.pole[0]+30,self.pole[1]+50)+self.vec,4)


class Potion():
    def __init__(self,x,y,type,image):
        self.x=x
        self.y=y
        self.height=40
        self.width=40
        self.type=type
        if self.type==1:
            self.image=[pygame.transform.rotozoom(heart,0,.8),pygame.transform.rotozoom(heart,0,.7)]
            self.width=22
            self.height=22
        if self.type==2:
            self.image=[heart,pygame.transform.rotozoom(heart,0,.88)]
            self.width=27
            self.height=27
        if self.type==3:
            self.image=[pygame.transform.rotozoom(heart,0,1.4),pygame.transform.rotozoom(heart,0,1.2)]
            self.width=38
            self.height=38
        if self.type==4:
            self.image=[pygame.transform.rotozoom(heart,0,2),pygame.transform.rotozoom(heart,0,1.75)]
            self.width=54
            self.height=54
        if self.type==11:
            self.image=[pygame.transform.rotozoom(stamina,0,.11),pygame.transform.rotozoom(stamina,0,.1)]
            self.width=16
            self.height=24
        if self.type==12:
            self.image=[pygame.transform.rotozoom(stamina,0,.15),pygame.transform.rotozoom(stamina,0,.135)]
            self.width=22
            self.height=33
        if self.type==13:
            self.image=[pygame.transform.rotozoom(stamina,0,.18),pygame.transform.rotozoom(stamina,0,.16)]
            self.width=26
            self.height=39
        
        self.visible=1
        self.rect=[self.image[0].get_rect(),self.image[1].get_rect()]
        self.hitbox=(self.rect[0][0]-self.width//2,self.rect[0][1]-self.height//2,self.width,self.height) 
        self.i=0
    def draw(self,screen):
       
        self.rect[0].center=Vector2(self.x,self.y)
        self.rect[1].center=Vector2(self.x,self.y)
        self.hitbox=(self.rect[0].center[0]-self.width//2,self.rect[0].center[1]-self.height//2,self.width,self.height) 
        

        if self.visible==1:
                        # screen.blit(ballR,(self.x,self.y-10))
            # pygame.draw.rect(screen,RED,self.hitbox)
         
            
            screen.blit(self.image[self.i//15],self.rect[self.i//15])
            self.i+=1
            if self.i==30:
               self. i=0
    def healthing(self, i):
        if self.type==1:
            i.health+=choice([3,2,4])
        if self.type==2:
            i.health+=choice([4,5,6])
        if self.type==3:
            i.health+=choice([10,8,13])
        if self.type==4:
            i.health+=choice([25,21,29])
        if self.type==11:
            i.stamina+=choice([3,2,4])
        if self.type==12:
            i.stamina+=choice([5,4,6])
        if self.type==13:
            i.stamina+=choice([8,10,12])
man = Alien(1010,1200, 570,50, 60, 120,0)
man2 = Alien(110,200, 570, 50,60, 120,1)

man.left=1
man2.right=1

block2=Block(1030,choice([500,600,400,450,550,650,350]),block1,48,48,320,670,2,0)
block3=Block(100,choice([500,600,400,450,550,650,350]),block1,48,48,320,670,4,1)
Players.append(man)
Players.append(man2)
# sword=Sword(man)
# man2 = Player(100, 400, 64, 64)

block11=Block(500,choice([500,600,400,450,550,650,350]),block1,48,48,320,670,2,2)
block12=Block(1430,choice([500,600,400,450,550,650,350]),block1,48,48,320,670,4,3)
block51=Block(765,400,block1,48,48,350,450,1,4)
block52=Block(671,400,block1,48,48,350,450,1,5)
block53=Block(718,400,block1,48,48,350,450,1,6)
block54=Block(859,400,block1,48,48,350,450,1,7)
block55=Block(812,400,block1,48,48,350,450,1,8)

block41=Block(337,453,block1,48,48,233,473,1,9)
block42=Block(337,500,block1,48,48,280,520,1,11)
block43=Block(290,500,block1,48,48,280,520,1,10)


block31=Block(1199,453,block1,48,48,233,473,1,12)
block32=Block(1199,500,block1,48,48,280,520,1,13)
block33=Block(1246,500,block1,48,48,280,520,1,14)


blocks.append(block2)
blocks.append(block3)
blocks.append(block11)
blocks.append(block12)
blocks.append(block51)
blocks.append(block52)
blocks.append(block53)
blocks.append(block54)
blocks.append(block55)
blocks.append(block41)
# blocks.append(block42)
blocks.append(block43)
blocks.append(block31)
# blocks.append(block32)
blocks.append(block33)


# blocks.append(block11)
# blocks.append(block2)
# blocks.append(block3)
font = pygame.font.Font("ComicNeue-Bold.ttf", 35)


def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

def releaseFireBall():
    
        fireball=FireBall(100,(15*randrange(1,4)))
        fireballs.append(fireball)

def redrawGame():
   
    
    screen.blit(bg, (0, 0))
    

    # enemy2.draw(screen)
    # for block in blocks:
    #     block.update(screen)
    for i in blocks:
        i.draw(screen)
        i.update()
    for i in destroyedBullets:
        i.draw(screen)
    # sword.draw(screen)
    # sword.c=man.direction

    if man.boot==1:
        screen.blit(boot,(360,30))
    # man2.draw(screen)
    for i in Players:
        for Bullet in i.bullets:
            Bullet.draw(screen)
        for Bullet in i.superBullets:
            Bullet.draw(screen)
    for fireball in fireballs:
        fireball.draw(screen)
    
    for health in healths:
        health.draw(screen)
    man.update()
    man2.update()
    # pygame.draw.circle(screen,(0,0,0),(765,77),2)

    pygame.display.flip()



fireballs=[]

font3 = pygame.font.Font("ComicNeue-Bold.ttf", 50)


i = 0
timeup=10000

time1 = pygame.time.get_ticks()
time3 = datetime.datetime.now().time().second
time4 = datetime.datetime.now().time().second
cooldown1=pygame.time.get_ticks()
cooldown2=pygame.time.get_ticks()

timeBoot=datetime.datetime.now().time().second
cooldownEnemies=pygame.time.get_ticks()
cooldownFireball=pygame.time.get_ticks()
cooldownAttack=pygame.time.get_ticks()
cooldownAttack1=pygame.time.get_ticks()
cooldownAttack22=pygame.time.get_ticks()
cooldownAttack2=pygame.time.get_ticks()
global cooldownBoot
cooldownBullet=pygame.time.get_ticks()
cooldownBullet2=pygame.time.get_ticks()
cooldownBoot=pygame.time.get_ticks()

SUPERattack=0


while True:#key==1:

    
    NtimeBoot=datetime.datetime.now().time().second
        # screen.fill(BLACK)
    
    time2 = pygame.time.get_ticks()
    time5=datetime.datetime.now().time().second
    dt=clock.tick(30)*.001*30

    # clock.tick(30)
    now1=pygame.time.get_ticks()  
    

    # pygame.key.set_repeat(1000, 0)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            exit()
        if event.type == pygame.KEYDOWN:
          
            nowAttack1=pygame.time.get_ticks()
            if nowAttack1-cooldownAttack1>=500:
                        if event.key==pygame.K_KP_1:
                            man.attack()
                            cooldownAttack1=nowAttack1
                        nowBullet=pygame.time.get_ticks()
            nowAttack22=pygame.time.get_ticks()
            if nowAttack22-cooldownAttack22>=500:
                        if event.key==pygame.K_g:
                            man2.attack()
                            cooldownAttack22=nowAttack22
            nowBullet=pygame.time.get_ticks()
            if nowBullet-cooldownBullet>=600:
                    if man.canFire:
                        if event.key==pygame.K_KP_2:
                            man.fire(0)
                        elif event.key==pygame.K_KP_5:
                            man.fire(10)
                            # man.position[0]+=100*man.direction

                            cooldownBullet=nowBullet
            nowBullet2=pygame.time.get_ticks()
            if nowBullet2-cooldownBullet2>=600:
                    if man2.canFire:
                        if event.key==pygame.K_h:
                            man2.fire(0)
                        elif event.key==pygame.K_y:
                            man2.fire(10)
                            # man2.position[0]+=100*man2.direction

                            cooldownBullet2=nowBullet2

    # for bullet in bullets:
    #     for i in enemys:
    #         if bullet.position[0] > i.hitbox[0] and bullet.position[0] < i.hitbox[0]+i.hitbox[2]:
    #             if bullet.position[1] > i.hitbox[1] and bullet.position[1] < i.hitbox[1]+i.hitbox[3]:
    #                 i.hit()
    #                 i.touched+=1
    #                 SUPERattack+=1

    #                 for i in bullets:
    #                     if len(bullets)>0:
    #           
    #               bullets.remove(i)
    if man.hitbox[1]<man2.attackhitbox[1] and man.hitbox[1]+man.hitbox[3]>man2.attackhitbox[1] +man2.attackhitbox[3]:
        if (man.position[0]>man2.position[0] and ((man2.attackhitbox[0]+man2.attackhitbox[2]>man.hitbox[0] and man2.attackhitbox[0]+man2.attackhitbox[2] < man.hitbox[0]+man.hitbox[2]) or (man2.attackhitbox[0]+man2.attackhitbox[2] >man.hitbox[0]+man.hitbox[2] and (man2.attackhitbox[0]<man.hitbox[0] or (man2.attackhitbox[0]>man.hitbox[0] and man2.attackhitbox[0]<man.hitbox[0]+man.hitbox[2]))))) or (man.position[0]<man2.position[0] and ((man2.attackhitbox[0]< man.hitbox[0]+man.hitbox[2] and man2.attackhitbox[0]>man.hitbox[0])or(man2.attackhitbox[0]<man.hitbox[0] and( man2.attackhitbox[0]+man2.attackhitbox[2]>man.hitbox[0]+man.hitbox[2] or (man2.attackhitbox[0]+man2.attackhitbox[2]<man.hitbox[0]+man.hitbox[2] and man2.attackhitbox[0]+man2.attackhitbox[2]>man.hitbox[0]))))):
                newAttack=pygame.time.get_ticks()
                if newAttack-cooldownAttack>=500:
                        man.hit(0,man2.position[0])
                        cooldownAttack=newAttack
    if man2.hitbox[1]<man.attackhitbox[1] and man2.hitbox[1]+man2.hitbox[3]>man.attackhitbox[1] +man.attackhitbox[3]:
        if (man2.position[0]>man.position[0] and ((man.attackhitbox[0]+man.attackhitbox[2]>man2.hitbox[0] and man.attackhitbox[0]+man.attackhitbox[2] < man2.hitbox[0]+man2.hitbox[2]) or (man.attackhitbox[0]+man.attackhitbox[2] >man2.hitbox[0]+man2.hitbox[2] and (man.attackhitbox[0]<man2.hitbox[0] or (man.attackhitbox[0]>man2.hitbox[0] and man.attackhitbox[0]<man2.hitbox[0]+man2.hitbox[2]))))) or (man2.position[0]<man.position[0] and ((man.attackhitbox[0]< man2.hitbox[0]+man2.hitbox[2] and man.attackhitbox[0]>man2.hitbox[0])or(man.attackhitbox[0]<man2.hitbox[0] and (man.attackhitbox[0]+man.attackhitbox[2]>man2.hitbox[0]+man2.hitbox[2] or (man.attackhitbox[0]+man.attackhitbox[2]<man2.hitbox[0]+man2.hitbox[2] and man.attackhitbox[0]+man.attackhitbox[2]>man2.hitbox[0]))))):
                newAttack2=pygame.time.get_ticks()
                if newAttack2-cooldownAttack2>=500:
                        man2.hit(0,man.position[0])
                        cooldownAttack2=newAttack2
              
    for bullet in man.bullets:
        
        if bullet.position[1]<man2.attackhitbox[1]  and bullet.position[1]>man2.attackhitbox[1]+man2.attackhitbox[3] and bullet.position[0]> man2.attackhitbox[0] and bullet.position[0]<man2.attackhitbox[0]+man2.attackhitbox[2]:
                   
                    if len(man.bullets)>=1:
                            man.bullets.remove(bullet)
        
        if bullet.position[0] > man2.hitbox[0] and bullet.position[0] < man2.hitbox[0]+man2.hitbox[2] and bullet.position[1] > man2.hitbox[1] and bullet.position[1] < man2.hitbox[1]+man2.hitbox[3]:
                bullet.destroyed=1
                destroyedBullets.append(AlienDestroyed(bullet.position,ballAlienDestroyed))
                
                man2.hit(100,bullet.position[0])
                if len(man.bullets)>=1:
                            man.bullets.remove(bullet)
        elif bullet.position[0] > man.hitbox[0] and bullet.position[0] < man.hitbox[0]+man.hitbox[2] and bullet.position[1] > man.hitbox[1] and bullet.position[1] < man.hitbox[1]+man.hitbox[3]:
                bullet.destroyed=1
                destroyedBullets.append(AlienDestroyed(bullet.position,ballAlienDestroyed))
               
                man.hit(100,bullet.position[0])
                if len(man.bullets)>=1:
                            man.bullets.remove(bullet)
        else:
            for health in healths:
                if bullet.position[0] > health.hitbox[0] and bullet.position[0] < health.hitbox[0]+health.hitbox[2] and bullet.position[1] > health.hitbox[1] and bullet.position[1] < health.hitbox[1]+health.hitbox[3]:
                        healths.remove(health)
                        bullet.destroyed=1
                        
                        if len(man.bullets)>=1:
                                man.bullets.remove(bullet)
        if bullet.position[0] < screen_width and bullet.position[0] > 0:
                    bullet.position += bullet.vec
                    bullet.counter+=1
        else:    
            bullet.view=0
            if len(man.bullets)>=1:
                 man.bullets.remove(bullet)
    for bullet in man2.bullets:
        if bullet.position[1]<man.attackhitbox[1]  and bullet.position[1]>man.attackhitbox[1]+man.attackhitbox[3] and bullet.position[0]> man.attackhitbox[0] and bullet.position[0]<man.attackhitbox[0]+man.attackhitbox[2]:
                    if len(man2.bullets)>=1:
                            man2.bullets.remove(bullet)
        if bullet.position[0] > man.hitbox[0] and bullet.position[0] < man.hitbox[0]+man.hitbox[2] and bullet.position[1] > man.hitbox[1] and bullet.position[1] < man.hitbox[1]+man.hitbox[3]:
                bullet.destroyed=1
                destroyedBullets.append(AlienDestroyed(bullet.position,ballAlienDestroyed))

                man.hit(100,bullet.position[0])
                if len(man2.bullets)>=1:
                            man2.bullets.remove(bullet)
        elif bullet.position[0] > man2.hitbox[0] and bullet.position[0] < man2.hitbox[0]+man2.hitbox[2] and  bullet.position[1] > man2.hitbox[1] and bullet.position[1] < man2.hitbox[1]+man2.hitbox[3]:
                bullet.destroyed=1
                destroyedBullets.append(AlienDestroyed(bullet.position,ballAlienDestroyed))
                
                man2.hit(100,bullet.position[0])
                if len(man2.bullets)>=1:
                            man2.bullets.remove(bullet)
        else:
            for health in healths:
                if bullet.position[0] > health.hitbox[0] and bullet.position[0] < health.hitbox[0]+health.hitbox[2] and bullet.position[1] > health.hitbox[1] and bullet.position[1] < health.hitbox[1]+health.hitbox[3]:
                        healths.remove(health)
                        bullet.destroyed=1
                        
                        if len(man2.bullets)>=1:
                                man2.bullets.remove(bullet)
        if bullet.position[0] < screen_width and bullet.position[0] > -50:
                    bullet.position += bullet.vec
                    bullet.counter+=1
        else:  
            
            if len(man2.bullets)>=1:
              man2.bullets.remove(bullet)
                 

                  
    for bullet in man.superBullets:
        
        if bullet.position[1]<man2.attackhitbox[1]  and bullet.position[1]>man2.attackhitbox[1]+man2.attackhitbox[3] and bullet.position[0]> man2.attackhitbox[0] and bullet.position[0]<man2.attackhitbox[0]+man2.attackhitbox[2]:
                   
                    if len(man.superBullets)>=1:
                            man.superBullets.remove(bullet)
        
        if bullet.position[0] > man2.hitbox[0] and bullet.position[0] < man2.hitbox[0]+man2.hitbox[2] and bullet.position[1] > man2.hitbox[1] and bullet.position[1] < man2.hitbox[1]+man2.hitbox[3]:
                bullet.destroyed=1
                destroyedBullets.append(AlienDestroyed(bullet.position,ballAlienDestroyed2))
                
                man2.hit(101,bullet.position[0])
                if len(man.superBullets)>=1:
                            man.superBullets.remove(bullet)
        elif bullet.position[0] > man.hitbox[0] and bullet.position[0] < man.hitbox[0]+man.hitbox[2] and bullet.position[1] > man.hitbox[1] and bullet.position[1] < man.hitbox[1]+man.hitbox[3]:
                bullet.destroyed=1
                destroyedBullets.append(AlienDestroyed(bullet.position,ballAlienDestroyed2))
               
                man.hit(101,bullet.position[0])
                if len(man.superBullets)>=1:
                            man.superBullets.remove(bullet)
        for health in healths:
            if bullet.position[0] > health.hitbox[0] and bullet.position[0] < health.hitbox[0]+health.hitbox[2] and bullet.position[1] > health.hitbox[1] and bullet.position[1] < health.hitbox[1]+health.hitbox[3]:
                    healths.remove(health)
                    bullet.destroyed=1
                    
                
        if bullet.position2[0] < screen_width and bullet.position2[0] > 0:
                    bullet.position2 += bullet.vec
                    bullet.counter+=1
        else:    
            bullet.view=0
            if len(man.superBullets)>=1:
                 man.superBullets.remove(bullet)
    for bullet in man2.superBullets:
        if bullet.position[1]<man.attackhitbox[1]  and bullet.position[1]>man.attackhitbox[1]+man.attackhitbox[3] and bullet.position[0]> man.attackhitbox[0] and bullet.position[0]<man.attackhitbox[0]+man.attackhitbox[2]:
                    if len(man2.superBullets)>=1:
                            man2.superBullets.remove(bullet)
        if bullet.position[0] > man.hitbox[0] and bullet.position[0] < man.hitbox[0]+man.hitbox[2] and bullet.position[1] > man.hitbox[1] and bullet.position[1] < man.hitbox[1]+man.hitbox[3]:
                bullet.destroyed=1
                destroyedBullets.append(AlienDestroyed(bullet.position,ballAlienDestroyed2))
                man.hit(101,bullet.position[0])
                if len(man2.superBullets)>=1:
                            man2.superBullets.remove(bullet)
        elif bullet.position[0] > man2.hitbox[0] and bullet.position[0] < man2.hitbox[0]+man2.hitbox[2] and  bullet.position[1] > man2.hitbox[1] and bullet.position[1] < man2.hitbox[1]+man2.hitbox[3]:
                bullet.destroyed=1
                destroyedBullets.append(AlienDestroyed(bullet.position,ballAlienDestroyed2))
                
                man2.hit(101,bullet.position[0])
                if len(man2.superBullets)>=1:
                            man2.superBullets.remove(bullet)
        for health in healths:
            if bullet.position[0] > health.hitbox[0] and bullet.position[0] < health.hitbox[0]+health.hitbox[2] and bullet.position[1] > health.hitbox[1] and bullet.position[1] < health.hitbox[1]+health.hitbox[3]:
                    healths.remove(health)
                    bullet.destroyed=1
                    
                  
        if bullet.position2[0] < screen_width and bullet.position2[0] > -50:
                    bullet.position2 += bullet.vec
                    bullet.counter+=1
        else:  
            
            if len(man2.superBullets)>=1:
              man2.superBullets.remove(bullet)
                 


    for fireball in fireballs:
   
        for i in Players:
            if fireball.x > i.hitbox[0]-15 and fireball.x < i.hitbox[0]+i.hitbox[2]+15:
                if fireball.y > i.hitbox[1] and fireball.y < i.hitbox[1]+i.hitbox[3]:
                        
                        i.hit(1000,fireball.x)
                        fireball.visible=0
                    
                        
            
        for block in blocks:

                if fireball.x > block.hitbox[0] and fireball.x < block.hitbox[0]+block.hitbox[2]:
                    if fireball.y > block.hitbox[1] and fireball.y < block.hitbox[1]+block.hitbox[3]:
                        fireball.visible=0
                        
                       
  
        if fireball.y < screen_height and fireball.y > 0:
                 fireball.y += fireball.step
        else:
               fireball.visible=0
                #  fireballs.remove(fireball)
        if fireball.die==1:
            fireballs.remove(fireball)



    for health in healths:
        for i in Players:
            if i.attackhitbox[0] < health.rect[0].center[0] and i.attackhitbox[0]+i.attackhitbox[2] > health.rect[0].center[0] and i.attackhitbox[1] < health.rect[0].center[1] and i.attackhitbox[1]+i.hitbox[3] > health.rect[0].center[1]:
                      healths.remove(health)
            elif i.hitbox[0] < health.rect[0].center[0] and i.hitbox[0]+i.hitbox[2] > health.rect[0].center[0] and i.hitbox[1] < health.rect[0].center[1] and i.hitbox[1]+i.hitbox[3] > health.rect[0].center[1]:
                      health.healthing(i)
                      healths.remove(health)
                     
        for fireball in fireballs:
                    if fireball.x>health.hitbox[0] and fireball.x <health.hitbox[0]+health.hitbox[2] and fireball.y > health.hitbox[1] and fireball.y<health.hitbox[1]+health.hitbox[3]:
                          healths.remove(health)
    
        
    # for bullet in bullets2:

    #     if bullet.position[0] > man.hitbox[0] and bullet.position[0] < man.hitbox[0]+man.hitbox[2]:
    #         if bullet.position[1] > man.hitbox[1] and bullet.position[1] < man.hitbox[1]+man.hitbox[3]:
    #             man.hit()
    #             bullets2.remove(bullet)

        # if bullet.position[0] > enemy2.hitbox[0] and bullet.position[0] < enemy2.hitbox[0]+enemy2.hitbox[2]:
        # if bullet.position[1] > enemy2.hitbox[1] and bullet.position[1] < enemy2.hitbox[1]+enemy2.hitbox[3]:
        #     bullets.remove(bullet)
        #     enemy2.hit()
        #     score += 1
        # if bullet.position[0] < screen_width and bullet.position[0] > 0:
        #     bullet.position[0] += bullet.step
        # else:

        #     bullets2.remove(bullet)

    if keys[pygame.K_LEFT] and man.position[0]-man.step >= 0:
        if man.canmove==1:
                    man.step=7
                    man.position[0] += man.step2
                    man.step2-=0.15
                    if man.step2<-13:
                        man.step2=-13
                    man.left = True
                    man.right = False
                    man.standing = False
                

    elif keys[pygame.K_RIGHT] and man.position[0]+man.width+man.step <= screen_width:
        if man.canmove==1:
                man.step2=-7
                man.position[0] += man.step
                man.step+=0.15
                if man.step>13:
                    man.step=13
                man.right = True
                man.left = False
                man.standing = False
                
    
    else:
        if man.step>7:
            man.position[0]+=man.step
            man.step*=0.93
            if man.step<=7:
                man.step=7
        elif man.step2<-7:
            man.position[0]+=man.step2
            man.step2*=0.93
            if man.step2>=-7:
               man.step2=-7
        man.standing = True
        man.moves = 0
    if keys[pygame.K_UP]:
        if man.canmove:
             man.jump()
    if event.type==pygame.KEYUP:    
        if event.key==pygame.K_UP:
            if man.is_jumping:
                while(man.velocity<0):
                     man.velocity+=1
                man.is_jumping=False

    if keys[pygame.K_KP_6]:
        if man.startX-180<=60:
           man.startX+=2

    elif keys[pygame.K_KP_4]:
        if man.startX-180>=-60:

            man.startX-=2


        ###########3333333333333333
        ##############
  

   
  

    
        





    if keys[pygame.K_a] and man2.position[0]-man2.step >= 0:
        if man2.canmove:
                man2.step=7
                man2.position[0] += man2.step2
                man2.step2-=0.15
                if man2.step2<-13:
                   man2.step2=-13
                man2.left = True
                man2.right = False
                man2.standing = False
                

    elif keys[pygame.K_d] and man2.position[0]+man2.width+man2.step <= screen_width:
        if man2.canmove:
                man2.step2=-7
                man2.position[0] += man2.step
                man2.step+=0.15
                if man2.step>13:
                    man2.step=13
                man2.right = True
                man2.left = False
                man2.standing = False
                
    
    else:
        if man2.step>7:
            man2.position[0]+=man2.step
            man2.step*=0.93
            if man2.step<=7:
                man2.step=7
        elif man2.step2<-7:
            man2.position[0]+=man2.step2
            man2.step2*=0.93
            if man2.step2>=-7:
               man2.step2=-7
        man2.standing = True
        man2.moves = 0
    if keys[pygame.K_w]:
        if man2.canmove:
            man2.jump()
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_w:
            if man2.is_jumping:
                while(man2.velocity<0):
                     man2.velocity+=1
                man2.is_jumping=False

    if keys[pygame.K_u]:
        if man2.startX-180<=60:
           man2.startX+=2

    elif keys[pygame.K_t]:
        if man2.startX-180>=-60:

            man2.startX-=2


   
    # if not man22.isJumping:
    #     if keys[pygame.K_w]:
    #         man22.isJumping = True
    # else:
    #     if man22.speed >= -10:
    #         neg = 1
    #         if man22.speed < 0:
    #             neg = -1
    #         man22.y -= (man22.speed**2)*0.27*neg
    #         man22.speed -= 1

    #     else:
    #         man22.speed = 10
    #         man22.isJumping = False


  
  
  

   
  





    newFireball=pygame.time.get_ticks()
    if newFireball-cooldownFireball>=randrange(15000,50000):
        releaseFireBall()
        cooldownFireball=newFireball
    if time2-time3 >= timeup:
        healths.append(Potion(randrange(100,1430),randrange(100,450),choice([1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,4,11,11,11,11,11,12,12,12,12,12,13,13,13]),heart))
    #     if man2.health <= 29:
    #         man2.health += 1
    #     if man.health <= 29:
    #         man.health += 1
        timeup=choice([1000,6000,10000,15000,12000,10000,30000])

        time3 = time2
    # time2=0

    redrawGame()
 

# print(dir(pygame.time))
   
