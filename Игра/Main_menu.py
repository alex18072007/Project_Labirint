import random
import sys

import pygame
from PyQt5 import QtCore, QtMultimedia
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush, QPixmap
# pygame.mixer.music.load()
# pygame.mixer.music.play()
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
        center = (self.x * TILE_SIZE + TILE_SIZE // 2) - 16, (self.y * TILE_SIZE + TILE_SIZE // 2) - 16
        pers = pygame.image.load('creature (1).png')
        PERS_SIZE = (32, 32)
        pers = pygame.transform.scale(pers, PERS_SIZE)
        screen.blit(pers, center)


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
        if pygame.key.get_pressed()[pygame.K_m]:
            print('process')
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            n_y += 1
        if pygame.key.get_pressed()[pygame.K_a]:
            n_x -= 1
        if pygame.key.get_pressed()[pygame.K_d]:
            n_x += 1
        if pygame.key.get_pressed()[pygame.K_w]:
            n_y -= 1
        if pygame.key.get_pressed()[pygame.K_s]:
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


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Main_menu.ui', self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/maxresdefault.jpg")))
        self.setPalette(pal)
        self.logo.resize(300, 300)
        self.pixmap = QPixmap('./data/Logo_comp.png')
        self.logo.setPixmap(self.pixmap)
        self.exit.clicked.connect(self.Exit)
        self.pushButton.clicked.connect(self.qwe)
        self.pushButton_2.clicked.connect(self.Sentinngs)
        self.load_mp3('./data/Musika/Funny_calm_relax_fone_music.mp3')
        self.player.play()

    def Sentinngs(self):
        uic.loadUi("Sentinngs.ui", self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/1200x900.jpg")))
        self.setPalette(pal)
        self.pushButton_2.clicked.connect(self.Troll)
        self.pushButton_3.clicked.connect(self.Titels)
        self.load_mp3('./data/Musika/Ph.mp3')
        self.player.play()

    def Titels(self):
        uic.loadUi("Titles.ui", self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/Ночь.jpg")))
        self.setPalette(pal)
        self.pushButton.clicked.connect(self.Sentinngs)
        self.load_mp3('./data/Musika/Titels.mp3')
        self.player.play()

    def Troll(self):
        uic.loadUi("Troll.ui", self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/Donat.jpg")))
        self.setPalette(pal)
        self.pushButton.clicked.connect(self.Sentinngs)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def Exit(self):
        uic.loadUi("Exit.ui", self)
        self.Yes.clicked.connect(self.close())
        self.pushButton_2.clicked.connect(self.No_Exit)

    def qwe(self):
        sw = Play(labyrinth, hero)
        sw.show()

    def No_Exit(self):
        print('Завершение')

    def Yes_Exit(self):
        print('назад')


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    labyrinth = Labyrinth('second_card', [0, 2, 3], 2)
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
    # main()
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
