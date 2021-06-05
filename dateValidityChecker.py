# Enter the date in DD/MM/YYYY format:
def date_validity_checker(text):
    import re
    date_regex = re.compile(r'^([0-3][0-9])/([0-1][1-9])/([1-2][0-9][0-9][0-9])')
    mo = date_regex.search(text)
    month = mo.group(2)
    day = mo.group(1)
    year = mo.group(3)
    if month[0] == '0':
        month = month[1]
    if day[0] == '0':
        day = day[1]

    if int(year) % 4 == 0 and int(year) % 100 != 0:
        leap_year = True
    elif int(year) % 400 == 0:
        leap_year = True
    else:
        leap_year = False

    if leap_year:
        feb_max = 29
    else:
        feb_max = 28

    days_corresponding_to_months = {
        '1': 31,
        '2': feb_max,
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }
    if int(day) <= days_corresponding_to_months[month]:
        print('Entered date is valid')
    else:
        print('Entered date is invalid.')
