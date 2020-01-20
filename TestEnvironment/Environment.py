import pygame
from pygame.locals import *
import sys


class Environment:
	def __init__(self):
		pygame.init()
		#setup fps
		self.fps = 30
		self.fpsClock = pygame.time.Clock()

		#setup width/height
		self.width = 1280
		self.height = 720
		#make display
		self.display = pygame.display.set_mode((self.width,self.height))
		self.title = "Environment"
		pygame.display.set_caption(self.title)

		#objects
		self.lst_objects = []

		print("made Environment")

	def gameLoop(self):
		while True:
			self.display.fill((0, 0, 0))
			#keys=pygame.key.get_pressed()
	
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			# Update
			for obj in self.lst_objects:
				obj.update()
			# Draw.
			for obj in self.lst_objects:
				obj.draw(self.display)
			
			pygame.display.flip()
			self.fpsClock.tick(self.fps)

	def add_Object(self,obj):
		self.lst_objects.append(obj)

	def run(self):
		self.gameLoop()