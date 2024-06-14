# src/cells/base_cell.py

from abc import ABC, abstractmethod

import random


class BaseCell(ABC):
    """
    The BaseCell class is the abstract class from which all other cell types in the simulation inherit.
    It defines the common interface and behavior for all cells.
    """

    def __init__(self, position: tuple[int, int], energy: float):
        """
        Initialize a new cell.

        Args:
            position (tuple[int, int]): The (x, y) position of the cell on the grid.
            energy (float): The initial energy level of the cell.
        """
        self.position = position
        self.energy = energy
        self.genome = self.initialize_genome()

    @abstractmethod
    def initialize_genome(self) -> list:
        """
        Initialize the genome of the cell.

        Returns:
            list: The genome structure represented by a list of integers.
        """
        pass

    @abstractmethod
    def perform_action(self) -> None:
        """
        Perform the cell's specific action based on its type and state.
        """
        pass

    def move(self, new_position: tuple[int, int]) -> None:
        """
        Move the cell to a new position.

        Args:
            new_position (tuple[int, int]): The new (x, y) position of the cell.
        """
        self.position = new_position

    def consume_energy(self, amount: float) -> None:
        """
        Consume a specified amount of energy.

        Args:
            amount (float): The amount of energy to be consumed.
        """
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0  # Ensure energy does not drop below zero

    def add_energy(self, amount: float) -> None:
        """
        Add a specified amount of energy.

        Args:
            amount (float): The amount of energy to be added.
        """
        self.energy += amount

    def mutate(self) -> None:
        """
        Mutate the cell's genome to simulate genetic evolution.
        """
        # Simple mutation logic; can be replaced with more complex mechanisms
        for i in range(len(self.genome)):
            if random.random() < 0.01:  # 1% chance to mutate each genome element
                self.genome[i] = random.randint(0, 255)

    def info(self) -> dict:
        """
        Return the current state information of the cell.

        Returns:
            dict: A dictionary containing the cell's position, energy, and genome.
        """
        return {
            "position": self.position,
            "energy": self.energy,
            "genome": self.genome,
        }
