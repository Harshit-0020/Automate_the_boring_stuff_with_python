def strong_password_checker(password):
    import re
    strong_password = True

    # Regex for upper-case characters.
    upper_regex = re.compile(r'[A-Z]')
    # Regex for lower-case characters.
    lower_regex = re.compile(r'[a-z]')
    #Regex for numeric characters.
    numeric_regex = re.compile(r'[0-9]')

    if len(password) < 8:                       # length of password greater than 8 characters.
        strong_password = False
    if not upper_regex.findall(password):       # if the password contains atleast 1 upper character.
        strong_password = False
    if not lower_regex.findall(password):       # if the password contains atleast one lower character.
        strong_password = False
    if not numeric_regex.findall(password):     # if the password contains atleast one numeric character.
        strong_password = False

    if strong_password:
        print('Password is strong.')
    else:
        print('Weak Password, please try a new password.')


