"""Filter implementations for moving objects
"""

from typing import List
import numpy as np

class BaseFilter():
    """Base Filter object for Filter module
    """

    def __init__(self, input_size:List, output_size:List) -> None:
        """_summary_

        Args:
            input_size (List): _description_
            output_size (List): _description_
        """
        self.input_size = input_size
        self.output_size = output_size

    def update(self, input_state: np.ndarray):
        """_summary_

        Args:
            input_state (np.ndarray): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError("This is base class, please refer the main classes")

    def predict(self) -> np.ndarray:
        """_summary_

        Raises:
            NotImplementedError: _description_

        Returns:
            np.ndarray: _description_
        """
        raise NotImplementedError("This is base class, please refer the main classes")
