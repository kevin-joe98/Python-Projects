import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# Set the dimensions of the game window
width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define snake parameters
snake_block = 10
snake_speed = 15

# Define clock to control the game speed
clock = pygame.time.Clock()

# Set font for score display
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def display_score(score):
    value = score_font.render("Score: " + str(score), True, BLACK)
    window.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, BLACK, [x[0], x[1], snake_block, snake_block])

# Function to display message (e.g., when game over)
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

# Main game loop
def game_loop():
    # Initial position of the snake
    game_over = False
    game_close = False

    x1 = width // 2
    y1 = height // 2

    # Movement variables for the snake
    x1_change = 0
    y1_change = 0

    # Snake parameters
    snake_list = []
    snake_length = 1

    # Place the first food item randomly
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Score counter
    score = 0

    while not game_over:

        while game_close:
            window.fill(WHITE)
            display_message("Game Over! Press Q-Quit or C-Play Again", RED)
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle user inputs for controlling the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Game over if the snake hits the wall
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update the game display and draw the background
        window.fill(WHITE)

        # Draw the food
        pygame.draw.rect(window, GREEN, [food_x, food_y, snake_block, snake_block])

        # Update the snake's position and draw it
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(score)

        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
