import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up game variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 15
PAD_WIDTH, PAD_HEIGHT = 10, 100
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [random.choice([1, -1]) * random.uniform(2, 4), random.choice([1, -1]) * random.uniform(2, 4)]
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT // 2 - HALF_PAD_HEIGHT]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH - PAD_WIDTH, HEIGHT // 2 - HALF_PAD_HEIGHT]
paddle1_vel = 0
paddle2_vel = 0
paddle_speed = 6
score1, score2 = 0, 0

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_vel = -paddle_speed
            elif event.key == pygame.K_s:
                paddle1_vel = paddle_speed
            elif event.key == pygame.K_UP:
                paddle2_vel = -paddle_speed
            elif event.key == pygame.K_DOWN:
                paddle2_vel = paddle_speed
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                paddle1_vel = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                paddle2_vel = 0

    # Update paddle positions
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel

    # Keep paddles on the screen
    paddle1_pos[1] = max(paddle1_pos[1], 0)
    paddle1_pos[1] = min(paddle1_pos[1], HEIGHT - PAD_HEIGHT)
    paddle2_pos[1] = max(paddle2_pos[1], 0)
    paddle2_pos[1] = min(paddle2_pos[1], HEIGHT - PAD_HEIGHT)

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Ball collision with top and bottom
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # Ball collision with paddles
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and paddle1_pos[1] < ball_pos[1] < paddle1_pos[1] + PAD_HEIGHT) or (
            ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and paddle2_pos[1] < ball_pos[1] < paddle2_pos[1] + PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0]

    # Ball out of bounds
    if ball_pos[0] <= BALL_RADIUS:
        score2 += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_vel = [random.choice([1, -1]) * random.uniform(2, 4), random.choice([1, -1]) * random.uniform(2, 4)]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        score1 += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_vel = [random.choice([1, -1]) * random.uniform(2, 4), random.choice([1, -1]) * random.uniform(2, 4)]

    # Draw everything
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(window, WHITE, (paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.circle(window, WHITE, ball_pos, BALL_RADIUS)
    pygame.draw.line(window, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(score1), 1, WHITE)
    window.blit(text, (250, 10))
    text = font.render(str(score2), 1, WHITE)
    window.blit(text, (510, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()