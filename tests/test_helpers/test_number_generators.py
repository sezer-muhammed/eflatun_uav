import pytest
from eflatun_uav.helpers.number_generators import convert_string_to_int

@pytest.mark.parametrize("input_string,base", [
    ("", 256),
    ("abcde", 256),
    ("a" * 20, 16),
])
def test_convert_string_to_int(input_string, base):
    result = convert_string_to_int(input_string, base=base)
    assert isinstance(result, int)
    assert 0 <= result < base


def test_convert_string_to_int_variance():
    result_a = convert_string_to_int("Şevvala")
    result_b = convert_string_to_int("Şevvalb")
    assert abs(result_a - result_b) >= 10
