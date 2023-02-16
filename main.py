import pygame
import math
pygame.init()

clock = pygame.time.Clock()
FPS = 60

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Parallax")

#define game variables
scroll = 0

ground_image = pygame.image.load("imgs/sky.jpg").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()
player_image = pygame.image.load("imgs/run1.png").convert_alpha()
player_rect = player_image.get_rect(midbottom = (80,400))
penguin_image = pygame.image.load("imgs/penguin.png").convert_alpha()
penguin_rect = penguin_image.get_rect(midbottom = (600,400))


screen.blit(ground_image,(0,0))

pygame.mixer.init
pygame.mixer.music.load('imgs/intro.mp3')
pygame.mixer.music.play()

bg_images = []
bg_image = pygame.image.load(f"imgs/sky.jpg").convert_alpha()
bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
  for x in range(5):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.2

def draw_ground():
  for x in range(15):
    screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))





class duck(pygame.sprite.Sprite):
  def __init__(self,width, pos_x,pos_y,color):
    super().__init__()
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    self.rect = self.image.get_rect()



class penguin(pygame.sprite.Sprite):
  def __init__(self,width, pos_x,pos_y,color):
    super().__init__()
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    self.rect = self.image.get_rect


class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"img/run1{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0

	def update(self):
		explosion_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()


explosion_group = pygame.sprite.Group()




#game loop
run = True
while run:

  clock.tick(FPS)

  #draw world
  draw_bg()
  draw_ground()
  screen.blit(player_image,player_rect)
  screen.blit(penguin_image,penguin_rect)
  

  #get keypresses
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT] and scroll > 0:
    scroll -= 3
  if key[pygame.K_RIGHT] and scroll < 3000:
    scroll += 3

  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()
  


pygame.quit()
