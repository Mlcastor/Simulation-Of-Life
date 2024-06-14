# src/cells/root_cell.py

from src.cells.base_cell import BaseCell
from src.cells.conduit_cell import ConduitCell


class RootCell(BaseCell):
    """
    The RootCell class represents a cell type that generates energy by transforming
    soil's organic matter, and transfers the generated energy to a connected conduit cell.
    """

    def __init__(self, position: tuple[int, int], energy: float):
        """
        Initialize the root cell with position and energy.

        Args:
            position (tuple[int, int]): The (x, y) position of the cell on the grid.
            energy (float): The initial energy level of the cell.
        """
        super().__init__(position, energy)
        self.connected_conduit: ConduitCell | None = None

    def initialize_genome(self) -> list:
        """
        Initialize the genome of the root cell. Root cells do not need a genome.

        Returns:
            list: An empty genome list as it's not applicable for root cells.
        """
        return []

    def perform_action(self) -> None:
        """
        Perform the root cell's action, which includes generating energy from
        the soil's organic matter and transferring it to the connected conduit cell.
        """
        if self.connected_conduit is None:
            self.on_death()
            return

        # Generate energy from soil's organic matter
        energy_generated = self.generate_energy()

        # Transfer the generated energy to the connected conduit cell
        self.connected_conduit.receive_energy(energy_generated)

    def generate_energy(self) -> float:
        """
        Generate energy by transforming the soil's organic matter.

        Returns:
            float: Amount of energy generated.
        """
        organic_matter_concentration = self.get_organic_matter_concentration()
        energy_generated = organic_matter_concentration * 5.0  # Example calculation
        return energy_generated

    def get_organic_matter_concentration(self) -> float:
        """
        Get the concentration of organic matter in the soil at the current position.

        Returns:
            float: The concentration of organic matter.
        """
        # Implement the logic to get the organic matter concentration at the current position
        organic_matter_concentration = 0.7  # Example value for demonstration
        return organic_matter_concentration

    def check_conduit(self) -> None:
        """
        Disconnect the root cell from the conduit cell.
        """
        if self.connected_conduit == None:
            self.on_death()

    def on_death(self) -> None:
        """
        Handle the actions to be performed when the root cell dies.
        """
        self.release_organic_matter()
        self.release_energy()
        self.energy = 0  # Ensure the cell energy is set to zero

    def release_organic_matter(self) -> None:
        """
        Release organic matter into the soil at the root cell's position.
        """
        # Implement the logic to release organic matter into the soil
        # For example, increase the organic matter concentration at this position
        pass

    def release_energy(self) -> None:
        """
        Release the root cell's remaining energy into the soil at its position.
        """
        # Implement the logic to release energy into the soil
        # For example, increase the energy level at this position in the soil
        pass
