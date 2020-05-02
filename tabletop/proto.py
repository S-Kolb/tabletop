import pygame
import math
import time



WIDTH = 1920
HEIGHT = 1080


class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption('Josh says snake!')
        self.clock = pygame.time.Clock()
        self.draw_map(r'C:\py_repos\tabletop\tabletop\images\shack1.jpg')

    def draw_map(self, image_path):
        map = pygame.image.load(image_path)
        scale = min(WIDTH / map.get_size()[0], HEIGHT / map.get_size()[1])
        map = pygame.transform.scale(map, (math.floor(scale*map.get_size()[0]), math.floor(scale*map.get_size()[1])))

        self.display.blit(map, (0, 0))

def escape_message(display, message='Hit enter to exit or any other key to continue.'):
    # large_text = pygame.font.Font('freesansbold.ttf', 72)
    text = pygame.font.Font.render(message, True, (255, 255, 255), background=(0, 0, 0))
    text.center((WIDTH/2), (HEIGHT/2))
    display.blit(text, text.get_rect())
    display.update()
    time.sleep(2)
    game_loop()


def game_loop():
    pygame.init()
    game = Game()

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                k = pygame.key.get_pressed()
                if k[pygame.K_ESCAPE]:
                    escape_message(pygame.display)
                    escape = True
                    while escape:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                k = pygame.key.get_pressed()
                                if k[pygame.K_RETURN]:
                                    escape = run = False
                                else:
                                    escape = False


        pygame.display.update()
        game.clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()

