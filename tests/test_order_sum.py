import unittest

def order_total(items):
    """Сумма заказа: сумма цена * количество."""
    return sum(price * qty for price, qty in items)

class OrderTotalTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(order_total([(350, 2), (120, 1)]), 820)

if __name__ == "__main__":
    unittest.main()
