import pygame


class Clock():

    def __init__(self):
        self.width, self.height = 650, 650
        self.white = (255, 255, 255)
        self.blue = (34, 79, 228)  # back grond color
        self.FPS = 60
        self.center = (self.width//2, self.height//2)
        self.clock_radius = self.width//2

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Analog Clock")
        self.clock = pygame.time.Clock()

    def draw_circle(self, screen):
        # main circle
        pygame.draw.circle(self.screen, self.white,
                           self.center, self.clock_radius - 10, 5)
        
        #central circle
        pygame.draw.circle(self.screen, self.white,
                           self.center, 10)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.screen.fill(self.blue)
            self.draw_circle(self.screen)

            pygame.display.update()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    myClocl = Clock()
    myClocl.run()
