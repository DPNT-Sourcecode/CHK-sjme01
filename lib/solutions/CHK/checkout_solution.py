import string

from lib.solutions.CHK.supermarket import SupermarketCheckout


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
    supercheckout = SupermarketCheckout()

    total_price = 0
    items = skus.split(",")
    for item in items:
        if len(item) > 1:
            item = item.strip()
            item_name = item[-1]
            item_count = int(item[:-1])
        else:
            item_name = item
            item_count = 1

        price = supercheckout.calculate_item_price(item_name, item_count)

        if price == -1:
            print("Invalid input")
            break
        total_price += price
    return total_price



