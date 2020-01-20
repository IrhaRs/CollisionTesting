import pygame
import math

class Poly:
	def __init__(self):
		#X and Y position:
		self.x=500
		self.y=400
		#Rotation
		self.rotation=0
		#Direction
		self.direction=(math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation)))
		print(self.direction)
		print(math.degrees(math.atan2(self.direction[0],self.direction[1])))
		#color of object
		self.color = (255,255,255)
		#points/corners (x,y)
		self.lst_relative_points=[]
		self.lst_points=[]

		#width(0=Fill, width >0 = line thickness)
		self.width = 1

		#gravity
		self.gravity = False


		#debug
		self.debug=False
		self.debug_AABB_color = (0,0,255)
		self.debug_AABB_padding=0
		self.debug_center_color = (255,0,0)
		self.debug_direction_color=(0,255,0)
		self.debug_direction_length = 1.5

	def update(self):
		pass

	def draw(self,display):
		if len(self.lst_points)>=3:
			pygame.draw.polygon(display,self.color,self.lst_points,self.width)
		if self.debug:
			points = self.getAABBShape(self.debug_AABB_padding)
			w= points[1][0]-points[0][1]
			h= points[1][1]-points[0][1]
			line = self.getAABBline(self.debug_AABB_padding)
			pygame.draw.line(display,self.debug_AABB_color,line[0],line[1],1)
			#pygame.draw.rect(display,self.debug_AABB_color,pygame.Rect(points[0][0],points[0][1],w,h),1)
			#pygame.draw.line(display,self.debug_direction_color,(self.x,self.y),((self.x+self.direction[0])*self.debug_direction_length,(self.y+self.direction[1])*self.debug_direction_length),1)
			pygame.draw.circle(display,self.debug_center_color,(self.x,self.y),1)

	def rotate(self,degrees):
		#calculate the direction and relative point vectors
		self.rotation +=degrees
		self.direction=(math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation)))
		self.calc_points()
	
	def calc_points(self):
		self.lst_points=[]
		for rp in self.lst_relative_points:
			#get the base point from rotation
			base_x,base_y = (math.cos(math.radians(self.rotation+rp[0])),math.sin(math.radians(self.rotation+rp[0])))
			#scalar and offset it around center
			point = [self.x+(base_x*rp[1]),self.y+(base_y*rp[1])]
			self.lst_points.append(point)



	def make_relative_point(self,x,y):
		distance = math.sqrt((x*x)+(y*y))
		r = math.degrees(math.atan2(x,y))+90

		print("degrees: "+str(r)+" scale: "+str(distance))
		self.lst_relative_points.append([r,distance])
		self.calc_points()

	def getAABBShape(self,padding):
		#get top left and right corner around 
		min_x=math.inf
		min_y=math.inf
		max_x=-math.inf
		max_y=-math.inf

		for p in self.lst_points:
			if p[0]>=max_x:
				max_x=p[0]
			if p[0]<=min_x:
				min_x=p[0]
			if p[1]>=max_y:
				max_y=p[1]
			if p[1]<=min_y:
				min_y=p[1]
		
		min_x-=padding
		min_y-=padding
		max_x+=padding
		max_y+=padding



		return [(min_x,min_y),(max_x-min_x,max_y-min_y)]


	def getAABBline(self,padding):
		#get top left and right corner around 
		min_x=math.inf
		min_y=math.inf
		max_x=-math.inf
		max_y=-math.inf

		for p in self.lst_points:
			if p[0]>=max_x:
				max_x=p[0]
			if p[0]<=min_x:
				min_x=p[0]
			if p[1]>=max_y:
				max_y=p[1]
			if p[1]<=min_y:
				min_y=p[1]
		
		min_x-=padding
		min_y-=padding
		max_x+=padding
		max_y+=padding

		

		return [(min_x,min_y),(max_x,max_y)]

