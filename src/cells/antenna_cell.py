# src/cells/antenna_cell.py

from src.cells.base_cell import BaseCell
from src.cells.conduit_cell import ConduitCell
import random


class AntennaCell(BaseCell):
    """
    The AntennaCell class represents a cell type that either gathers energy
    or handles communication, depending on its current mode.
    """

    def __init__(self, position: tuple[int, int], energy: float):
        super().__init__(position, energy)
        self.mode: str = "energy_gatherer"  # Initial mode
        self.connected_conduit: ConduitCell | None = (
            None  # Reference to connected conduit cell
        )
        self.radio_frequency: float = random.uniform(
            0.1, 10.0
        )  # Random radio frequency

    def perform_action(self) -> None:
        """Perform the cell's action based on its current mode."""
        if self.connected_conduit is None:
            self.on_death()
            return

        if self.mode == "energy_gatherer":
            self.gather_energy()
        elif self.mode == "communication_handler":
            self.handle_communication()

    def gather_energy(self) -> None:
        """Gather residual energy from the soil and send it to the connected conduit cell."""
        # Example mechanism to gather energy from the soil
        energy_gathered: float = 10.0  # This value may be determined by other factors
        self.add_energy(energy_gathered)

        # Send the gathered energy to the connected conduit cell
        if self.connected_conduit:
            self.connected_conduit.receive_energy(energy_gathered)

    def handle_communication(self) -> None:
        """Handle communication using the cell's radio frequency."""
        # Placeholder for communication logic
        pass

    def gather_mode(self, conduit_cell: ConduitCell) -> None:
        """
        Connect to a conduit cell.

        Args:
            conduit_cell (ConduitCell): The conduit cell to connect to.
        """
        self.connected_conduit = conduit_cell
        self.mode = "energy_gatherer"  # Switch to "energy gatherer" mode initially

    def communicate_mode(self, conduit_cell: ConduitCell) -> None:
        """Disconnect from the conduit cell."""
        self.connected_conduit = conduit_cell
        self.mode = "communication_handler"  # Switch to "communication handler" mode

    def on_death(self) -> None:
        """Handle actions to be performed when the cell dies."""
        self.release_organic_matter()
        self.release_energy()

    def release_organic_matter(self) -> None:
        """Release organic matter into the soil at the cell's position."""
        # Placeholder for releasing organic matter logic
        pass

    def release_energy(self) -> None:
        """Release the cell's remaining energy into the soil at its position."""
        # Placeholder for releasing energy logic
        pass
