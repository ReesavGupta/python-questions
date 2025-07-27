import pytest
from ecommerce_product_management_system_with_property import Product

def test_valid_product():
    p = Product("Samsung TV", 30000, 10, 50, "Electronics")
    assert p.name == "Samsung TV"
    assert p.final_price == 27000.00
    assert p.savings_amount == 3000.00
    assert p.availability_status == "In Stock"
    assert "Samsung TV" in p.product_summary

def test_low_stock():
    p = Product("T-Shirt", 500, 20, 5, "Clothing")
    assert p.availability_status == "Low Stock"

def test_out_of_stock():
    p = Product("Harry Potter", 400, 0, 0, "Books")
    assert p.availability_status == "Out of Stock"

def test_invalid_category():
    with pytest.raises(ValueError):
        Product("Chair", 1500, 10, 100, "Furniture")

def test_invalid_name():
    with pytest.raises(ValueError):
        Product("A", 1000, 10, 5, "Home")

def test_invalid_discount():
    with pytest.raises(ValueError):
        Product("Shoe", 1000, 90, 5, "Sports")

def test_invalid_stock_quantity():
    with pytest.raises(ValueError):
        Product("Bat", 1000, 10, -1, "Sports")

def test_invalid_base_price():
    with pytest.raises(ValueError):
        Product("Ball", -100, 10, 5, "Sports")
