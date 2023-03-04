class ShoppingCart:
    'Add goods to shopping cart'
    def __init__(self):
        self.items = {}

    def  __getitem__(self, item):
        if item in self.items:
            return self.items[item]
        return 0

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        if key not in self.items:
            raise ValueError (f'{key} not in goodslist delitem')
        else:
            del self.items[key]

    def add_item(self, item, value=1):
        if item in self.items:
            self.items[item] += value
        else:
            self.items[item] = value

    def remove_item(self, item, value=1):
        if item not in self.items:
            pass
            # raise ValueError (f'{item} not in googslist')
        elif value >= self.items[item]:
            del self.items[item]
        else:
            self.items[item] -= value

if __name__ == '__main__':
    cart = ShoppingCart()

    # Add some items to the cart
    cart.add_item('Apple', 3)
    cart.add_item('Banana', 2)
    cart.add_item('Orange')

    assert cart['Banana'] == 2
    assert cart['Orange'] == 1
    assert cart['Kivi'] == 0

    cart.add_item('Orange', 9)
    assert cart['Orange'] == 10

    print("Shopping Cart:")
    for item_name in cart.items:
        print(f"{item_name}: {cart[item_name]}")

    cart['Apple'] = 5
    cart['Banana'] = 7
    cart['Kivi'] = 11
    assert cart['Apple'] == 5
    assert cart['Banana'] == 7
    assert cart['Kivi'] == 11

    print("Updated Shopping Cart:")
    for item_name in cart.items:
        print(f"{item_name}: {cart[item_name]}")

    # Remove an item from the cart
    cart.remove_item('Banana')
    assert cart['Banana'] == 6

    cart.remove_item('Apple', 4)
    assert cart['Apple'] == 1

    cart.remove_item('Apple', 2)
    assert cart['Apple'] == 0
    assert 'Apple' not in cart.items

    # cart.remove_item('Potato')

    del cart['Banana']
    assert cart['Banana'] == 0
    print('')
    assert 'Banana' not in cart.items

    print("Updated Shopping Cart:")
    for item_name in cart.items:
        print(f"{item_name}: {cart[item_name]}")