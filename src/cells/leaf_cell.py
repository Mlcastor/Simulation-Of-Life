# src/cells/leaf_cell.py

from src.cells.base_cell import BaseCell
from src.cells.conduit_cell import ConduitCell


class LeafCell(BaseCell):
    """
    The LeafCell class represents a cell type that performs photosynthesis to generate energy,
    which is then transferred to a connected conduit cell.
    """

    def __init__(self, position: tuple[int, int], energy: float):
        """
        Initialize the leaf cell with position and energy.
        """
        super().__init__(position, energy)
        self.connected_conduit: ConduitCell | None = None

    def perform_action(self) -> None:
        """
        Perform the leaf cell's action, which includes generating energy and
        transferring it to the connected conduit cell.
        """
        if self.connected_conduit is None:
            self.on_death()
            return

        # Generate energy based on sunlight
        energy_generated = self.generate_energy()

        # Transfer the generated energy to the connected conduit cell
        self.connected_conduit.receive_energy(energy_generated)

    def generate_energy(self) -> float:
        """
        Generate energy based on the amount of sunlight in the current position.

        Returns:
            float: Amount of energy generated.
        """
        sunlight_intensity = self.get_sunlight_intensity()
        energy_generated = sunlight_intensity * 10.0  # Example calculation
        return energy_generated

    def get_sunlight_intensity(self) -> float:
        """
        Get the intensity of sunlight at the current position.

        Returns:
            float: The intensity of sunlight.
        """
        # Implement the logic to get the sunlight intensity at the current position
        sunlight_intensity = 0.8  # Example value for demonstration
        return sunlight_intensity

    def connect_to_conduit(self, conduit_cell: ConduitCell) -> None:
        """
        Connect the leaf cell to a conduit cell.

        Args:
            conduit_cell (ConduitCell): The conduit cell to connect to.
        """
        self.connected_conduit = conduit_cell

    def check_conduit(self) -> None:
        """
        Disconnect the leaf cell from the conduit cell.
        """
        if self.connected_conduit == None:
            self.on_death()

    def on_death(self) -> None:
        """
        Handle the actions to be performed when the leaf cell dies.
        """
        self.release_organic_matter()
        self.release_energy()

    def release_organic_matter(self) -> None:
        """
        Release organic matter into the soil at the leaf cell's position.
        """
        # Implement the logic to release organic matter into the soil
        pass

    def release_energy(self) -> None:
        """
        Release the leaf cell's remaining energy into the soil at its position.
        """
        # Implement the logic to release energy into the soil
        pass
