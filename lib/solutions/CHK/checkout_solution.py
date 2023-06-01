def calculate_item_price(item, count):
    pricing_table = {
        "A": 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40

    }

    special_offers = {
        'A': [(3, 130), (5, 200)],
        'B': [(2, 45)],
        'E': [(2, 'B')]
    }
    price = 0
    if item not in special_offers and item not in pricing_table:
        return -1

    if count < 3 and item in special_offers:
        return count * pricing_table[item]

    if count >= 1 and item not in special_offers:
        return count * pricing_table[item]

    if item in special_offers:
        for quantity, offer_price in special_offers[item]:
            if item == "E" and offer_price.isalpha():
                free_item = offer_price
                return pricing_table[item] * count + pricing_table[free_item]
            elif count > quantity == 5 and item == "A":
                offer_multiplier = count // quantity == 5
                remaining_items = count % quantity == 5
                return offer_multiplier * offer_price + remaining_items * pricing_table[item]
            elif count > quantity == 3 and count < quantity == 5 and item == "A":
                offer_multiplier = count // quantity == 3
                remaining_items = count % quantity == 3
                return offer_multiplier * offer_price + remaining_items * pricing_table[item]
            elif count == quantity == 3 and item == "A":
                return offer_price
            elif count == quantity == 5 and item == "A":
                return offer_price
            elif count == quantity:
                return offer_price
            else:
                return count * pricing_table[item]

    return count * pricing_table[item]


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
    total_price = 0

    if len(skus) == 0:
        return 0

    if len(skus) == 1 and skus not in "ABCDE":
        return -1

    if len(skus) > 1 and skus.isupper():

        items = set(skus)
        for item in items:
            item_count = skus.count(item)
            price = calculate_item_price(item, item_count)
            total_price += price
    elif len(skus) == 1:
        item_name = skus
        item_count = 1
        price = calculate_item_price(item_name, item_count)
        total_price += price
    else:
        return -1
    return total_price







