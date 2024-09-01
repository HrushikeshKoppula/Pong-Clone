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
        self.points = 0
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

class BALL:
    def __init__(self):
        self.velx = 2
        self.vely = 4
        self.centrex = screen_width//2
        self.centrey = screen_height//2

    def collision_control(self):
        self.rect = pygame.Rect(self.centrex-5, self.centrey-5,10,10)
        Player1.rect = pygame.Rect(Player1.left, Player1.top, Player1.width, Player1.height)
        Player2.rect = pygame.Rect(Player2.left, Player2.top, Player2.width, Player2.height)
        if self.rect.colliderect(Player1.rect) or self.rect.colliderect(Player2.rect):
            self.velx = -self.velx

    def Move(self):
        self.centrex += self.velx
        self.centrey += self.vely
        if self.centrey < 5 or self.centrey > screen_height - 5:
            self.vely = -self.vely
        if self.centrex < 5:
            Player2.points += 1
            self.centrex = screen_width//2
            self.centrey = screen_height//2
        if self.centrex > screen_width - 5:
            Player1.points += 1
            self.centrex = screen_width//2
            self.centrey = screen_height//2

    def Draw(self):
        pygame.draw.circle(screen, "white", (self.centrex, self.centrey), 5)

def BoardDraw(Player1, Player2, Ball):
    Ball.collision_control()
    Ball.Move()
    Player1.Draw()
    Player2.Draw()
    Ball.Draw()
    p1 = font.render(str(Player1.points),True,(100, 100, 100))
    p1_rect = p1.get_rect(center=(screen_width//4, screen_height//4))
    screen.blit(p1, p1_rect)
    p2 = font.render(str(Player2.points),True,(100, 100, 100))
    p2_rect = p2.get_rect(center=(3*screen_width//4, screen_height//4))
    screen.blit(p2, p2_rect)
    for i in range(45):
        pygame.draw.rect(screen, (100, 100, 100),(screen_width//2-2, i*16, 4, 8))


playing = False
controls_info = font.render("Controls:   Player - 1: W, S    Player - 2: UP, Down",True,"white")
controls_rect = controls_info.get_rect(center=(screen_width//2,screen_height//2-200))
start_info = font.render("Press SPACE to start the game",True,"white")
start_rect = start_info.get_rect(center=(screen_width//2,screen_height//2+200))
Player1 = PLAYER(0, screen_height//2-20, 10, 40, "white")
Player2 = PLAYER(screen_width - 10, screen_height//2-20, 10, 40, "white")
Ball = BALL()

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

        BoardDraw(Player1, Player2, Ball)
        

    elif keys[pygame.K_SPACE]:
        playing = True

    else:
        screen.blit(controls_info, controls_rect)
        screen.blit(start_info, start_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
