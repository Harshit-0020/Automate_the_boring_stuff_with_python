def print_picnic(items_dict, left_width, right_width):
    print('PICNIC TABLE'.center(left_width+right_width, '-'))
    for x, y in items_dict.items():
        print(f"{x.ljust(left_width, '.')}{str(y).rjust(right_width, ' ')}")


picnicItems = {'sandwiches': 4,
               'apples': 12,
               'cups': 4,
               'cookies': 8000}
print_picnic(picnicItems, 12, 5)
print('\n\n')
print_picnic(picnicItems, 20, 6)
