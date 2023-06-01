import string

from lib.solutions.CHK.supermarket import SupermarketCheckout


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
    supercheckout = SupermarketCheckout()
    supercheckout.set_price('A', 50)
    supercheckout.set_price('B', 30)
    supercheckout.set_price('C', 20)
    supercheckout.set_price('D', 15)
    supercheckout.set_special_offer('A', 3, 130)
    supercheckout.set_special_offer('B', 2, 45)

    if len(skus) == 0:
        return -1

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
