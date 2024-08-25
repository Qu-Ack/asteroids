import pygame
from asteroidfield import AsteroidField
from asteroids import Asteroid
from constants import *
from player import Player
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    # frame rate logic
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)


    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    ## Game Loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0 , 0 , 0 ,0 ))
        
        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        for asteroid in asteroids:
            if player.detectCollision(asteroid):
                print("Game Over!")
                exit()

            for bullet in shots:
                if bullet.detectCollision(asteroid):
                    bullet.kill()
                    asteroid.split()
            

        pygame.display.flip()

        time_passed = clock.tick(60)
        dt = time_passed/1000



if __name__ == "__main__":
    main()
