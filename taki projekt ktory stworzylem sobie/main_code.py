import c
import pygame
import sys

pygame.init()

screen_size = 800, 600
screen = pygame.display.set_mode(screen_size)
screen_center = (screen_size[0] // 2, screen_size[1] // 2)


class Button:
    def __init__(self, pos, width, height, color):
        x, y = pos
        self.rect = (x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def clicked(self, mouse_pos):
        x_check = self.rect[0] < mouse_pos[0] < self.rect[0] + self.rect[2]
        y_check = self.rect[1] < mouse_pos[1] < self.rect[1] + self.rect[3]
        if x_check and y_check:
            return True


def main(s):
    button = Button(screen_center, 20, 10, c.blue)
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.clicked(event.pos):
                    print("Wydaje mi się że kliknąłeś niebieski przycisk")
            screen.fill(c.black)
            button.draw()
            pygame.display.flip()
    sys.exit()


if __name__ == "__main__":
    main("nine")

