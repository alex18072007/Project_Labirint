import pygame
import os

WIDTH = 600
HEIGHT = 600
FPS = 50

pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ["ГЕЙмМастерс Представляет",
                  "Игра о которой слагают легенды.",
                  "любители Fuckin Slave заценят",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)
start_screen()

if __name__ == '__main__':
    screen.fill('white')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 1073741903:
                    x_pos += 10
                if event.key == 1073741904:
                    x_pos -= 10
                if event.key == 1073741905:
                    y_pos += 10
                if event.key == 1073741906:
                    y_pos -= 10
        pygame.display.flip()
    pygame.quit()