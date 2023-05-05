""" 
This module creates numbers for given variable type of inputs
"""

from typing import Optional


def convert_string_to_int(string: str, *, base: Optional[int] = 256) -> int:
    """
    Converts a string to an deterministicly random integer representation using the specified base.

    This function calculates two totals, one for the forward direction of the string
    and another for the reverse direction. The final result is the sum of both totals
    modulo the given base.

    Works better for texts longer than 5 letters.

    Args:
        string (str): The input string to be converted to an integer.
        base (Optional[int], optional): The base to be used for the conversion. Defaults to 256.

    Raises:
        ValueError: If the base is not an integer or if it is 0, -1, or 1.

    Returns:
        int: The integer representation of the input string.

    Example:
        >>> convert_string_to_int("Hello, World!")
        157
        >>> convert_string_to_int("Hello, World")
        84
        >>> convert_string_to_int("Hello, World!", base = 36)
        13
    """
    if base is not None and not isinstance(base, int):
        raise ValueError(f"Base must be an integer, not {type(base)}")
    if base in [0, 1, -1]:
        raise ValueError("Base cannot be 0, -1 or 1")

    total_forward = sum(
        ord(letter) * index * index for index, letter in enumerate(string)
    )
    total_reverse = sum(
        ord(letter) * index * index
        for index, letter in enumerate(string[::-1], start=1)
    )

    return int((total_reverse + total_forward) % base)

class TesterClass:
    """
    This is a summary for the TesterClass.
    """

    def __init__(self) -> None:
        """
        Initialize the TesterClass instance.
        """
        pass

    def tester__(self, adam: int, kadin: float) -> str:
        """
        This is a summary for the tester__ method.

        Args:
            adam (int): A description for the 'adam' parameter.
            kadin (float): A description for the 'kadin' parameter.

        Returns:
            str: A description for the return value.
        """
        return "asd"