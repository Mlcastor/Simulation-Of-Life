# src/core/environment.py
import random

from src.core.world import World
from src.core.sector import Sector


class Environment:
    """
    Represents the environment of the simulation, including ecological niches and weather events.
    """

    def __init__(self, world: World):
        """
        Initializes the Environment with a reference to the World instance.

        Args:
            world (World): The world in which the environment exists.
        """
        self.world = world
        self.ecological_niches = {}
        self.weather_events = {}

    def define_ecological_niches(self):
        """
        Define different ecological niches and their characteristics.
        """
        self.ecological_niches["forest"] = {
            "sunlight_exposure": 50,
            "organic_matter": 80,
            "temperature_range": (10, 20),
            "rainfall_range": (10, 20),
        }

        self.ecological_niches["plains"] = {
            "sunlight_exposure": 90,
            "organic_matter": 40,
            "temperature_range": (15, 30),
            "rainfall_range": (5, 15),
        }

        # Additional ecological niches can be added here

    def handle_weather_events(self):
        """
        Simulate weather events and their impact on the environment.
        """
        for sector in self.world.sectors:
            if random.random() < 0.1:  # 10% chance of a weather event
                event_type = random.choice(["storm", "drought", "heatwave"])
                self.apply_weather_event(sector, event_type)

    def apply_weather_event(self, sector: Sector, event_type: str):
        """
        Apply the effects of a weather event on the given sector.

        Args:
            sector (Sector): The sector affected by the weather event.
            event_type (str): The type of weather event ('storm', 'drought', 'heatwave').
        """
        if event_type == "storm":
            sector.rainfall += 20
            sector.sunlight_exposure -= 10
        elif event_type == "drought":
            sector.rainfall -= 20
            sector.temperature += 5
        elif event_type == "heatwave":
            sector.temperature += 10
            sector.sunlight_exposure += 5

    def update_environment(self):
        """
        Update the environment by handling weather events and communicating with the World and Sector classes.
        """
        self.handle_weather_events()
        self.world.distribute_sunlight()
        self.world.accumulate_organic_matter()
        # Possibly more methods interacting with the World and Sector classes
