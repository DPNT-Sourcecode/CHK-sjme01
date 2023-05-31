import string

from lib.solutions.CHK.supermarket import SupermarketCheckout


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    supercheckout = SupermarketCheckout()

    total_price = 0
    items = skus.split(",")
    for item in items:
        item = item.strip()
        item_name = item[-1]
        item_count = int(item[:-1])

        price = supercheckout.calculate_item_price(item_name, item_count)

        if price == -1:
            print("Invalid input")
            break
        total_price += price
    return total_price
