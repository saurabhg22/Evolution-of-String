import random
import pygame
import time
strings = []
population = 20
mainstring = raw_input("Enter the word, phrase or sentence you want to generate: ")
mutuation = .5
pygame.init()
light_green = (191,248,22)
yellow=(255,245,62)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green = (0,155,0)
blue=(0,0,255)
stringlength = len(mainstring)
display_width=1000
display_height=600
gd=pygame.display.set_mode((display_width,display_height))
for i in range(population):
    string = ""
    for j in range(stringlength):
        string+=random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()_+{}|:\"<>?,\./;'[]-=")
    strings.append(string)
def cost(string):
    c = 0
    for i in range(len(string)):
        c+=abs(ord(mainstring[i])-ord(string[i]))
    return c
def sort():
    for j in range(population):
        maxcost = 0
        for i in range(population - j):
            if maxcost<cost(strings[i]):
                maxcost=cost(strings[i])
                k = i
        strings[population - j-1],strings[k] = strings[k],strings[population - j-1]
def msgtoscrn(msg,color,y_displace=0,size=25,x_displace=0):
    font = pygame.font.SysFont("monospace",size)
    screen_text = font.render(msg,True,color)
    textrect = screen_text.get_rect()
    textrect.center = (display_width/2) + x_displace,(display_height/2) + y_displace
    gd.blit(screen_text,textrect)     
def mutuate():
    for i in range(population):
        if random.uniform(0.0,1.0)<mutuation:
            r = random.randint(0,len(mainstring)-1)
            l = list(strings[i])
            c = random.randint(0,1)
            if c==0:
                l[r] = chr(ord(l[r])+1)
            else:
                l[r] = chr(ord(l[r])-1)
            strings[i] = "".join(l)
def upgrade():
    mutuate()
    sort()
    for i in range(population/4):
        strings[population/2+2*i] = strings[2*i][:stringlength/2]+strings[2*i+1][stringlength/2:]
        strings[population/2+2*i+1] = strings[2*i][stringlength/2:]+strings[2*i+1][:stringlength/2]
def main():
    i = 1
    mcost = cost(strings[0])
    gd.fill(white)
    msgtoscrn("Press any Key to Start!!!...",black,0,30)
    pygame.display.update()
    condition = True
    while condition:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                condition = False
                break
    while strings[0]!=mainstring:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gd.fill(white)
        msgtoscrn("Generation: "+str(i)+"        Cost: "+str(cost(strings[0])),blue,-270,20,-250)
        msgtoscrn(strings[0],((255*cost(strings[0]))/mcost,155-(155*cost(strings[0]))/mcost,0),-50,30)
        i+=1
        upgrade()
        pygame.display.update()
    gd.fill(white)
    msgtoscrn(strings[0],green,-50,30)
    msgtoscrn("Generation: "+str(i)+"        Cost: "+str(cost(strings[0])),blue,-270,20,-250)
    msgtoscrn("Press any Key!!!...",black,0,20)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                pygame.quit()
                quit()
main()
