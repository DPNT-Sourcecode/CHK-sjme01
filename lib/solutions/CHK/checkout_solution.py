def calculate_item_price(item, count):
    pricing_table = {
        "A": 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
    }

    special_offers = {
        'A': [(3, 130), (5, 200)],
        'B': [(2, 45)],
        'H': [(5, 45), (10, 80)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(2, 90), (3, 130)]

    }
    price = 0
    if item not in special_offers and item not in pricing_table:
        return -1

    # if count < 3 and item in special_offers:
    #     return count * pricing_table[item]

    if count >= 1 and item not in special_offers:
        return count * pricing_table[item]

    if item == "A" and count == 5 or count == 3:
        for quantity, offer_price in special_offers[item]:
            if count == quantity:
                return offer_price

    if item == "A" and count > 5:
        if count > 5:
            offer_multiplier = count // 5
            remaining_items = count % 5
            if remaining_items < 3:
                return offer_multiplier * 200 + remaining_items * pricing_table["A"]
            elif remaining_items == 3:
                return offer_multiplier * 200 + 130
            elif remaining_items == 4:
                offer_multiplier2 = remaining_items // 3
                remaining_items2 = remaining_items % 3
                return offer_multiplier * 200 + offer_multiplier2 * 130 + remaining_items2 * pricing_table["A"]

    if item == "A" and 3 < count < 4:
        for quantity, offer_price in special_offers[item]:
            if count > quantity == 3:
                offer_multiplier = count // 3
                remaining_items = count % 3
                return offer_multiplier * 130 + remaining_items * pricing_table[item]

    if item in special_offers:
        for quantity, offer_price in special_offers[item]:
            mins = special_offers[item][0][0]
            maxs = special_offers[item][1][0]

            

            if count > quantity:
                offer_multiplier = count // quantity
                remaining_items = count % quantity
                return offer_multiplier * offer_price + remaining_items * pricing_table[item]
            elif count == quantity:
                return offer_price

    return count * pricing_table[item]


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
    total_price = 0

    if len(skus) == 0:
        return 0

    if len(skus) == 1 and not "A" <= skus <= "Z":
        return -1

    if len(skus) > 1 and skus.isupper():

        items = set(skus)
        for item in items:
            item_count = skus.count(item)
            if item == "E" and item_count in [2, 3, 4] and len(skus) > 2:
                discount = 30 if item_count == 2 or item_count == 3 else 45
                price = calculate_item_price(item, item_count) - discount
            elif item == "B" and item_count in [2] and skus.count("E") == 2:
                discount = 30
                price = 2 * discount
            elif item == "F" and item_count in [3, 4, 5, 6]:
                discount = 10 if item_count in [3, 4] else 20
                price = calculate_item_price(item, item_count) - discount
            else:
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
