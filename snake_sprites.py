#!/usr/bin/env python
import pygame
from pygame.locals import USEREVENT
import random

# constants
ROWS, COLS = 20, 20
CELL_SIZE = 25
WINDOW_WIDTH, WINDOW_HEIGHT = CELL_SIZE*COLS, CELL_SIZE*ROWS

SNAKE_SIZE = CELL_SIZE
SNAKE_COLOR = (0, 0, 255)

APPLE_SIZE = CELL_SIZE
APPLE_COLOR = (0, 255, 0)

TIMER_EVENT = USEREVENT + 1


class Snake_Part(pygame.sprite.Sprite):
    def __init__(self, coords):
        """ Draws a snake part at the given coords.

            Attributes:
                coords (list): Snake part coordinates.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SNAKE_SIZE, SNAKE_SIZE))
        self.rect = self.image.get_rect()

        pygame.draw.rect(self.image, SNAKE_COLOR, [0, 0, SNAKE_SIZE, SNAKE_SIZE])
        self.move_to_position(coords[0], coords[1])

    def move_to_position(self, x, y):
        """ Moves the sprite to the given position.

            Attributes:
                x (int): x-position.
                y (int): y-position.
        """
        sprite_x = x*COLS
        sprite_y = y*ROWS

        self.rect.x, self.rect.y = sprite_x, sprite_y


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        """ Draws a rectangular apple at a random position.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((APPLE_SIZE, APPLE_SIZE))
        self.rect = self.image.get_rect()

        pygame.draw.rect(self.image, APPLE_COLOR, [0, 0, APPLE_SIZE, APPLE_SIZE])
        self.move_to_random_position()

    def update(self):
        """ Called by Group::update() method in main loop.
        """
        self.move_to_random_position()

    def move_to_random_position(self):
        """ Moves the sprite to a random position.
        """
        sprite_x = random.randrange(COLS)*COLS
        sprite_y = random.randrange(ROWS)*ROWS

        if sprite_x + APPLE_SIZE > WINDOW_WIDTH:
            sprite_x = WINDOW_WIDTH - APPLE_SIZE
        if sprite_y + APPLE_SIZE > WINDOW_HEIGHT:
            sprite_y = WINDOW_HEIGHT - APPLE_SIZE

        self.rect.x, self.rect.y = sprite_x, sprite_y
