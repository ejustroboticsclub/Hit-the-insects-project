import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Get the screen width and height
SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h

# Set up display
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Hit the Insect - One Player")

# Load background image
BACKGROUND_FILE = "E:\\robotics club\\Hit-the-insects-project\\garden.png"  # file path
BACKGROUND_IMAGE = pygame.image.load(BACKGROUND_FILE)
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonts
FONT = pygame.font.Font(None, 36)

# Insects
INSECT_SPEED = 5
INSECT_FOLDER = "E:\\robotics club\\Hit-the-insects-project\\insects\\"  # Folder containing insect images
INSECT_FILES = ["ant.png", "bee.png", "cricket.png", "dragonfly.png", "fly.png", "spider.gif"]  # List of insect image files

# Game parameters
ROUND_DURATION = 20  #  in seconds
round_start_time = None  

class Insect:
    def __init__(self):
        self.image = self.load_random_insect()
        self.rect = self.image.get_rect()
        max_x = max(SCREEN_WIDTH - self.rect.width, 0)
        self.rect.x = random.randint(0, max_x)
        self.rect.y = -self.rect.height

    def load_random_insect(self):
        insect_image = pygame.image.load(INSECT_FOLDER + random.choice(INSECT_FILES))
        insect_image = pygame.transform.scale(insect_image, (int(insect_image.get_width() * 0.2), int(insect_image.get_height() * 0.2)))
        return insect_image

    def move(self):
        self.rect.y += INSECT_SPEED

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class HitTheInsectGame:
    def __init__(self):
        self.player_score = 0
        self.insects = []
        self.game_over = False  # Flag to indicate game over state
        self.round_end_time = None  # Time when the round ends

    def spawn_insect(self):
        if not self.game_over:
            insect = Insect()
            self.insects.append(insect)

    def check_collision(self, x, y):
        for insect in self.insects:
            if insect.rect.collidepoint(x, y):
                self.player_score += 1
                self.insects.remove(insect)
                return True
        return False

    def update(self):
        if not self.game_over:
            for insect in self.insects:
                insect.move()
                if insect.rect.y > SCREEN_HEIGHT:
                    self.insects.remove(insect)

    def draw(self, surface):
        surface.blit(BACKGROUND_IMAGE, (0, 0))

        for insect in self.insects:
            insect.draw(surface)

        score_text = FONT.render(f"Score: {self.player_score}", True, (255, 255, 255))
        surface.blit(score_text, (20, 20))

        if self.game_over:
            final_score_text = FONT.render(f"Final Score: {self.player_score}", True, (255, 255, 255))
            surface.blit(final_score_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 40))

def main():
    game = HitTheInsectGame()

    clock = pygame.time.Clock()
    running = True

    SPAWN_EVENT = pygame.USEREVENT
    pygame.time.set_timer(SPAWN_EVENT, 1000)

    global round_start_time
    round_start_time = pygame.time.get_ticks()

    while running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - round_start_time) // 1000

        if game.game_over and game.round_end_time is None:
            game.round_end_time = current_time + 20 * 1000  # Set the end time of the round

        if game.game_over and current_time >= game.round_end_time:
            game = HitTheInsectGame()  # Restart the game
            round_start_time = pygame.time.get_ticks()  # Reset round start time
            continue

        if elapsed_time >= ROUND_DURATION:
            if not game.game_over:
                print("Time Out!")
                game.game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWN_EVENT:
                game.spawn_insect()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not game.game_over:
                    if game.check_collision(*pygame.mouse.get_pos()):
                        print("Hit!")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Exit the game when Esc key is pressed

        game.update()
        game.draw(WINDOW)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
