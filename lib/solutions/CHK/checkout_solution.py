
class SupermarketCheckout:
    def __int__(self):
        self.pricing_table = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15

        }
        self.special_offers = {
            'A': (3, 150),
            'B': (2, 45)
        }

    def set_price(self, item, price):
        self.pricing_table[item] = price

    def set_special_offer(self, item, quantity, offer_price):
        self.special_offers[item] = (quantity, offer_price)

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
    # supercheckout.set_price('A', 50)
    # supercheckout.set_price('B', 30)
    # supercheckout.set_price('C', 20)
    # supercheckout.set_price('D', 15)
    # supercheckout.set_special_offer('A', 3, 130)
    # supercheckout.set_special_offer('B', 2, 45)

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


