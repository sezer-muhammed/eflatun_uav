"""Filter implementations for moving objects
"""

from typing import List

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
        