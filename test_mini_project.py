#import pytest
from mini_project import produce_pretty_list

def test_produce_pretty_list_with_products():
    mock_product_list = [
    {"name": "Black tea", "price": "1.50"},
    {"name": "Americano", "price": "1.80"},
    {"name": "Strawberry smoothie", "price": "1.20"},
    {"name": "Avacado sandwich", "price": "0.90"},
    ]
    # Arrange
    expected = """Index: 0 Details: {'name': 'Black tea', 'price': '1.50'}\nIndex: 1 Details: {'name': 'Americano', 'price': '1.80'}\nIndex: 2 Details: {'name': 'Strawberry smoothie', 'price': '1.20'}\nIndex: 3 Details: {'name': 'Avacado sandwich', 'price': '0.90'}\n"""
    # Act
    actual = produce_pretty_list(mock_product_list)
    # Assert
    assert actual == expected

def test_produce_pretty_list_with_no_products():
    mock_product_list = []
    # Arrange
    expected = """"""
    # Act
    actual = produce_pretty_list(mock_product_list)
    # Assert
    assert actual == expected