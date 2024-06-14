# src/dynamics/energy.py
from typing import Dict, List

from src.cells.base_cell import BaseCell
from src.core.sector import Sector
from src.core.world import World
from src.cells.leaf_cell import LeafCell


class EnergyManager:
    """
    Manages the energy dynamics of the simulation, including energy sources, budgets, and allocation.
    """

    def __init__(self, cell_types: Dict[str, type]):
        """
        Initializes the EnergyManager with the available cell types.

        Args:
            cell_types (Dict[str, type]): A dictionary mapping cell type names to their respective classes.
        """
        self.cell_types = cell_types
        self.energy_sources = {
            "sunlight": self.get_sunlight_energy,
            "organic_matter": self.get_organic_matter_energy,
            "cell_consumption": self.get_cell_consumption_energy,
        }

    def get_sunlight_energy(self, leaf_cell: LeafCell, sector: Sector) -> float:
        """
        Calculates the energy obtained from sunlight for the given cell and sector.

        Args:
            cell (BaseCell): The cell object.
            sector (Sector): The sector in which the cell is located.

        Returns:
            float: The amount of energy obtained from sunlight.
        """
        sunlight_exposure = sector.sunlight_exposure
        photosynthesis_efficiency = leaf_cell.generate_energy
        return sunlight_exposure * photosynthesis_efficiency

    def get_organic_matter_energy(self, cell, sector) -> float:
        """
        Calculates the energy obtained from organic matter for the given cell and sector.

        Args:
            cell (BaseCell): The cell object.
            sector (Sector): The sector in which the cell is located.

        Returns:
            float: The amount of energy obtained from organic matter.
        """
        organic_matter = sector.organic_matter
        nutrient_absorption_efficiency = cell.nutrient_absorption_efficiency
        return organic_matter * nutrient_absorption_efficiency

    def get_cell_consumption_energy(self, cell, target_cell) -> float:
        """
        Calculates the energy obtained from consuming the target cell.

        Args:
            cell (BaseCell): The cell object consuming the target cell.
            target_cell (BaseCell): The cell being consumed.

        Returns:
            float: The amount of energy obtained from consuming the target cell.
        """
        return target_cell.energy_content * cell.consumption_efficiency

    def allocate_energy(self, cell, sector):
        """
        Allocates energy to the given cell based on its needs and the available energy sources.

        Args:
            cell (BaseCell): The cell object to allocate energy to.
            sector (Sector): The sector in which the cell is located.

        Returns:
            float: The amount of energy allocated to the cell.
        """
        total_energy = 0
        for source, get_energy_func in self.energy_sources.items():
            if source != "cell_consumption":
                total_energy += get_energy_func(cell, sector)

        # Implement dynamic resource allocation logic here
        cell.energy_level = total_energy
        return total_energy

    def update_energy_distribution(self, world):
        """
        Updates the energy distribution across the simulation.

        Args:
            world (World): The world object containing the sectors and cells.
        """
        for sector in world.sectors:
            for cell in sector.cells:
                self.allocate_energy(cell, sector)
