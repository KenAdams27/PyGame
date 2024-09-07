import asyncio
import pygame
from pygame import mixer
from sys import exit
from random import randint

pygame.init()

#creating the score
def display_score(start_time):
        global score,game_lost
        if game_lost is True:return 0
        else:
          current_time=pygame.time.get_ticks()-start_time
          score=int(current_time//58.45)
          score_surface = test_font.render(f'Score :  {score}',False,'#945AA4')
          score_rect = score_surface.get_rect(center =(700,100))
          screen.blit(score_surface,score_rect)
          return score

#obstacle movement function-
def obstacle_movement(obstacle_list):    
     if obstacle_list:
          for obstacle_rect in obstacle_list:
               obstacle_rect.x -=5
               if obstacle_rect.bottom==540:screen.blit(enemy_one_surface,obstacle_rect)
               else:screen.blit(enemy_two_surface,obstacle_rect)                 
          obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x>-100]
          return obstacle_list
     else : return []

#animating the walk for the player
def player_animation():
     global player_surface,player_index
     player_index +=0.1
     if player_index>=len(player_walk):player_index=0
     player_surface=player_walk[int(player_index)]

def winning():
     global winning_animation_surface,winning_animation_index
     winning_animation_index +=0.14
     if winning_animation_index>=len(winning_animation_frames):winning_animation_index=0
     winning_animation_surface=winning_animation_frames[int(winning_animation_index)]

def powerupanimation():
     global power_up_surface,power_up_index
     power_up_index +=1.4
     if power_up_index>=len(power_up_frames):power_up_index=0
     power_up_surface=power_up_frames[int(power_up_index)]


# all important variables
game_lost=False
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Run Code Run')
clock=pygame.time.Clock()
test_font=pygame.font.Font('Python projects/Game_test/Fonts/Font3.ttf',40)
large_font=pygame.font.Font('Python projects/Game_test/Fonts/Font3.ttf',100)
fire_font=pygame.font.Font('Python projects/Game_test/Fonts/Font4.otf',50)
game_active=True
obstacle_rect_list=[]
player_gravity=0
obstacle_timer =  pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1200)

#loading the audio file
mixer.music.load('Python projects/Game_test/Music/music.mp3')
mixer.music.play(-1)

#powerup
power_up=False

#all surface and rectangles required :
#creating the surfaces for our display
sky_surface = pygame.image.load('Python projects/Game_test/Graphics/Sky1.png').convert_alpha()
ground_surface=pygame.image.load('Python projects/Game_test/Graphics/ground2.jpg').convert_alpha()

#adding enemy_one to the game
#adding animations
enemy_one_frame1 = pygame.image.load('Python projects/Game_test/Graphics/Enemies/enemy_1.png').convert_alpha()
enemy_one_frame2 = pygame.image.load('Python projects/Game_test/Graphics/Enemies/enemy_1_walk.png').convert_alpha()
enemy_one_frames = [enemy_one_frame1,enemy_one_frame2]
enemy_one_index = 0
enemy_one_surface =enemy_one_frames[enemy_one_index]
enemy_one_rect=enemy_one_surface.get_rect(bottomright=(600,540))

#adding enemy_two to the game
#adding animations
enemy_two_frame1 = pygame.image.load('Python projects/Game_test/Graphics/Enemies/enemy_2.png').convert_alpha()
enemy_two_frame2 = pygame.image.load('Python projects/Game_test/Graphics/Enemies/enemy_2_fly.png').convert_alpha()
enemy_two_frames = [enemy_two_frame1,enemy_two_frame2]
enemy_two_index = 0
enemy_two_surface = enemy_two_frames[enemy_two_index]

#adding our player_character to the game
player_walk1= pygame.image.load('Python projects/Game_test/Graphics/Players/Player_walk1.png').convert_alpha()
player_walk2= pygame.image.load('Python projects/Game_test/Graphics/Players/Player_walk2.png').convert_alpha()
player_walk=[player_walk1,player_walk2]
player_index=0
player_surface = player_walk[player_index]
player_rect=player_surface.get_rect(topleft = (40,500))

#power_up_walk
power_up_walk_1=pygame.image.load('Python projects/Game_test/Graphics/Players/pu.png').convert_alpha()

#gameover screen character
player_lost=pygame.image.load('Python projects/Game_test/Graphics/Players/Player_lost.png').convert_alpha()
player_lost_rect=player_lost.get_rect(center = (400,250))

#restart game text 
restart_text = test_font.render('Click or Press space to restart.',False,'White')
restart_text_rect = restart_text.get_rect(center = (410,500))

#play_again
pl_text = test_font.render('Click or Press space to play again.',False,'Black')
pl_text_rect = pl_text.get_rect(center = (397,550))

#animation for winning the game
frame_1 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_1.png').convert_alpha()
frame_2 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_2.png').convert_alpha()
frame_3 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_3.png').convert_alpha()
frame_4 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_4.png').convert_alpha()
frame_5 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_5.png').convert_alpha()
frame_6 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_6.png').convert_alpha()
frame_7 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_7.png').convert_alpha()
frame_8 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_8.png').convert_alpha()
frame_9 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_9.png').convert_alpha()
frame_10 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_10.png').convert_alpha()
frame_11 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_11.png').convert_alpha()
frame_12 = pygame.image.load('Python projects/Game_test/Graphics/Win/Winning_Animation/frame_12.png').convert_alpha()
winning_animation_frames=[frame_1,frame_2,frame_3,frame_4,frame_5,frame_6,frame_7,frame_8,frame_9,frame_10,frame_11,frame_12]
winning_animation_index=0
winning_animation_surface=winning_animation_frames[winning_animation_index]
winning_animation_rect=winning_animation_surface.get_rect(center = (380,250))

#powerup frames
f1=pygame.image.load('Python projects/Game_test/Resources/powerup/1.gif').convert_alpha()
f2=pygame.image.load('Python projects/Game_test/Resources/powerup/2.gif').convert_alpha()
f3=pygame.image.load('Python projects/Game_test/Resources/powerup/3.gif').convert_alpha()
f4=pygame.image.load('Python projects/Game_test/Resources/powerup/4.gif').convert_alpha()
f5=pygame.image.load('Python projects/Game_test/Resources/powerup/5.gif').convert_alpha()
f6=pygame.image.load('Python projects/Game_test/Resources/powerup/6.gif').convert_alpha()
f7=pygame.image.load('Python projects/Game_test/Resources/powerup/7.gif').convert_alpha()
f8=pygame.image.load('Python projects/Game_test/Resources/powerup/8.gif').convert_alpha()
f9=pygame.image.load('Python projects/Game_test/Resources/powerup/9.gif').convert_alpha()
f10=pygame.image.load('Python projects/Game_test/Resources/powerup/10.gif').convert_alpha()
f11=pygame.image.load('Python projects/Game_test/Resources/powerup/11.gif').convert_alpha()
f12=pygame.image.load('Python projects/Game_test/Resources/powerup/12.gif').convert_alpha()
f13=pygame.image.load('Python projects/Game_test/Resources/powerup/13.gif').convert_alpha()
f14=pygame.image.load('Python projects/Game_test/Resources/powerup/14.gif').convert_alpha()
f15=pygame.image.load('Python projects/Game_test/Resources/powerup/15.gif').convert_alpha()
f16=pygame.image.load('Python projects/Game_test/Resources/powerup/16.gif').convert_alpha()
f17=pygame.image.load('Python projects/Game_test/Resources/powerup/17.gif').convert_alpha()
f18=pygame.image.load('Python projects/Game_test/Resources/powerup/18.gif').convert_alpha()
f19=pygame.image.load('Python projects/Game_test/Resources/powerup/19.gif').convert_alpha()
f20=pygame.image.load('Python projects/Game_test/Resources/powerup/20.gif').convert_alpha()
f21=pygame.image.load('Python projects/Game_test/Resources/powerup/21.gif').convert_alpha()
f22=pygame.image.load('Python projects/Game_test/Resources/powerup/22.gif').convert_alpha()
f23=pygame.image.load('Python projects/Game_test/Resources/powerup/23.gif').convert_alpha()
f24=pygame.image.load('Python projects/Game_test/Resources/powerup/24.gif').convert_alpha()
power_up_frames=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24]
power_up_index=0
power_up_surface=power_up_frames[power_up_index]
power_up_rect=power_up_surface.get_rect(center=(145,450))


#text for winning the game
winning_text = test_font.render('You won !!',False,'Black')
winning_text_rect =winning_text.get_rect(center = (380,500))

#animation timers for enemies
enemy_two_animationtimer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_two_animationtimer,200)

enemy_one_animationtimer =  pygame.USEREVENT + 3
pygame.time.set_timer(enemy_one_animationtimer,200)

#menu screen variables
loading_screen_image=pygame.image.load('Python projects/Game_test/Resources/loading_screen.png').convert_alpha()
loading_screen_image_rect=loading_screen_image.get_rect(center=(180,300))

gamename=large_font.render("Code Runner",False,"White")
gamename_rect=gamename.get_rect(center=(550,200))

menu_text=test_font.render("Click or press space to make",False,"white")
menu_text_rect=menu_text.get_rect(center=(550,400))

menu_textt=test_font.render("our code run.",False,'white')
menu_textt_rect=menu_textt.get_rect(center=(550,440))

hero_name=test_font.render("Code >_<",False,'white')
hero_name_rect=hero_name.get_rect(center=(170,500))

#loading screen
def loadingscreen():
     mixer.music.pause()
     while True:
          screen.fill('#3E2F7F')    
          screen.blit(loading_screen_image,loading_screen_image_rect)
          screen.blit(gamename,gamename_rect)
          screen.blit(menu_text,menu_text_rect)
          screen.blit(menu_textt,menu_textt_rect)
          screen.blit(hero_name,hero_name_rect)
          pygame.display.update()
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                    menutime=pygame.time.get_ticks()
                    mixer.music.unpause()
                    asyncio.run(main(menutime))
               if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    menutime=pygame.time.get_ticks()
                    mixer.music.unpause()
                    asyncio.run(main(menutime))
               
#the main game loop
async def main(menutime):
   global game_active,clock,player_gravity,obstacle_rect_list,enemy_one_animationtimer,enemy_two_animationtimer,enemy_one_surface,enemy_two_surface
   global test_font,enemy_one_index,enemy_two_index,game_lost,power_up
   start_time=menutime
   while True:
   #event loop to check if the player quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #eventl loop to check the user input
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom==630 and game_active is True:
                player_gravity =-20
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and player_rect.bottom==630 and game_active is True:
                player_gravity =-20
        if event.type== pygame.MOUSEBUTTONDOWN and event.button==3 and 200<=score<=300:
             power_up = True
           
        else:
             if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE and game_active is False:
                  game_active = True
                  game_lost=False
                  mixer.music.load('Python projects/Game_test/Music/music.mp3')
                  mixer.music.play(-1)
                  enemy_one_rect.left=800
                  start_time=pygame.time.get_ticks()
             if event.type==pygame.MOUSEBUTTONDOWN and game_active is False:
                  game_active = True
                  game_lost=False
                  mixer.music.load('Python projects/Game_test/Music/music.mp3')
                  mixer.music.play(-1)
                  enemy_one_rect.left=800
                  start_time=pygame.time.get_ticks()
        if game_active is True:
          if event.type == obstacle_timer :
               if randint(0,1):
                    obstacle_rect_list.append(enemy_two_surface.get_rect(bottomright=(randint(900,1100),440)))      
               else:
                    obstacle_rect_list.append(enemy_one_surface.get_rect(bottomright=(randint(900,1100),540)))
          if event.type == enemy_two_animationtimer:
               if enemy_two_index == 0 : enemy_two_index = 1
               else : enemy_two_index = 0
               enemy_two_surface = enemy_two_frames[enemy_two_index]
          if event.type ==  enemy_one_animationtimer:
               if enemy_one_index == 0 : enemy_one_index =  1
               else : enemy_one_index = 0
               enemy_one_surface =  enemy_one_frames[enemy_one_index]
    #menuscreen
    
     
    #stopping the game if player wins           
    s=display_score(start_time)
    if s > 999:
          game_active = False  
          s=0 
    if 200<=s<=300:player_walk[0]=power_up_walk_1
    if s>300 or power_up is True: player_walk[0]=player_walk1 
     #stopping power up after a certain time
    if s>=500:power_up=False  

    if game_active is True:
        #adding the layers of our display 
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,400))
        display_score(start_time)
        #player
        player_gravity+=1
        player_rect.y+=player_gravity
        #creating a floor to prevent the player from falling off of the screen
        player_animation()
        if player_rect.bottom>=630:player_rect.bottom = 630
        screen.blit(player_surface,player_rect)
        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #powerup
        if power_up is True:
                  powerupanimation()
                  screen.blit(power_up_surface,power_up_rect)
                  if obstacle_rect_list:
                       for obstacle in obstacle_rect_list:
                            if obstacle.collidepoint(200,500) or obstacle.collidepoint(200,400):obstacle.x=90000
                   
        #collisions
        if obstacle_rect_list:
             for obstacle in obstacle_rect_list:
                  if obstacle.collidepoint(player_rect.centerx,player_rect.centery):
                       power_up=False
                       game_active=False
                       obstacle_rect_list=[]

    #game over screen
    else:
       
         score_text=test_font.render(f'Game Over :(','False','White')
         score_text_rect = score_text.get_rect(center = (400,550))
         if score <=999:#game losing conditon
          mixer.music.unload()
          game_lost=True
          power_up=False
          screen.fill('#3E2F7F')
          screen.blit(player_lost,player_lost_rect)
          screen.blit(restart_text,restart_text_rect)
          screen.blit(score_text,score_text_rect)

         else:#game winning condition
              screen.fill('white')
              winning()
              screen.blit(winning_animation_surface,winning_animation_rect)
              screen.blit(winning_text,winning_text_rect)
              screen.blit(pl_text,pl_text_rect)

    #updating the display
    pygame.display.update()
    clock.tick(60)
    await asyncio.sleep(0)

loadingscreen()
    