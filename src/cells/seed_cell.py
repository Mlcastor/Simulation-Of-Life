# src/cells/seed_cell.py

from src.cells.base_cell import BaseCell


class SeedCell(BaseCell):
    """
    The SeedCell class represents a dormant brain cell type that consumes very little energy. It is
    connected to a ConduitCell and becomes a BrainCell when the ConduitCell dies.
    """

    def __init__(
        self, position: tuple[int, int], energy: float, genome: list[int], conduit_cell
    ):
        """
        Initialize a new SeedCell.

        Args:
            position (tuple[int, int]): The (x, y) position of the cell on the grid.
            energy (float): The initial energy level of the cell.
            genome (list[int]): The genome structure represented by a list of integers.
            conduit_cell: A reference to the associated ConduitCell.
        """
        super().__init__(position, energy)
        self.genome = genome
        self.conduit_cell = conduit_cell

    def initialize_genome(self) -> list[int]:
        """
        Initialize the genome of the SeedCell.

        Returns:
            list[int]: The genome structure represented by a list of integers.
        """
        # Returning the genome passed on from the BrainCell parent
        return self.genome

    def perform_action(self) -> None:
        """
        Perform the SeedCell's specific action based on its state.

        Checks the state of the associated ConduitCell.
        If the ConduitCell is dead, transitions this SeedCell to a BrainCell.
        Consumes a minimal amount of energy.
        """
        # Check if the connected ConduitCell is dead
        if not self.conduit_cell.alive:
            self.become_brain_cell()

        # Minimal energy consumption
        self.consume_energy(0.1)

    def become_brain_cell(self) -> None:
        """
        Transition the SeedCell to a BrainCell.
        """
        # Implement the logic for transforming this cell into a BrainCell.
        # Assuming there is a BrainCell class that we can import and use.
        from .brain_cell import BrainCell

        new_brain_cell = BrainCell(self.position, self.energy, self.genome)
        # Additional logic might be required to replace this cell in the grid structure

    def info(self) -> dict:
        """
        Return the current state information of the SeedCell.

        Returns:
            dict: A dictionary containing the cell's position, energy, genome, and conduit_cell state.
        """
        info = super().info()
        info.update({"conduit_cell_alive": self.conduit_cell.alive})
        return info
