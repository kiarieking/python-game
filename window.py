import pygame
pygame.init()

blue=(116,191,247)
display_width=800
display_height=600
gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("racing game")
clock=pygame.time.Clock()

def game_loop():
	bumped=False
	while not bumped:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				bumped=True

		gamedisplays.fill(blue)
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()