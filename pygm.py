import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Gey Tema")

walkLeft = [pygame.image.load('Photo/1.png'),
pygame.image.load('Photo/2.png'),
pygame.image.load('Photo/3.png'),
pygame.image.load('Photo/4.png'),
pygame.image.load('Photo/5.png'),
pygame.image.load('Photo/6.png'),]

walkRight = [pygame.image.load('Photo/7.png'),
pygame.image.load('Photo/8.png'),
pygame.image.load('Photo/9.png'),
pygame.image.load('Photo/10.png'),
pygame.image.load('Photo/11.png'),
pygame.image.load('Photo/12.png'),]

bg = pygame.image.load('Photo/phon.png')

pleirStop = pygame.image.load('Photo/111.png')

clock = pygame.time.Clock()

x = 300
y = 430
widht = 57
height = 76
speed = 5

isJamp = False
jampCaunt = 10

left = False
right = False
animCount = 0


bullets = []
lastM = "right"



def drowWindow():
	global animCount
	win.blit(bg,(0,0))
	if animCount + 1 >=30:
		animCount = 0

	if left:
		win.blit(walkLeft[animCount//5], (x,y))
		animCount +=1
	elif right:
		win.blit(walkRight[animCount//5],(x,y))
		animCount+=1
	else :
		win.blit(pleirStop,(x,y))


	
	pygame.display.update()


run = True
while run:
		clock.tick(30)

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
						run = False


		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT] and x > 15:
				x-=speed
				left = True
				right = False
		elif keys[pygame.K_RIGHT] and x < 500 -widht - 10:
				x+=speed
				left = False
				right = True
		else:
			left = False
			right = False
			animCount = 0		
		if not(isJamp):
				
				if keys[pygame.K_SPACE]:
						isJamp = True
				elif keys[pygame.K_UP]:
						isJamp = True
		else: 
				if jampCaunt >=-10:
						if jampCaunt < 0:
							y = (jampCaunt**2)/2 + y
						else:
							y-=(jampCaunt **2)/2
						jampCaunt -=1
				else:
						isJamp = False
						jampCaunt = 10

				
		
		drowWindow()

pygame.quit()