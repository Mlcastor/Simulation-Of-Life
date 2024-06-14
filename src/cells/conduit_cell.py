# src/cells/conduit_cell.py

from typing import Tuple, Optional
from src.cells.base_cell import BaseCell
from src.cells.brain_cell import BrainCell


class ConduitCell(BaseCell):
    """
    A ConduitCell is responsible for transmitting energy and signals between cells,
    particularly from peripheral cells to brain cells.
    """

    def __init__(self, position: Tuple[int, int], energy: float):
        """
        Initialize a ConduitCell.

        Args:
            position (tuple[int, int]): The (x, y) position of the cell on the grid.
            energy (float): The initial energy level of the cell.
        """
        super().__init__(position, energy)
        self.connected_brain: Optional[BrainCell] = None
        self.next_conduit: Optional[ConduitCell] = None

    def perform_action(self) -> None:
        """
        Execute the ConduitCell's actions, including receiving and forwarding energy and signals.
        """
        if not self.connected_brain and not self.next_conduit:
            self.on_death()
            return

        self.receive_and_forward()

    def receive_energy(self, amount: float) -> None:
        """
        Receive a specified amount of energy.

        Args:
            amount (float): The amount of energy received.
        """
        self.energy += amount

    def receive_signals(self, signals: dict) -> None:
        """
        Receive signals from the previous cell.

        Args:
            signals (dict): A dictionary of signals.
        """
        # For now, assume signals are simply stored or forwarded
        pass  # Logic for handling received signals would go here

    def receive_and_forward(self) -> None:
        """
        Receive energy and signals and forward them to the next conduit or the brain cell.
        """
        # Forward energy
        energy_amount = min(10, self.energy)  # Example fixed amount to forward
        if self.next_conduit:
            self.next_conduit.receive_energy(energy_amount)
        elif self.connected_brain:
            self.connected_brain.add_energy(energy_amount)

        # Forward signals (assuming we have some signals to forward)
        signals = {}  # Example signals
        if self.next_conduit:
            self.next_conduit.receive_signals(signals)
        elif self.connected_brain:
            self.connected_brain.process_signals(signals)

    def connect_to_brain(self, brain_cell: BrainCell) -> None:
        """
        Connects the ConduitCell to a brain cell.

        Args:
            brain_cell (BrainCell): The brain cell to connect to.
        """
        self.connected_brain = brain_cell

    def connect_to_next_conduit(self, next_conduit: "ConduitCell") -> None:
        """
        Connects this ConduitCell to the next ConduitCell in the chain.

        Args:
            next_conduit (ConduitCell): The next ConduitCell to connect to.
        """
        self.next_conduit = next_conduit

    def move(self, new_position: Tuple[int, int]) -> None:
        """
        Override `move` method to prevent the cell from moving.

        Args:
            new_position (tuple[int, int]): The new (x, y) position.
        """
        pass  # Conduit cells cannot move

    def on_death(self) -> None:
        """
        Actions to perform when the ConduitCell dies.
        """
        self.release_organic_matter()
        self.release_energy()

    def release_organic_matter(self) -> None:
        """
        Release organic matter to the soil at the cell's position.
        """
        # Implementation to release organic matter
        pass

    def release_energy(self) -> None:
        """
        Release the cell's remaining energy to the soil at its position.
        """
        # Implementation to release energy into the soil
        pass
