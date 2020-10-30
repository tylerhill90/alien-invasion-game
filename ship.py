import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image,
                                            (int(ai_settings.screen_width/10),
                                             int(ai_settings.screen_height/10)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the leftside center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centery)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > self.screen_rect.top + 40:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and (self. rect.bottom <
                                 self.screen_rect.bottom):
            self.center += self.ai_settings.ship_speed_factor

        self.rect.centery = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centery
