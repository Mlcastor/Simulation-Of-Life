# src/core/world.py

import random
from src.core.sector import Sector


class World:
    def __init__(self, width=1800, height=1400, num_sectors=8):
        self.width = width
        self.height = height
        self.sectors = self._create_sectors(num_sectors)
        self.grid = self._create_grid()
        self.season_cycle = 0
        self.random_events = []

    def _create_sectors(self, num_sectors):
        # Divide the world into sectors
        sectors = []
        sector_width = self.width // num_sectors
        sector_height = self.height // num_sectors
        for i in range(num_sectors):
            for j in range(num_sectors):
                sectors.append(
                    Sector(
                        i * sector_width, j * sector_height, sector_width, sector_height
                    )
                )
        return sectors

    def _create_grid(self):
        return [[None for _ in range(self.width)] for _ in range(self.height)]

    def update_environment(self):
        self.seasonal_cycle()
        self.dynamic_environmental_changes()

    def seasonal_cycle(self):
        # Implement seasonal changes affecting temperature, light levels, and rainfall
        self.season_cycle = (self.season_cycle + 1) % 4
        for sector in self.sectors:
            sector.update_season(self.season_cycle)

    def dynamic_environmental_changes(self):
        # Introduce random weather events and their effects
        for sector in self.sectors:
            if random.random() < 0.1:  # 10% chance of random event
                sector.random_event()

    def distribute_sunlight(self):
        # Method to simulate sunlight exposure in each sector
        for sector in self.sectors:
            sector.update_sunlight()

    def accumulate_organic_matter(self):
        # Method to handle organic matter accumulation and toxicity
        for sector in self.sectors:
            sector.update_organic_matter()
