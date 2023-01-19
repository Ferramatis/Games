import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set the width and height of the screen (width, height).
size = (300, 220)
size_game = (300, 200)  # size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snake Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initial snake block position
snake_x, snake_y = 10, 10

# Initial direction of the snake
direction = "right"

# Initial snake length
snake_length = 5

# List to store the rectangles that represent the snake's body
snake_body = []

# Create the initial snake body
for i in range(snake_length):
    x = snake_x - (i * 10)
    y = snake_y
    snake_body.append(pygame.Rect(x, y, 10, 10))

# Initial apple position
apple_x, apple_y = random.randint(
    0, size_game[0]), random.randint(0, size_game[1])
apple_x -= apple_x % 10
apple_y -= apple_y % 10
# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
grey = (31, 31, 31)

# Font for displaying score
font_style = pygame.font.SysFont(None, 50)


def message(msg, color, x_pos, y_pos):
    mesg = font_style.render(msg, True, color)
    rect = mesg.get_rect()
    rect.center = (x_pos, y_pos)
    screen.blit(mesg, rect)


# Main game loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # Check if a key is pressed
        elif event.type == pygame.KEYDOWN:
            # Check if the left arrow key is pressed
            if event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"

    # update the position of the snake based on the current direction
    if direction == "right":
        snake_x += 10
    elif direction == "left":
        snake_x -= 10
    elif direction == "up":
        snake_y -= 10
    elif direction == "down":
        snake_y += 10

    # Check for collision with the apple
    if snake_body[0].colliderect(pygame.Rect(apple_x, apple_y, 10, 10)):
        # Increase the snake length
        snake_length += 1
        # Add a new rectangle to the snake body
        snake_body.append(pygame.Rect(snake_x, snake_y, 10, 10))
        # Generate a new random position for the apple
        apple_x, apple_y = random.randint(
            0, size_game[0]), random.randint(0, size_game[1])
        apple_x -= apple_x % 10
        apple_y -= apple_y % 10
    # update the position of each segment of the snake based on the previous segment
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i].x = snake_body[i - 1].x
        snake_body[i].y = snake_body[i - 1].y

    # update the head of the snake
    snake_body[0].x = snake_x
    snake_body[0].y = snake_y

    # Check for collision with the snake's body
    for i in range(1, len(snake_body)):
        if snake_body[0].colliderect(snake_body[i]):
            done = True

    # Check if the snake's head is outside of the screen boundaries
    if snake_x + 10 > size_game[0] or snake_y + 10 > size_game[1] or snake_x < 0 or snake_y < 0:
        done = True

    # --- Drawing code should go here
    screen.fill(black)

    if done:
        message("Game Over", red, size_game[0]/2, size_game[1]/2-25)
        message("Score: "+str(snake_length-5), red,
                size_game[0]/2, size_game[1]/2+25)
        pygame.display.update()
        time.sleep(3)
        break

    # Draw the grid
    for i in range(0, size_game[0], 10):
        pygame.draw.line(screen, grey, (i, 0), (i, size_game[1]), 1)
    for j in range(0, size_game[1], 10):
        pygame.draw.line(screen, grey, (0, j), (size_game[0], j), 1)

    # Draw separator line
    pygame.draw.line(screen, (255, 255, 255),
                     (0, size_game[1]), (size[0], size_game[1]), 2)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, white, segment)

    # Draw the apple
    pygame.draw.rect(screen, red, [apple_x, apple_y, 10, 10])

    font_style = pygame.font.SysFont(None, 20)
    score = font_style.render("Score: " + str(snake_length-5), True, white)
    screen.blit(score, (0, size_game[1]+5))

    # Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

# Close the window and quit.
pygame.quit()
