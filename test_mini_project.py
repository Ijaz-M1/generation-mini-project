import pytest
from mini_project import produce_pretty_list

from mini_project import product_list
from mini_project import courier_list

def test_produce_pretty_list_with_products():
    # Arrange
    expected_output = product_list
    # Act
    result = produce_pretty_list(product_list)
    # Assert
    assert result == expected_output

def test_produce_pretty_list_with_couriers():
    # Arrange
    expected_output = courier_list
    # Act
    result = produce_pretty_list(courier_list)
    # Assert
    assert result == expected_output