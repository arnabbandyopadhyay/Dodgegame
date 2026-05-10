import pygame
import random
import sys


class Dodgegame:
    def __init__(self):
        pygame.init()

        self.width = 600
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Dodge the Blocks")

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)

        self.font = pygame.font.SysFont("Arial", 36)

        self.player_size = 50
        self.player_speed = 10
        self.player_x = self.width // 2
        self.player_y = self.height - self.player_size - 10

        self.block_size = 50
        self.block_speed = 7
        self.blocks = []

        self.score = 0
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

    def move_player(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player_x -= self.player_speed

        if keys[pygame.K_RIGHT]:
            self.player_x += self.player_speed

        self.player_x = max(0, min(self.player_x, self.width - self.player_size))

    def spawn_blocks(self):
        if random.randint(1, 20) == 1:
            x = random.randint(0, self.width - self.block_size)
            self.blocks.append([x, 0])

    def move_blocks(self):
        for block in self.blocks:
            block[1] += self.block_speed

        self.blocks = [block for block in self.blocks if block[1] < self.height]

    def check_collision(self):
        player = pygame.Rect(
            self.player_x,
            self.player_y,
            self.player_size,
            self.player_size
        )

        for block in self.blocks:
            enemy = pygame.Rect(
                block[0],
                block[1],
                self.block_size,
                self.block_size
            )

            if player.colliderect(enemy):
                self.running = False

    def draw_objects(self):
        self.screen.fill(self.white)

        pygame.draw.rect(
            self.screen,
            self.blue,
            (self.player_x, self.player_y, self.player_size, self.player_size)
        )

        for block in self.blocks:
            pygame.draw.rect(
                self.screen,
                self.red,
                (block[0], block[1], self.block_size, self.block_size)
            )

        score_text = self.font.render(
            f"Score: {self.score}", True, self.black
        )
        self.screen.blit(score_text, (10, 10))

        pygame.display.update()

    def game_over(self):
        self.screen.fill(self.white)

        text = self.font.render("Game Over!", True, self.red)
        rect = text.get_rect(center=(self.width // 2, self.height // 2))

        self.screen.blit(text, rect)
        pygame.display.update()
        pygame.time.wait(2000)

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while self.running:
            self.clock.tick(self.fps)

            self.handle_events()
            self.move_player()
            self.spawn_blocks()
            self.move_blocks()
            self.check_collision()

            self.score += 1
            self.draw_objects()

        self.game_over()
        self.quit_game()


if __name__ == "__main__":
    game = Dodgegame()
    game.run()