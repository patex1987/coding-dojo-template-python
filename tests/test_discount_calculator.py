import pytest
import discount_calculator


def test_insert_no_input():
    """
    Test case - no input
    """
    assert discount_calculator.calculate_price() == 0


def test_no_discount():
    """
    Test case - without discount
    """
    assert discount_calculator.calculate_price(book1_count=1) == 8
    assert discount_calculator.calculate_price(book2_count=1) == 8

def test_first_discount():
    """
    Test case 
    """