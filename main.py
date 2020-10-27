#some special imports
import pygame
import random
import time
from win32com.client import Dispatch
#screen display
screen_width = 1280
screen_height = 960

pygame.init()

#defining fps1
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))
#defining colors
white = (200,200,200)
red = (255,0,0)
blue = (0,0,255)
#text display
player_score = 0
opponent_score = 0
game_font = pygame.font.SysFont("comicsansms",64)
game_font1 = pygame.font.SysFont("comicsansms",32)
pause_font = pygame.font.SysFont("comicsansms",32)
#ball
ball_speed_x = 7*random.choice((1,-1))
ball_speed_y = 7*random.choice((1,-1))
player_speed = 0
opponent_speed = 25
#objects shape and positions

def speak(str):
    speak = Dispatch(("SAPI.spVoice"))
    speak.Speak(str)

def paused():
    pause = True
    while pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
                elif event.key == pygame.K_RETURN:
                    pygame.quit()

                    quit()


        pygame.display.update()
        clock.tick(5)

pygame.display.set_caption("Ping Pong")
ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2-70,10,140)
opponent = pygame.Rect(10,screen_height/2-70,10,140)
#making the ball restart
def ball_restart():
    global ball_speed_x,ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y*= random.choice((1,-1))
    ball_speed_x*= random.choice((1,-1))

#player movement
def playeranimation():
    player.y += player_speed
    if player.top<=0:
        player.top = 0
    if player.bottom>=screen_height:
        player.bottom = screen_height
#OPPPONENT AI
def opponent_ai():
    if opponent.top< ball.y:
        opponent.top+= opponent_speed

    if opponent.bottom>ball.y:
        opponent.bottom-= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
#ball movement
def animation():
    global ball_speed_x,ball_speed_y,player_score , opponent_score
    ball.x += ball_speed_x*4
    ball.y += ball_speed_y*4
    #boundries
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y*=-1
    if ball.left<=0 :
        player_score += 1
        ball_restart()
    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()
    #collide
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x*=-1

#game loop
exitgame = True
while exitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed-=50
            elif event.key == pygame.K_DOWN:
                player_speed+=50
            if event.key == pygame.K_SPACE:
                paused()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 50
            elif event.key == pygame.K_DOWN:
                player_speed -= 50

#calling functions
    animation()

    playeranimation()
    opponent_ai()

#drawing objects
    screen.fill((42, 45, 51))

    pygame.draw.rect(screen,(0, 255, 255),player)
    pygame.draw.rect(screen,(255, 102, 102),opponent)
    pygame.draw.ellipse(screen,(204, 255, 229),ball)
    pygame.draw.aaline(screen,white, (screen_width/2,0), (screen_width/2,screen_height))

    #showing the text
    player_text = game_font.render(f"{player_score}", False,(0,255,255))
    #drawing
    screen.blit(player_text,(660,470))
    #showing the text
    opponent_text = game_font.render(f"{opponent_score}", False,(255,102,102))
    #drawing
    screen.blit(opponent_text,(600,470))

    pause_button = pause_font.render("Press space to pause to resume Press it again",False,(255,255,204))
    screen.blit(pause_button,(300,20))
    text_color = (0, 153, 153)
    you_won =  game_font1.render("YOU WON FIRST ROUND NEXT ROUND", False,text_color)
    computer_wins = game_font1.render("COMPUTER WINS 1 ROUND NEXT ROUND", False,text_color)
    you_won1 = game_font1.render("YOU WON SECOND ROUND NEXT ROUND", False, text_color)
    computer_wins1 = game_font1.render("COMPUTER WINS 2 ROUND NEXT ROUND", False, text_color)
    if player_score == 5:


        screen.blit(you_won, (300,60))



    elif opponent_score == 5:
        screen.blit(computer_wins, (300,60))

    if player_score == 10:

        screen.blit(you_won1, (300,60))

        break


    elif opponent_score == 10:
        screen.blit(computer_wins1, (300,40))
        break


    clock.tick(30)
    pygame.display.flip()
