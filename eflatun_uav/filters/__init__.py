"""Filter implementations for moving objects
"""

from typing import List
import numpy as np


class BaseFilter:
    """A base class representing a generic filter for moving objects.

    This class serves as a foundation for more specific filter implementations. It is designed to be
    subclassed, and does not provide a full implementation that can be used on its own.
    """

    def __init__(self, input_size: List, output_size: List) -> None:
        """Initializes the base filter with the given input and output size.

        Args:
            input_size (List): The size of the input state. This is usually a list where each element represents
                               the size of a different aspect of the input state.
            output_size (List): The size of the output state. Similar to the input size, this is a list where each
                                element represents the size of a different aspect of the output state.
        """
        self.input_size = input_size
        self.output_size = output_size

    def update(self, input_state: np.ndarray):
        """Updates the state of the filter based on the given input state.

        This method is intended to be overridden by subclasses.

        Args:
            input_state (np.ndarray): The input state used to update the filter. The size and structure of this
                                      input should match the input_size specified when the filter was initialized.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.
        """
        raise NotImplementedError("This is base class, please refer the main classes")

    def predict(self) -> np.ndarray:
        """Predicts the next state based on the current state of the filter.

        This method is intended to be overridden by subclasses.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.

        Returns:
            np.ndarray: The predicted next state. The size and structure of this output should match the output_size
                        specified when the filter was initialized.
        """
        raise NotImplementedError("This is base class, please refer the main classes")
