import pytest
from Product import Product

@pytest.fixture 
def stock():
    stock = Product('Laptop','P-001',60)
    return stock
def test_adjust_stock(stock):
    assert stock.adjust_stock() == 60