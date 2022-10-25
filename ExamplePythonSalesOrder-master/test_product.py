from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.ProductRepository import ProductRepository

def test_unit_down_stock():
    product1 = Product(1, "Tomato", 50, 20)
    product_repository = ProductRepository()

    product_repository.append_product(product1)
    product1.down_stock(10)

    assert product1.stock == 10

def test_integration_down_stock():
    
    customer1 = Customer(1, "Jefté")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(1, "Banana", 50, 10)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 5)
    order.add_order_product(order_product1)

    assert product1.stock == 5


def test_integration_process_product():
    customer1 = Customer(1, "Luana")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(1, "Corn", 5, 10)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 5)
    order.add_order_product(order_product1)

    order_product1.process_product(product1, 3)

    assert order_product1.value_item == 15
    assert product1.stock == 2





