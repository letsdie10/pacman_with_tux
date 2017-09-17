import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
	def __init__(self, ai_settings, screen):
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		
		self.image = pygame.image.load('images/wall.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		self.rect.x, self.rect.y = 0, 0
		
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#self.x = float(self.rect.x)
		#self.y = float(self.rect.y)
		
	def update(self):
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
		#self.rect.x = self.x
		#self.rect.y = self.y
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)