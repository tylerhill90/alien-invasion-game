import pygame
from pygame.sprite import Sprite


class Life(Sprite):
    """A class to represent a single life left."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its startingposition."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/life.png')
        self.image = pygame.transform.scale(self.image,
                                            (int(ai_settings.screen_width/20),
                                             int(ai_settings.screen_height/20)))
        self.rect = self.image.get_rect()
