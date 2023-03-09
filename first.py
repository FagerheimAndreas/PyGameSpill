import pygame

# setter opp pygame
pygame.init()

# lager vindu
screen = pygame.display.set_mode((800,600))
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background,(800,600))

#bullet = pygame.transform.scale(bullet,(50,28))
# set tittel og ikon
pygame.display.set_caption("Space invasion")

#spiller
playerImage = pygame.image.load("skip.png")
playerX = 400
playerY = 500
moveX = 0
moveY = 0
# fiende
enemyImage = pygame.image.load("skip.png")
enemyImage = pygame.transform.rotate(enemyImage,180)
enemyX = 400
enemyY = 100
EmoveX = 0.1
EmoveY = 0
#bullet
bullet = pygame.image.load("bullet.png")
bX = playerX
bY = playerY +20
fired = False
xFired = bX
bmoveY = 0

def player(x,y):
   screen.blit(playerImage, (x, y)) #blit er tegne

def enemy(x,y):
   screen.blit(enemyImage, (x, y)) #blit er tegne
def move():
   global playerX,bX, bmoveY, bY, fired
   playerX +=moveX
   bX = playerX+16
   if fired:
      bX = xFired + 16
      
   if bY <= -20:
      bY = playerY+20
      bmoveY = 0
      fired = False
      
   bY +=bmoveY

   if playerX <= 0:
      playerX = 0
   elif playerX>= 736:
      playerX =736
def moveEnemy():
   global enemyX, enemyY, EmoveX
   
   enemyX +=EmoveX
   
   if enemyX <= 0:
      EmoveX *=-1
      enemyY += 20
   elif enemyX >= 736:
      EmoveX *=-1
      enemyY += 20

#game loop
running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.KEYDOWN:      
         if event.key == pygame.K_LEFT:
            moveX = -0.1
         if event.key == pygame.K_RIGHT:
            moveX = 0.1
         if event.key == pygame.K_SPACE:
            if not fired:
               bmoveY = -0.1
               xFired = playerX
               bY = playerY+20
               fired = True
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            moveX = 0
            moveY = 0
         
   #endre farge på skjermen 
        
   screen.fill((105,105,255))
   screen.blit(background, (0,0) )
   screen.blit(bullet, (bX,bY) )
   move()
   moveEnemy()
   player(playerX, playerY)
   enemy(enemyX, enemyY)
   #oppdater skjermen
   pygame.display.update()


