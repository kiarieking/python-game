import pygame
pygame.init()

blue=(116,191,247)
display_width=800
display_height=600
gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("racing game")
clock=pygame.time.Clock()
carimg=pygame.image.load("ui.png")
backgroundpic=pygame.image.load("download12.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
strip=pygame.image.load("strip.jpg")

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

	bumped=False
	while not bumped:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				bumped=True


		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				x_change=-5
			if event.key==pygame.K_RIGHT:
				x_change=5

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				x_change=0			
		x+=x_change

		gamedisplays.fill(blue)
		background()
		car(x,y)
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()