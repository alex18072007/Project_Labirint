import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT, = 480, 480
FPS = 15
MAPS_DIR = 'maps'
TILE_SIZE = 32


class Labyrinth:
    def __init__(self, filename, free, finish):
        self.map = []
        with open(f'{MAPS_DIR}/{filename}') as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free = free
        self.finish = finish

    def render(self, screen):
        colors = {0: (0, 255, 153), 1: (0, 0, 0), 2: (255, 51, 204), 3: (8, 100, 100)}
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size,
                                   self.tile_size, self.tile_size)
                screen.fill(colors[self.get_tile_id((x, y))],  rect)

    def get_tile_id(self, position):
        return self.map[position[1]][position[0]]

    def svoboda(self, position):
        return self.get_tile_id(position) in self.free


class Hero:
    def __init__(self, position):
        self.x, self.y = position

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        center = self.x * TILE_SIZE + TILE_SIZE // 2, self.y * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.circle(screen, (255, 255, 255), center, TILE_SIZE // 2)


class Play:
    def __init__(self, labyrinth, hero):
        self.labyrinth = labyrinth
        self.hero = hero

    def render(self, screen):
        self.labyrinth.render(screen)
        self.hero.render(screen)

    def lvlup_hero(self):
        n_x, n_y = self.hero.get_position()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            n_x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            n_x += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            n_y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            n_y += 1
        if self.labyrinth.svoboda((n_x, n_y)):
            self.hero.set_position((n_x, n_y))

    def win(self):
        return self.labyrinth.get_tile_id(self.hero.get_position()) == self.labyrinth.finish


def messege(screen, massage):
    font = pygame.font.Font(None, 50)
    text = font.render(massage, 1, (50, 70, 0))
    text_x = WINDOW_WIDTH // 2 - text.get_width() // 2
    text_Y = WINDOW_HEIGHT // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(screen, (200, 150, 50), (text_x - 10, text_Y - 10,
                                              text_w + 20, text_h + 20))
    screen.blit(text, (text_x, text_Y))


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    labyrinth = Labyrinth('simle_map.txt', [0, 2, 3], 2)
    hero = Hero((7, 7))
    play = Play(labyrinth, hero)

    clock = pygame.time.Clock()
    running = True
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not game_over:
            play.lvlup_hero()
        screen.fill((0, 0, 0))
        play.render(screen)
        if play.win():
            game_over = True
            messege(screen, 'Победа!')
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
