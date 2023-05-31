class SupermarketCheckout:
    def __int__(self):
        self.pricing_table = {


        }
        self.special_offers = {

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


