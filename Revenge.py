import pygame,sys
from pygame.locals import *
import time
global CY
pygame.init()




global DC,CY,keys_pressed
CY=pygame

DC = ' '
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
GREEN = (0,255,0)
RED =   (255,0,0)
ORANGE = (255,45,0)
GRAY_BLACK = (10,10,10)
GRAY = (100,100,100)
LIGHT_BLUE = (25,185,255)
mouse_pos = pygame.mouse.get_pos()
class Window:
    def __init__(self,width,height,mode):
        global DC,clock
        self.w=width
        self.h=height
        self.DC = pygame.display.set_mode((self.w,self.h),mode)
        DC = self.DC
    def exit(self,num):
        if num == 1:
            rect(WHITE,0,0,self.w,20,0)
            text("{CY}",GRAY,15,1.5,1.5)
            exit=Button_exit(RED,self.w-20,self.h-self.h,20,20)
            exit.action()

class text():
    def __init__(self,name,color,n,x,y):
        global DC

        self.x=x
        self.y=y
        font = pygame.font.SysFont('console',n)
        self.tex=font.render(name,True,(color))
        DC.blit(self.tex,(self.x,self.y))


class rect():
    def __init__(self,color,x,y,w,h,f):
        global DC
        self.rect=pygame.Rect(x,y,w,h)
        pygame.draw.rect(DC,(color),(self.rect),f)

class circle():
    def __init__(self,color,x,y,r,f):
        global DC
        pygame.draw.circle(DC,color,(x,y),r,f)

class line():
    def __init__(self,color,x1,y1,x2,y2,f):
        global DC
        pygame.draw.line(DC,(color),(x1,y1),(x2,y2),f)

class arc():
    def __init__(self,color,x1,y1,x2,y2,v1,v2,v3):
        global DC
        pygame.draw.arc(DC,color,(x1,y1,x2,y2),v1,v2,v3)

class ellipse():
    def __init__(self,color,w,h,x,y,f):
        global DC
        pygame.draw.ellipse(DC,((color)),(w,h,x,y),f)

class polygon():
    def __init__(self,color,x1,y1,x2,y2,x3,y3,f):
        global DC
        self.pointlist_1 = [(x1, y1), (x2, y2), (x3, y3)]
        pygame.draw.polygon(DC,color, self.pointlist_1,f)

class Cursor:
    def __init__(self,color,f):
        pygame.mouse.set_visible(0)
        self.x,self.y=pygame.mouse.get_pos()
        self.color=color
        polygon(self.color,self.x,self.y,self.x,self.y+10,self.x+8,self.y+8,f)



class image():
    def __init__(self,namefile,s1,s2):
        self.image=''
        self.image=pygame.image.load(namefile)
        self.image_s=pygame.transform.scale(self.image,(s1,s2))

    def imageDraw(self,x,y):
        global DC
        DC.blit(self.image_s,(x,y))

class sound():
    def __init__(self,nameFile):
        self.sond=pygame.mixer.Sound(nameFile)
    def play(self):
        self.sond.play()

class music():
    def __init__(self,nameFile,r):
        self.soud=pygame.mixer.music.load(nameFile)
        self.soud=pygame.mixer.music.play(r)

class background():
    def __init__(self,color):
        global DC
        DC.fill((color))



class image_rotate():
    def __init__(self,namefile,vel,x,y,s1,s2):
       
        self.image=pygame.transform.scale(pygame.image.load(namefile).convert_alpha(),(s1,s2))
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.vel=vel
        self.angle=0
    def rotar(self):
        global DC
        if self.vel>0 or self.vel<0:
            self.angle+=self.vel
        self.angle=self.angle%360

        tmp=pygame.transform.rotate(self.image,self.angle)
        rect=tmp.get_rect()
        rect.center=self.rect.center
        DC.blit(tmp,rect)


class move():
    def __init__(self,posx,posy,speed,mouse_pos):

        self.mouse_pos=mouse_pos
        self.x=posx
        self.y=posy
        self.vel=speed
        run = (self.mouse_pos[0] - self.x) * self.vel
        rise = (self.mouse_pos[1] - self.y) * self.vel
        self.x += run
        self.y += rise

class Button_exit:
    def __init__(self,color1,w,h,x,y):
        global DC
        self.color1=color1
        self.color2=BLACK
        self.w=w
        self.h=h
        self.x=x
        self.y=y
        self.f=0
        self.text='X'
        self.n=15
        self.act=False
        self.mas=()

    def action(self):

        self.mouse=pygame.mouse.get_pos()
        self.click=pygame.mouse.get_pressed()
        self.cubo=pygame.draw.rect(DC,(self.color1),(self.w,self.h,self.x,self.y),self.f)
        text(self.text,(WHITE),self.n,self.w+5,self.h)

        if self.cubo.collidepoint(self.mouse):
            self.cubo=pygame.draw.rect(DC,(self.color2),(self.w,self.h,self.x,self.y),self.f)
            text(self.text,(RED),self.n,self.w+5,self.h)
            if self.click[0] == 1:
                self.act=True

        if self.act==True:
            sys.exit()
        self.act=False


        
class Button:
    def __init__(self,text,color1,color2,w,h):
        global DC
        self.color1=color1
        self.color2=color2
        self.w=w
        self.h=h
        self.x=80
        self.y=20
        self.f=0
        self.text=text
        self.n=15
        self.act=False
        self.mas=()

    def action(self,fun):

        self.mouse=pygame.mouse.get_pos()
        self.click=pygame.mouse.get_pressed()
        self.cubo=pygame.draw.rect(DC,(self.color1),(self.w,self.h,self.x,self.y),self.f)
        text(self.text,(self.color2),self.n,self.w+20,self.h)

        if self.cubo.collidepoint(self.mouse):
            self.cubo=pygame.draw.rect(DC,(self.color2),(self.w,self.h,self.x,self.y),self.f)
            text(self.text,(self.color1),self.n,self.w+20,self.h)
            if self.click[0] == 1:
                self.act=True

        if self.act==True:
            fun()
        self.act=False

class Collider_mouse:
    def __init__(self,pos,mouse_pos,fun):
        self.mouse = mouse_pos
        self.fun=fun
        self.actv=False
        self.x,self.y,self.w,self.h=pos
        if self.mouse[0] > self.x and self.mouse[0] < self.x + self.w:
            if self.mouse[1] > self.y and self.mouse[1] < self.y + self.h:
                self.actv=True
                if self.actv==True:
                    self.fun()
        else:
            self.actv=True

class Collider_obj:
    def __init__(self,object1, object2,fun):
        self.fun = fun
        self.actv=False
        self.object1=object1
        self.object2=object2
        if self.object1[0] < self.object2[0] + self.object2[2] and self.object1[0] + self.object1[2] > self.object2[0] and \
                self.object1[1] < self.object2[1] + self.object2[3] and self.object1[1] + self.object1[3] > self.object2[1]:
            self.actv=True
            if self.actv==True:
                self.fun()
        else:
            self.actv=False
global event
event=''
class line_text:
    def __init__(self,font,color,x,y,color_box,width,cursor):
        self.color=color
        self.x = x
        self.y = y
        self.width = width
        self.height = 15
        self.activ = False
        self.textbox = ''
        self.color_box = (200,200,200)
        self.color2 = color_box
        self.base_font = pygame.font.Font(None,font)
        self.barra_x=self.x
        self.barra_y=self.y
        self.barra_activ = True
        self.color_b = cursor
        self.car = 0
        self.num = 0
       
    def display(self):

        global DC,event
        self.key = self.textbox
        self.input_rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.barra = pygame.Rect(self.barra_x,self.barra_y + 4,4,8)
        self.long_text = len(self.textbox)
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.keys= pygame.key.get_pressed()
        if self.width == 300:
            self.num = self.width/7.5

        elif self.width == 350:
            self.num = self.width/7

        if self.input_rect.collidepoint(self.mouse):
            if self.click[0] == 1:
                self.activ =True
                self.color_box = (GRAY)
            pygame.draw.rect(DC,self.color_box,self.input_rect,0)
            
           
        
        else:
            if self.click[0] == 1:
                self.activ = False
                self.color_box = self.color2
        if self.activ == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    time.sleep(0.1)
                    self.textbox = self.textbox[0:-1]
       
                else:
                    if self.long_text < self.num:
                        time.sleep(0.1)
                        self.textbox += event.unicode
                    


            else:
                self.textbox = self.textbox


        
        text_surface = self.base_font.render(self.textbox,True,self.color)
        DC.blit(text_surface,(self.input_rect.x+5,self.input_rect.y+3))
        self.barra.x = text_surface.get_width()+self.barra_x+5
       


        if self.activ == True:
            pygame.draw.rect(DC,self.color_b,self.barra,0)


class text_box:
    def __init__(self,color_text,x,y,color_box,width,color_barra,max_line):
        from Revenge import line_text
        self.max_line=max_line
        self.w=width
        self.sum=0
        self.font=15
        self.color=color_text
        self.x=x
        self.y=y
        self.color_box=color_box
        self.cursor=color_barra
        self.add_rect = 1
        self.add_actv = False
        self.list_box=[]
        for i in range(self.max_line):
            self.l1=line_text(self.font,self.color,self.x,self.y+self.sum,self.color_box,self.w,self.cursor)
            self.list_box.append(self.l1)
            self.sum = self.sum + 20
       
        
    def draw_box(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        for l1 in self.list_box:
            l1.display()
        for l1 in self.list_box:
            if l1.input_rect.collidepoint(self.mouse):
                if l1.activ==True:
                    if self.click[2]:
                        self.sum = self.sum - 20
                        self.list_box.remove(l1)
        
                else:          
                    if self.click[2]:
                        time.sleep(0.1)
                        print(len(self.list_box))
                        self.add_actv=True
        if self.add_actv==True:
            for i in range(self.add_rect):
                self.l1=line_text(self.font,self.color,self.x,self.y+self.sum,self.color_box,self.w,self.cursor)
                self.list_box.append(self.l1)
                self.sum = self.sum + 20
                self.add_actv=False            
                     
class Entry:
    def __init__(self,font,color,x,y,color_box,width,cursor):
        self.color=color
        self.x = x
        self.y = y
        self.width = width
        self.height = 20
        self.long=9
        self.num = width/self.long
        self.activ = False
        self.textbox = ''
        self.color_box = color_box
        self.color2 = color_box
        self.base_font = pygame.font.Font(None,font)
        self.barra_x=self.x
        self.barra_y=self.y
        self.barra_activ = True
        self.color_b = cursor
        self.car = 0
        self.time=0.1
    def display(self):
        global DC,event
        self.key = self.textbox
        self.input_rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.barra = pygame.Rect(self.barra_x,self.barra_y + 4,1,12)
        self.long_text = len(self.textbox)
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.keys= pygame.key.get_pressed()
        if self.input_rect.collidepoint(self.mouse):
            if self.click[0] == 1:
                self.activ =True
                self.color_box = (GRAY)
        else:
            if self.click[0] == 1:
                self.activ = False
                self.color_box = self.color2
        if self.activ == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    time.sleep(self.time)
                    self.textbox = self.textbox[0:-1]

                else:
                    if self.long_text < self.num:
                        time.sleep(self.time)
                        self.textbox += event.unicode
            else:
                self.textbox = self.textbox
        text_surface = self.base_font.render(self.textbox,True,self.color)
        DC.blit(text_surface,(self.input_rect.x+5,self.input_rect.y+3))
        self.barra.x = text_surface.get_width()+self.barra_x+5
        pygame.draw.rect(DC,self.color_box,self.input_rect,1)


        if self.activ == True:
            pygame.draw.rect(DC,self.color_b,self.barra,0)

class load:
    def __init__(self,x,y,w,h,color_1,color_2,load):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.color_1=color_1
        self.color_2=color_2
        self.Activ=False
        self.load=load
    def display(self):

        rect(self.color_1,self.x,self.y,self.load,self.h,0)
        rect(self.color_2,self.x,self.y,self.w,self.h,0)
        if self.w<self.load:
            self.w += 2
        else:
            self.Activ=True

class mouse:
    def __init__(self):
        self.pos = pygame.mouse.get_pos()

class loading:
    def __init__(self):
        global event
        global user_text
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            event=event
        
def update(time):
    clock = pygame.time.Clock()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(time)

def mainloop():
    pygame.quit()


# FALTA TERMINAR!!!!!:

# Un dia loco usando todo lo que se para mejorar este modulo 13/07/2020.
# creo que pronto lograre mi objetivo. 25/09/2020.
