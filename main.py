import pygame

pygame.init()
screen_size = (screen_width,screen_height) = (1280,720)
screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font("FiraCode-Regular.ttf", 24)
clock = pygame.time.Clock()
running = True

class PLAYER:
    def __init__(self,left=screen_width/2,top=screen_height/2+200,width=45,height=80,color="green",speed=5):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.rlim = screen_width-width
        self.ulim = 0
        self.llim = 0
        self.dlim = screen_height-height

    def Draw(self):
        pygame.draw.rect(screen,self.color,(self.left,self.top,self.width,self.height))

    def Left(self):
        self.left-=self.speed
        if self.left<self.llim:
            self.left=self.llim

    def Right(self):
        self.left+=self.speed
        if self.left>self.rlim:
            self.left=self.rlim

    def Up(self):
        self.top-=self.speed
        if self.top<self.ulim:
            self.top=self.ulim

    def Down(self):
        self.top+=self.speed
        if self.top>self.dlim:
            self.top=self.dlim

playing = False
controls_info = font.render("Controls:   Player - 1: W, S    Player - 2: UP, Down",True,"white")
controls_rect = controls_info.get_rect(center=(screen_width//2,screen_height//2-200))
start_info = font.render("Press SPACE to start the game",True,"white")
start_rect = start_info.get_rect(center=(screen_width//2,screen_height//2+200))
Player1 = PLAYER(0, screen_height//2, 10, 40, "white")
Player2 = PLAYER(screen_width - 10, screen_height//2, 10, 40, "white")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    screen.fill("black")

    if playing:
        if keys[pygame.K_w]:
            Player1.Up()
        if keys[pygame.K_s]:
            Player1.Down()
        if keys[pygame.K_UP]:
            Player2.Up()
        if keys[pygame.K_DOWN]:
            Player2.Down()

        Player1.Draw()
        Player2.Draw()

        

    elif keys[pygame.K_SPACE]:
        playing = True

    else:
        screen.blit(controls_info, controls_rect)
        screen.blit(start_info, start_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
