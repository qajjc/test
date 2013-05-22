__author__ = 'thinkpad'

import CartInterface

class MissCart(CartInterface):
    def __init__(self):
        pass

    def count_products(self):
        print "miss cart count products"

    def get_product_amount(self):
        print "miss cart get product amount"

    def add_product_to_cart(self):
        print "miss cart add product to cat"
