import pygame

pygame.init() #시작하겠습니다

#window size of 500 width, 500 height
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Movement Practice")

#캐릭터의 위치와 트기
x = 50
y = 50
width = 40
height = 60
velocity = 10

isJump = False
jumpCount = 10

slide = 40

run = True
while run:
    pygame.time.delay(100) #this will delay the game the given amount of millisecond, 감도
    for event in pygame.event.get(): #어떤 이벤트가 일어났을때 모든 정보를 수집해라
        if event.type == pygame.QUIT:
            run = False 
    keys = pygame.key.get_pressed()
    print(keys)

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity

    if keys[pygame.K_RIGHT] and x < 500 - velocity - width:
        x += velocity

    if keys[pygame.K_LCTRL] and x < 500 - slide - width:
        x += slide

    if not (isJump):
        if keys[pygame.K_UP] and y > velocity:
            y -= velocity

        if keys[pygame.K_DOWN] and y < 500 - velocity - height:
            y += velocity

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -5: #어디까지 꺼질거냐
            y -= (jumpCount * abs(jumpCount)) * 0.3 #어디까지 높이 올라갈건지
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False



    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update() #rectangle을 볼수 있게 해줌 frame(깜빡이는 속도)
pygame.quit()

