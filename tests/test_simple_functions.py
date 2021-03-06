import pytest

from simple_functions import my_sum, factorial


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (2, 2),
        (4, 24)
    ])
    def test_factorial(self, number, expected):
        '''Test factorial function'''
        result = factorial(number)
        assert result == expected
