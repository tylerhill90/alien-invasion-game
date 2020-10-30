#!/usr/bin/env python3

"""A game where you defend from invading aliens. Every level the aliens get
faster!
"""

import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    """Run the game until all lives are expended. Ask to play again.
    """

    # Initialize game, settings, and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aliean Invasion")

    # Make the Play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics + create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make an alien group.
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        ship, aliens, bullets)

        if stats.game_active:
            # Update ship position
            ship.update()
            # Update bullet(s) position(s)
            gf.update_bullets(ai_settings, screen, stats, sb, ship,
                              aliens, bullets)
            # Update alien positions
            gf.update_aliens(ai_settings, screen, stats, sb, ship,
                             aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()
