def format_price(price):
    price = int(price)
    result = f'Цена: {price} руб.'
    return result

result = format_price(56.24)
print(result)