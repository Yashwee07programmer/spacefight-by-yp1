import pygame
import sys
import random
# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player variables
player_width = 50
player_height = 100
player_speed = 8

# Obstacle variables
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

# Load player image
player_image = pygame.image.load("C:\\yashweep\\spacefight\\assets\\spaceship.png")
player_image = pygame.transform.scale(player_image, (player_width, player_height))

# Load obstacle image
obstacle_image = pygame.image.load("C:\\yashweep\\spacefight\\assets\\obstacle.png")
obstacle_image = pygame.transform.scale(obstacle_image, (obstacle_width, obstacle_height))

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space Game")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - player_height // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += player_speed

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - obstacle_width)
        self.rect.y = -obstacle_height

    def update(self):
        self.rect.y += obstacle_speed

def main():
    all_sprites = pygame.sprite.Group()
    obstacles_group = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Generate obstacles
        if random.randint(0, obstacle_frequency) == 0:
            obstacle = Obstacle()
            obstacles_group.add(obstacle)
            all_sprites.add(obstacle)

        all_sprites.update()

        # Remove off-screen obstacles
        obstacles_group = pygame.sprite.Group(
            obstacle for obstacle in obstacles_group if obstacle.rect.y < HEIGHT
        )

        # Check for collisions
        if pygame.sprite.spritecollide(player, obstacles_group, False):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
