import pygame,sys#new libraries


from pygame.locals import QUIT
from random import randint




pygame.init()
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption('Rectangle maker')
myfont = pygame.font.SysFont('sans',50)
#mytext = myfont.render('Hello World',True,'white')
screen.blit(myfont.render('Hello World',True,'white'),(100,700))


class Rectangles():
    def __init__(self,color,dimensions):
        self.color = color
        self.dimensions = dimensions
    def create(self):
        pygame.draw.rect(screen,self.color,self.dimensions)
    def colorchange(self):
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        pygame.draw.rect(screen,self.color,self.dimensions)


circle = pygame.draw.circle(screen,'green',(700,500),50,3)
class Circles():
    def __init__(self,color,position,radius,thickness):
        self.color = color
        self.position = position
        self.radius = radius
        self.thickness = thickness
    def form(self):
        pygame.draw.circle(screen,self.color,self.position,self.radius, self.thickness)
    def grow(self):
        self.radius = self.radius+10
        pygame.draw.circle(screen,self.color,self.position,self.radius,self.thickness)
    def shrink(self):
        #if self.radius <10:
            #self.radius = 10
        self.radius = self.radius-10
        pygame.draw.circle(screen,self.color,self.position,self.radius,self.thickness)
        

    


long = Rectangles('orange',(100,100,100,500))
verybig = Rectangles('purple',(500,0,300,500))
testcirc = Circles('white',(500,600),50,5)

#long.create()
#verybig.create()








#While loop goes last
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            #long.colorchange()
            testcirc.shrink()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #verybig.colorchange()
            testcirc.grow()
            


    pygame.display.update()





