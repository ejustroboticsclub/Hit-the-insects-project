import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1000, 800
if WIDTH < 2:  # Ensure WIDTH is at least 2
    WIDTH = 2
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hit the Insect - Two Players")

# Colors
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (100, 100, 100)

# Fonts
FONT = pygame.font.Font(None, 36)

# Insects
INSECT_SPEED = 5
INSECT_FOLDER = "insects/"  # Folder containing insect images       #insects\\ for windows
INSECT_FILES = ["ant.png", "bee.png", "cricket.png", "dragonfly.png", "fly.png"]  # List of insect image files

# Player areas
PLAYER_AREA_WIDTH = WIDTH // 2

class Insect:
    def __init__(self, player):
        self.image = self.load_random_insect()
        self.rect = self.image.get_rect()
        self.rect.x = int(random.uniform(player * PLAYER_AREA_WIDTH, min((player + 1) * PLAYER_AREA_WIDTH - self.rect.width, WIDTH - self.rect.width)))
        self.rect.y = -self.rect.height

    def load_random_insect(self):
        insect_image = pygame.image.load(INSECT_FOLDER + random.choice(INSECT_FILES))
        return insect_image

    def move(self):
        self.rect.y += INSECT_SPEED

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class HitTheInsectGame:
    def __init__(self):
        self.player_scores = [0, 0]
        self.insects = [[], []]  # Separate insect lists for each player

    def spawn_insect(self, player):
        insect = Insect(player)
        self.insects[player].append(insect)

    def check_collision(self, x, y):
        for insects in self.insects:
            for insect in insects:
                if insect.rect.collidepoint(x, y):
                    player = 0 if insect.rect.x < PLAYER_AREA_WIDTH else 1
                    self.player_scores[player] += 1
                    insects.remove(insect)
                    return True
        return False

    def update(self):
        for insects in self.insects:
            for insect in insects:
                insect.move()

                # Remove insects that are out of the screen
                if insect.rect.y > HEIGHT:
                    insects.remove(insect)

    def draw(self, surface):
        surface.fill(GREEN)  # Fill the background with green

        for i, insects in enumerate(self.insects):
            for insect in insects:
                insect.draw(surface)

            score_text = FONT.render(f"Player {i+1} Score: {self.player_scores[i]}", True, BLACK)
            surface.blit(score_text, (i * (WIDTH // 2) + 20, 20))

        # Draw centered line between player areas
        pygame.draw.line(surface, LINE_COLOR, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 3)

def main():
    game = HitTheInsectGame()

    clock = pygame.time.Clock()
    running = True

    SPAWN_EVENT = pygame.USEREVENT
    pygame.time.set_timer(SPAWN_EVENT, 1000)  # Spawn an insect every second

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWN_EVENT:
                for player in range(2):
                    game.spawn_insect(player)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.check_collision(*pygame.mouse.get_pos()):
                    print("Hit!")

        game.update()
        game.draw(WINDOW)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
