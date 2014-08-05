#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys
from snake_sprites import *

# game vars
score = 0
direction = 'right'
snake_coords = [(6, 5), (5, 5)]
apple_coords = []

# game init
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game - Score: %s" % score)
clock = pygame.time.Clock()

# groups & sprites
sprites_group = pygame.sprite.Group()

apple = Apple()
sprites_group.add(apple)

# sync movement
pygame.time.set_timer(TIMER_EVENT, 200)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direction = 'right'
            elif event.key == K_LEFT:
                direction = 'left'
            elif event.key == K_UP:
                direction = 'up'
            elif event.key == K_DOWN:
                direction = 'down'
        elif event.type == TIMER_EVENT:
            # move snake's head & follow it with other parts
            snake_head = snake_coords[0]
            del snake_coords[-1]

            if direction == 'right':
                snake_coords.insert(0, (snake_head[0] + 1, snake_head[1]))
            elif direction == 'left':
                snake_coords.insert(0, (snake_head[0] - 1, snake_head[1]))
            elif direction == 'top':
                snake_coords.insert(0, (snake_head[0], snake_head[1] - 1))
            elif direction == 'down':
                snake_coords.insert(0, (snake_head[0], snake_head[1] + 1))

    # render window
    sprites_group.empty()
    window.fill((0, 0, 0))

    # render sprites
    for i, coord in enumerate(snake_coords):
        # check for collision between head & apple
        snake_part = Snake_Part(coord)
        sprites_group.add(snake_part)

    sprites_group.draw(window)

    # refresh screen
    clock.tick(60)
    pygame.display.flip()
