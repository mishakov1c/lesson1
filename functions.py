def get_sum(one, two, delimimer = '&'):
    result = f'{one}{delimimer}{two}'
    return result

result = get_sum("Learn", "python")
print(result.upper())


