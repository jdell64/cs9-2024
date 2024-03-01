import pygame
from globals import HEIGHT, WIDTH, screen, GREEN, WHITE, BLACK, FPS, clock, WINNING_SCORE
from striker import Striker
from ball import Ball
from utils import reset_game

# Game Manager
def main():
    running = True

    # Load music
    pygame.mixer.music.load("bg.wav", "wav")
    pygame.mixer.music.play(-1)
    hit_sound = pygame.mixer.Sound("hit.wav")
 
    # Defining the objects
    player_start_y = HEIGHT//2 - 50
    geek1 = Striker(20, player_start_y, 10, 100, 10, GREEN)
    geek2 = Striker(WIDTH-30, player_start_y, 10, 100, 10, GREEN)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
 
    listOfGeeks = [geek1, geek2]
 
    # Initial parameters of the players
    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0

    while running:
        screen.fill(BLACK)
 
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                if event.key == pygame.K_DOWN:
                    geek2YFac = 1
                if event.key == pygame.K_w:
                    geek1YFac = -1
                if event.key == pygame.K_s:
                    geek1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0
 
        # Collision detection
        for geek in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                hit_sound.play()
                ball.hit()
 
        # Updating the objects
        geek1.update(geek1YFac)
        geek2.update(geek2YFac)
        point = ball.update()
 
        # -1 -> Geek_1 has scored
        # +1 -> Geek_2 has scored
        #  0 -> None of them scored
        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1
 
        if point:   # Someone has scored a point and the
          # ball is out of bounds. So, we reset it's position
            ball.reset()
            if geek1Score >= WINNING_SCORE:
                # show a win screen, then after key press, reset game
                reset_game(ball, listOfGeeks)
                geek1Score = 0
                geek2Score = 0
            elif geek2Score >= WINNING_SCORE:
                reset_game(ball, listOfGeeks)
                geek1Score = 0
                geek2Score = 0


        # Displaying the objects on the screen
        geek1.display()
        geek2.display()
        ball.display()
 
        # Displaying the scores of the players
        geek1.displayScore("Geek_1 : ", geek1Score, 100, 20, WHITE)
        geek2.displayScore("Geek_2 : ", geek2Score, WIDTH-100, 20, WHITE)
 
        pygame.display.update()
        # Adjusting the frame rate
        clock.tick(FPS)

