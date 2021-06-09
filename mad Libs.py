# Read a text file.
textFile = open("C:\\Users\\harsh\\Desktop\\sonnet29.txt", 'r')  # Enter the path of the file to read here.
text = textFile.read()
text_edited = text

# Find the ADJECTIVE, NOUN, ADVERB or VERB occurences in the text.
# For each of these occurences demand replacements from the user.
while True:
    if 'ADJECTIVE' in text_edited:
        adjective = input("Enter an adjective: ")
        text_edited = text_edited.replace('ADJECTIVE', adjective, 1)
    if 'NOUN' in text_edited:
        noun = input("Enter a noun: ")
        text_edited = text_edited.replace('NOUN', noun, 1)
    if 'ADVERB' in text_edited:
        adverb = input("Enter an adverb: ")
        text_edited = text_edited.replace('ADVERB', adverb, 1)
    if 'VERB' in text_edited:
        verb = input("Enter a verb: ")
        text_edited = text_edited.replace('VERB', verb, 1)
    else:
        break
print('\n' + text_edited)
newTextFile = open('C:\\Users\\harsh\\Desktop\\file1.txt', 'w')  # Enter the path to create a new file.
newTextFile.write(text_edited)
