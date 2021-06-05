#! python3
# mclip.py - A multi-Clipboard Program
import sys
import pyperclip
Text = {
    'greet': 'Hello, how are you ?',
    'gm': 'Good Morning',
    'ge': 'Good Evening',
    'ga': 'Good Afternoon',
    'bye': 'Bye, see you later.',
    'agree': 'Yes, I agree. That sounds fine to me',
    'busy': 'Sorry, can we do this later this week or next week ?',
}
if len(sys.argv) < 2:
    print("Usage: py mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]
if keyphrase in Text.keys():
    pyperclip.copy(Text.get(keyphrase))
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print('There is no text for ' + keyphrase)
