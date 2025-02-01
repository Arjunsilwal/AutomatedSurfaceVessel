import pygame


class GraphicsManager:
    def __init__(self, width, height, caption):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

    def clear_screen(self, color):
        self.screen.fill(color)

    def update_display(self):
        pygame.display.flip()
        self.clock.tick(60)

    def get_screen(self):
        return self.screen

    def quit(self):
        pygame.quit()