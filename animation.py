import pygame
pygame.init()


# игрок
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        # переменные передвижения по вертикали и горизонтали
        self.dx = 0
        self.dy = 0

        self.Go = False
        self.Frame = 0

        self.Left = False
        self.Right = True
        self.Up = False
        self.Down = False

    # движение
    def update(self, *args):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # проверка на сторону движения
        if self.Right:
            file = 'right'
        elif self.Left:
            file = 'left'
        elif self.Up:
            file = 'right'
        else:
            file = 'right'

        # анимация
        if self.Go:
            self.Frame += 0.2
            if self.Frame > 6:
                self.Frame -= 6

            Personnel = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png']
            self.image = pygame.image.load('image/' + file + '/' + Personnel[int(self.Frame)]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (player.rect.width * 3, player.rect.height * 3))
        else:
            self.image = pygame.image.load('image/' + file + '/3.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (player.rect.width * 3, player.rect.height * 3))

        # обнуление движения
        self.dy = 0
        self.dx = 0


width, height = 2000, 1000

sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# создание игрока
player = Object(100, 400, 'image/right/3.png')

while True:
    sc.fill(pygame.Color('white'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYUP:
            player.Go = False

    key = pygame.key.get_pressed()

    # движение вправо
    if key[pygame.K_RIGHT]:
        player.dx = 5

        player.Go = True

        player.Up = False
        player.Down = False
        player.Left = False
        player.Right = True

    # движение влево
    if key[pygame.K_LEFT]:
        player.dx = -5

        player.Go = True

        player.Up = False
        player.Down = False
        player.Left = True
        player.Right = False

    # движение вверх
    if key[pygame.K_UP]:
        player.dy = -5

        player.Go = True

        player.Down = False
        player.Up = True

    # движение вниз
    if key[pygame.K_DOWN]:
        player.dy = 5

        player.Go = True

        player.Down = True
        player.Up = False

    player.update(height - player.rect.height * 3)
    sc.blit(player.image, player.rect)

    pygame.display.update()
    clock.tick(60)
