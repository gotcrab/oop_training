class Order:
    'Add and delete goods from a list. In the same time create a new order'
    def __init__(self, cart: list, customer: str):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)

    def __radd__(self, other):
        new_cart = self.cart.copy()
        new_cart.insert(0, other)
        return Order(new_cart, self.customer)

    def __sub__(self, other):
        if other in self.cart:
            new_cart = self.cart.copy()
            new_cart.remove(other)
            return Order(new_cart, self.customer)
        return self

    def __rsub__(self, other):
        if other in self.cart:
            new_cart = self.cart.copy()
            new_cart.remove(other)
            return Order(new_cart, self.customer)
        return self




order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')

