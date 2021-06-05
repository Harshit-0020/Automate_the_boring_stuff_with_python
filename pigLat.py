# English to pig-latin
message = input('Enter the english message to translate to pig-latin: ')

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

piglatin = []  # A list of words in pig-latin
for word in message.split():
    # Separate the non-letters at the start of this word.
    prefixNonLetters = ''
    while len(word) > 0 and not word.isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        piglatin.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of this word.
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in upper case or title case.
    was_upper = word.isupper()
    was_Title = word.istitle()

    word = word.lower()  # Make the word lowercase for translation.

    # Separate the consonants at the starting of this word.
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add pig-latin neding to the word.
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to upper case or title case.
    if was_Title:
        word = word.title()
    if was_upper:
        word = word.upper()

    # Add the non-letter characters back to the start ot the end of the word.
    word = prefixNonLetters + word + suffixNonLetters

    # Finally append the word to pig-latin.
    piglatin.append(word)

# Now print the joined pig-latin list.
print(' '.join(piglatin))
