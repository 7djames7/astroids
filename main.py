import pygame
from constants import *
from circleshape import CircleShape
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # Game initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Time initialization
    absolute_time = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add to Groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Generate game objects
    player1 = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroidfield = AsteroidField()



    # Game Loop
    while True:
        # Grab Escape command
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Move objects
        for updatables in updatable:
            updatables.update(dt)

        # Collision Loop
        for asteroid in asteroids:
            # Shot Collision
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

            # Player Collision
            if player1.collision(asteroid):
                print("Game over!")
                raise SystemExit

        # Render portion    
        screen.fill("black") # Initialize Background
        
        for drawables in drawable: # Draw all objects
            drawables.draw(screen) 

        pygame.display.flip() # Refresh
        
        # Limit FPS to tick(60) in fps
        dt = absolute_time.tick(60)/1000

if __name__ == "__main__":
    main()