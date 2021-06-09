#! python3
# mcb.pyw
# Usage: py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - Deletes a keyword from the shelf file
#        py.exe mcb.pyw list - loads all keywords to clipboard.
#        py.exe mcb.pyw delete - deletes all the keywords from the shelf file.
#        py.exe mcb.pyw values - copies list of all value to the clipboard
import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print(f"Key {sys.argv[2]} and its corresponding text on clipboard added to the database.")
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
        print(f"Key {sys.argv[2]} removed from database.")

#  List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print("List of keys copied to clipboard.")
    if sys.argv[1].lower() == 'values':
        pyperclip.copy(str(list(mcbShelf.values())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print("All the data removed from the database.")
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f"Text belonging to {sys.argv[1]} copied to clipboard.")

mcbShelf.close()
