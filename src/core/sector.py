# src/core/sector.py

import random


class Sector:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sunlight_exposure = 0
        self.organic_matter = 0
        self.temperature = 0
        self.rainfall = 0

    def update_sunlight(self):
        # Update sunlight exposure based on sector properties
        self.sunlight_exposure = self.calculate_sunlight()

    def update_organic_matter(self):
        # Update organic matter accumulation and its toxic effects
        if self.organic_matter > 100:
            self.organic_matter += 1  # Increase toxicity
        else:
            self.organic_matter += 0.1  # Normal accumulation

    def update_season(self, season_cycle):
        # Change sector properties based on the current season
        if season_cycle == 0:  # Spring
            self.temperature = 15
            self.rainfall = 10
        elif season_cycle == 1:  # Summer
            self.temperature = 25
            self.rainfall = 5
        elif season_cycle == 2:  # Autumn
            self.temperature = 10
            self.rainfall = 15
        elif season_cycle == 3:  # Winter
            self.temperature = 0
            self.rainfall = 20

    def random_event(self):
        # Introduce a random event in the sector
        event_type = random.choice(["storm", "drought", "heatwave"])
        if event_type == "storm":
            self.rainfall += 20
            self.sunlight_exposure -= 10
        elif event_type == "drought":
            self.rainfall -= 20
            self.temperature += 5
        elif event_type == "heatwave":
            self.temperature += 10
            self.sunlight_exposure += 5

    def calculate_sunlight(self):
        # Placeholder method for actual sunlight calculation
        # This should factor in current weather and sector location
        return max(0, 100 - self.rainfall)
