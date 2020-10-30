import pygame
from pygame.sprite import Sprite
from pygame.draw import line


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its startingposition."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image,
                                            (int(ai_settings.screen_width/14),
                                             int(ai_settings.screen_height/14)))
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen.
        self.rect.right = self.screen_rect.right
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its currenet location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of scoreboard."""
        screen_rect = self.screen.get_rect()
        self.line = line(self.screen, (0, 0, 0), (
            self.screen_rect.right, 40), (self.screen_rect.left, 40))
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= self.line.bottom:
            return True

    def update(self):
        """Move the alien down or up."""
        self.y -= (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.y = self.y
