import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    # frame rate logic
    clock = pygame.time.Clock()
    dt = 0



    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    ## Game Loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(0 , 0 , 0 ,0 ))
        player.draw(screen)
        pygame.display.flip()

        
        time_passed = clock.tick(60)
        dt = time_passed/1000



if __name__ == "__main__":
    main()
