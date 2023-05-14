""" 
This module creates numbers for given variable type of inputs
"""

from typing import Optional


def convert_string_to_int(string: str, *, base: Optional[int] = 256) -> int:
    """
    Converts a string to an deterministicly random integer representation using the specified base.

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

def convert_string_to_float(string: str) -> float:
    """
    Converts a string to a deterministic random float representation between 0 and 1.

    Works better for texts longer than 5 letters.

    Args:
        string (str): The input string to be converted to a float.

    Returns:
        float: The float representation of the input string between 0 and 1.

    Example:
        >>> convert_string_to_float("Hello, World")  
        0.3350260018341942
        >>> convert_string_to_float("Hi, World?")     
        0.8893743173684925
        >>> convert_string_to_float("Hi, World")  
        0.03764671504177386
    """
    total_forward = sum(
        ord(letter) * index * index for index, letter in enumerate(string)
    )
    total_reverse = sum(
        ord(letter) * index * index
        for index, letter in enumerate(string[::-1], start=1)
    )

    frac = (total_reverse + 1) / (total_forward + 1)
    total = ((total_reverse + total_forward) * frac) % 1

    return total
