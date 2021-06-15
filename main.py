import pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))
from random import randint
from time import sleep
a = 20
b = 20
R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)
rimbalzi = 0
tentativi = 1
xrossa = randint(32, 268)
yrossa = randint(32, 268)
pygame.draw.circle(screen, (0, 255, 0), (20, 20), 20)
pygame.draw.circle(screen, (255, 0, 0), (xrossa, yrossa), 32)
pygame.display.flip()
print("1️⃣ Primo Livello")
vx = int(input("Inserisci la velocità x: "))
vy = int(input("Inserisci la velocità y: "))
def pallaverde(x, y):
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (R, G, B), (x, y), 20)
    pygame.draw.circle(screen, (255, 0, 0), (xrossa, yrossa), 32)
    pygame.display.flip()
while a < 300 and b < 300:
    pallaverde(a, b)
    sleep(0.03)
    if a>280 or a<20:
        vx = -vx
        rimbalzi += 1
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)
    if b>280 or b<20:
        vy = -vy
        rimbalzi += 1
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)
    a = a + vx
    b += vy
    if rimbalzi>10:
      print("Non funziona! Inserisci dei nuovi valori.")
      vx = int(input("Inserisci la velocità x: "))
      vy = int(input("Inserisci la velocità y: "))
      tentativi+=1
      rimbalzi=0
    if abs(xrossa - a) <= 32 and abs(yrossa - b) <= 32:
        pygame.draw.circle(screen, (0, 255, 0), (xrossa, yrossa), 32)
        str(rimbalzi)
        str(tentativi)
        print("Hai vinto con", rimbalzi,"rimbalzi! Ce l'hai fatta al ",tentativi,"° tentativo.")
        sleep(1)
        break
screen.fill((255, 255, 255))
print("2️⃣ Secondo livello")
xrossa = randint(32, 268)
yrossa = randint(32, 268)
pygame.draw.circle(screen, (R, G, B), (20, 20), 20)
pygame.draw.circle(screen, (255, 0, 0), (xrossa, yrossa), 32)
pygame.display.flip()
vrossa = 2
x=20
y=20
rimbalzi=0
vx = int(input("Inserisci la velocità x: "))
vy = int(input("Inserisci la velocità y: "))
def palle(x,y,xrossa,yrossa):
  screen.fill((255,255,255))
  pygame.draw.circle(screen, (255,0,0), (xrossa,yrossa), 32)
  pygame.draw.circle(screen,(R,G,B),(x,y),20)
  pygame.display.flip()
while yrossa+32<=300 and x<300 and y<300:
  palle(x,y,xrossa,yrossa)
  xrossa=xrossa
  if yrossa>=268  or yrossa<=32:
    vrossa=-vrossa
  yrossa+=vrossa
  sleep(0.03)
  if x > 280 or x < 20:
    vx = -vx
    rimbalzi += 1
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
  if y>280 or y<20:
    vy = -vy
    rimbalzi += 1
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
  x= x + vx
  y += vy
  if abs(xrossa-x)<32 and abs(yrossa-y)<32:
    str(rimbalzi)
    print("Hai vinto con", rimbalzi,"rimbalzi!")
    break