import string


class SupermarketCheckout:
    def __int__(self):
        self.pricing_table = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15

        }
        self.special_offers = {
            "A": (3, 130),
            "B": (2, 45)
        }

    def checkout(self, basket):
        item_counts = {}
        total_price = 0

        for item in basket:
            if item not in self.pricing_table:
                return -1

            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

        for item, count in item_counts.items():
            price = self.calculate_item_price(item, count)
            if price == -1:
                return -1
            total_price += price

    def calculate_item_price(self, item, count):
        if item in self.special_offers:
            quantity, offer_price = self.special_offers[item]
            if count >= quantity:
                offer_multiplier = count // quantity
                remaining_items = count % quantity
                return offer_multiplier * offer_price + remaining_items
        return count * self.pricing_table[item]


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
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


