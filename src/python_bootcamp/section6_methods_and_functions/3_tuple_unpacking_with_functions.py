stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]


def most_price_check(stock_prices):
    current_max = 0
    name = ''

    for company, price in stock_prices:
        if price > current_max:
            current_max = price
            name = company
        else:
            pass

    return name, current_max


item = most_price_check(stock_prices)
print(item)  # ('GOOG', 400)
