def format_price(price):
    price = int(price)
    result = f'Цена: {price} руб.'
    return result

price = 56.24
result = format_price(price)
print(result)