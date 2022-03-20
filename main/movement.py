import pygame

pygame.init() #시작하겠습니다

#window size of 500 width, 500 height
win = pygame.display.set_mode((500,500))
win = pygame.display.set_caption("Movement Practice")

#캐릭터의 위치와 트기
x = 50
y = 50
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.delay(100) #this will delay the game the given amount of millisecond, 감도
    for event in pygame.event.get(): #어떤 이벤트가 일어났을때 모든 정보를 수집해라
        if event.type == pygame.QUIT:
            run = False 

    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update() #rectangle을 볼수 있게 해줌 frame(깜빡이는 속도)
pygame.quit()

