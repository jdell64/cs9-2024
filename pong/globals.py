import pygame

pygame.init()

font20 = pygame.font.Font('SpaceMono-Regular.ttf', 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 900, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 30