import pytest
from eflatun_uav.helpers.number_generators import convert_string_to_int, convert_string_to_float


@pytest.mark.parametrize(
    "input_string,base",
    [
        ("", 256),
        ("abcde", 256),
        ("a" * 20, 16),
    ],
)
def test_convert_string_to_int(input_string, base):
    result = convert_string_to_int(input_string, base=base)
    assert isinstance(result, int)
    assert 0 <= result < base


def test_convert_string_to_int_variance():
    result_a = convert_string_to_int("Şevvala")
    result_b = convert_string_to_int("Şevvalb")
    assert abs(result_a - result_b) >= 10

@pytest.mark.parametrize(
    "input_string",
    [
        "",
        "abcde",
        "a" * 20,
    ],
)
def test_convert_string_to_float(input_string):
    result = convert_string_to_float(input_string)
    assert isinstance(result, float)
    assert 0 <= result <= 1

@pytest.mark.parametrize(
    "input_string",
    [
        "a",
        "a" * 100,
    ],
)
def test_convert_string_to_float_bounds(input_string):
    result = convert_string_to_float(input_string)
    assert 0 <= result <= 1

def test_convert_string_to_float_difference():
    result_a = convert_string_to_float("aaaab")
    result_b = convert_string_to_float("aaaaa")
    assert abs(result_a - result_b) >= 0.1