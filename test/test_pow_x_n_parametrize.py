import pytest
import math
from pow_x_n import power


# Test cases for pytest parametrization are stored as tuples,
# where the variables are defined in the @pytest.mark.parametrize(**args) decorator.
test_cases = [(1, 0, 1), (2, 8, 256)]


# In pytest we can parametrize inputs, which enables running many tests with the same code.
@pytest.mark.parametrize("x, n, expected", test_cases)
def test_fast_power(x, n, expected):
    assert power(x, n) == expected
