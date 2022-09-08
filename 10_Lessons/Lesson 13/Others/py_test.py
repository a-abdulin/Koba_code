import pytest

from utils import ticket_price

set_parameters = [(0, "Бесплатно"), (1, "Бесплатно"), (7, "100 рублей"), (18, "200 рублей"),
                  (25, "300 рублей"), (0.5, "Бесплатно"), (60, "Бесплатно"), (-1, "Ошибка")]


@pytest.mark.parametrize("first, expected", set_parameters)
def test_multiply(first, expected):
    assert ticket_price(first) == expected
