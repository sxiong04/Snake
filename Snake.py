import pygame
import random
import time

red = (255, 0, 0)
green = (0, 255, 0)
SCREEN = 1000
SIZE = 25
x = int(random.randint(int(SCREEN / SIZE / 4), int(SCREEN / SIZE / 2))) * SIZE
y = int(random.randint(int(SCREEN / SIZE / 4), int(SCREEN / SIZE / 2))) * SIZE


class Apple:
    def __init__(self, surface):
        self.surface = surface
        self.x = int(random.randint(0, int(SCREEN / SIZE))) * SIZE
        self.y = int(random.randint(0, int(SCREEN / SIZE))) * SIZE

    def draw(self):
        pygame.display.update()
        pygame.draw.rect(self.surface, red, (self.x, self.y, SIZE, SIZE))
        pygame.display.update()

    def move(self):
        self.x = int(random.randint(0, int(SCREEN / SIZE) - 1)) * SIZE
        self.y = int(random.randint(0, int(SCREEN / SIZE) - 1)) * SIZE
        self.draw()


class Snake:
    def __init__(self, surface, length):
        self.length = length
        self.surface = surface
        self.x = [x] * length
        self.y = [y] * length
        self.direction = random.choice(["left", "right", "up", "down"])

    def draw(self):
        pygame.display.update()
        self.surface.fill((0, 0, 0))
        for i in range(self.length):
            pygame.draw.rect(self.surface, green, (self.x[i], self.y[i], SIZE, SIZE))
            pygame.display.update()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == "left":
            self.x[0] -= SIZE
        elif self.direction == "right":
            self.x[0] += SIZE
        elif self.direction == "up":
            self.y[0] -= SIZE
        else:
            self.y[0] += SIZE
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN, SCREEN))
        self.snake = Snake(self.surface, 5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: {self.snake.length - 5}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.score()
        pygame.display.update()
        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.apple.move()
            self.snake.increase_length()

        for i in range(1, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game Over"

    def collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    def show_game_over(self):
        self.surface.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 30)
        line = font.render(f"Game Over! Your score is {self.snake.length - 5}\nTo play the game again, Press Enter", True, (255, 255, 255))
        self.surface.blit(line, (500, 400))
        pygame.display.update()
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                    elif event.key == pygame.K_UP:
                        self.snake.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.move_down()

            self.play()
            try:
                self.play()
            except Exception as e:
                self.show_game_over()
            time.sleep(.1)


if __name__ == "__main__":
    game = Game()
    game.run()
