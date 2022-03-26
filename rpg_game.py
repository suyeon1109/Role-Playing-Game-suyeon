import pygame

pygame.init() #시작하겠습니다

#window size of 500 width, 500 height
win = pygame.display.set_mode((480,480))
pygame.display.set_caption("Pirate Game")

walkRight = [pygame.image.load('source/R1.png'),
pygame.image.load('source/R2.png'),
pygame.image.load('source/R3.png'),
pygame.image.load('source/R4.png'),
pygame.image.load('source/R5.png'),
pygame.image.load('source/R6.png'),
pygame.image.load('source/R7.png'),
pygame.image.load('source/R8.png'),
pygame.image.load('source/R9.png')]

walkLeft = [pygame.image.load('source/L1.png'),
pygame.image.load('source/L2.png'),
pygame.image.load('source/L3.png'),
pygame.image.load('source/L4.png'),
pygame.image.load('source/L5.png'),
pygame.image.load('source/L6.png'),
pygame.image.load('source/L7.png'),
pygame.image.load('source/L8.png'),
pygame.image.load('source/L9.png')]

bg = pygame.image.load('source/bg.jpg')
char = pygame.image.load('source/standing.png')


#캐릭터의 위치와 크기
x = 50
y = 400
width = 40
height = 60
velocity = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

slide = 80

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0)) #this will draw our background image at (0,0)

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1

    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    
    else:
        win.blit(char, (x,y))
        walkCount = 0

    pygame.display.update()


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get(): #어떤 이벤트가 일어났을때 모든 정보를 수집해라
        if event.type == pygame.QUIT:
            run = False 
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - velocity - width:
        x += velocity
        left = False
        right = True
    
    else:
        left = False 
        right = False
        walkCount = 0

    if not (isJump):
        # if keys[pygame.K_UP] and y > velocity:
        #     y -= velocity

        # if keys[pygame.K_DOWN] and y < 500 - velocity - height:
        #     y += velocity

        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10: #어디까지 꺼질거냐
            y -= (jumpCount * abs(jumpCount)) * 0.3 #어디까지 높이 올라갈건지
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()