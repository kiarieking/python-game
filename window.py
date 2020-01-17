import pygame
pygame.init()
import time
import random

blue=(119,118,110)
black=(0,0,0)
red=(255,0,0)
display_width=800
display_height=600
gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("racing game")
clock=pygame.time.Clock()
carimg=pygame.image.load("ui.png")
backgroundpic=pygame.image.load("download12.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
strip=pygame.image.load("strip.jpg")
car_width=53

def obstacle(obs_startx,obs_starty,obs):
	if obs==0:
		obs_pic=pygame.image.load("car.jpg")
	elif obs==1:
		 obs_pic=pygame.image.load("car1.jpg")
	elif obs==2:
		obs_pic=pygame.image.load("car2.jpg")
	elif obs==3:
		obs_pic=pygame.image.load("car4.jpg")
	elif obs==4:
		obs_pic=pygame.image.load("car5.jpg")
	elif obs==5:
		obs_pic=pygame.image.load("car6.jpg")
	elif obs==6:
		obs_pic=pygame.image.load("car7.jpg")

	gamedisplays.blit(obs_pic,(obs_startx,obs_starty))	

def score_system(score,passed):
	font=pygame.font.SysFont(None,25)
	text=font.render("Passed "+str(passed),True,black)
	score=font.render("Score"+str(score),True,red)
	gamedisplays.blit(text,(0,50))
	gamedisplays.blit(score,(0,20))

def text_objects(text,font):
	textsurface=font.render(text,True,black)
	return textsurface,textsurface.get_rect()

def message_display(text):
	largetext=pygame.font.Font("freesansbold.ttf",80)
	textsurf,textrect=text_objects(text,largetext)
	textrect.center=((display_width/2),(display_height/2))
	gamedisplays.blit(textsurf,textrect)
	pygame.display.update()
	time.sleep(3)
	game_loop()

def crash():
	message_display("GAME OVER")		

def background():
	gamedisplays.blit(backgroundpic,(0,0))
	gamedisplays.blit(backgroundpic,(0,200))
	gamedisplays.blit(backgroundpic,(0,400))
	gamedisplays.blit(backgroundpic,(700,0))
	gamedisplays.blit(backgroundpic,(700,200))
	gamedisplays.blit(backgroundpic,(700,400))
	gamedisplays.blit(yellow_strip,(400,0))
	gamedisplays.blit(yellow_strip,(400,100))
	gamedisplays.blit(yellow_strip,(400,200))
	gamedisplays.blit(yellow_strip,(400,300))
	gamedisplays.blit(yellow_strip,(400,400))
	gamedisplays.blit(yellow_strip,(400,500))
	gamedisplays.blit(strip,(160,0))
	gamedisplays.blit(strip,(160,100))
	gamedisplays.blit(strip,(160,200))
	gamedisplays.blit(strip,(640,0))
	gamedisplays.blit(strip,(640,100))
	gamedisplays.blit(strip,(640,200))

def car(x,y):
	gamedisplays.blit(carimg,(x,y))


def game_loop():
	x=(display_width*0.45)
	y=(display_height*0.8)
	x_change=0
	obstacle_speed=9
	obs=0
	y_change=0
	obs_startx=random.randrange(200,(display_width-200))
	obs_starty=-550
	obs_width=56
	obs_height=125
	passed=0
	level=0
	score=0

	bumped=False
	while not bumped:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				x_change=-5
			if event.key==pygame.K_RIGHT:
				x_change=5
			if event.key==pygame.K_a:
				obstacle_speed+=2
			if event.key==pygame.K_b:
				obstacle_speed-=2		
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				x_change=0			
		x+=x_change

		gamedisplays.fill(blue)
		background()
		obs_starty-=(obstacle_speed/4)
		obstacle(obs_startx,obs_starty,obs)
		obs_starty+=obstacle_speed
		car(x,y)
		score_system(passed,score)
		if x>640-car_width or x<160:
			crash()
		if x>display_width-(car_width+140) or x<140:
			crash()
		if obs_starty>display_height:
			obs_starty=0-obs_height
			obs_startx=random.randrange(140,(display_width-140))
			obs=random.randrange(0,7)
			passed=passed+1
			score=passed*10
			if int(passed)%10==0:
				level=level+1
				obstacle_speed+=2
				largetext=pygame.font.Font("freesansbold.ttf",80)
				textsurf,textrect=text_objects("Level "+str(level),largetext)
				textrect.center=((display_width/2),(display_height/2))
				gamedisplays.blit(textsurf,textrect)
				pygame.display.update()
				time.sleep(3)

		if y<obs_starty+obs_height:
			if x>obs_startx and x<obs_startx+obs_width or x+car_width>obs_startx and x+car_width<obs_startx+obs_width:
				crash()	

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit() 