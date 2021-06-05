#! python3
import pyperclip
import re
phone_number_regex = re.compile(r'''
                            (\d{3}|\(|d{3}\))               # area code
                            (\s|-|\.)                       #separator
                            (\d{3})                           # first three digits
                            (\s|-|\.)                       # separator
                            (\d{4})                           # last four digits
                            (\s*(ext|x|ext\.)\s*(\d{2,5}))?   #extension
                            ''', re.VERBOSE)

email_address_regex = re.compile(r"""
                                    ([a-zA-Z0-9._%+-]+)           # username
                                    (@)                           # @ symbol
                                    ([a-zA-Z0-9.-]+)              # domain name
                                    (\.[a-zA-Z]{2,4})           # dot-something
                                    """, re.VERBOSE)

# Find the matches in the clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phone_number_regex.findall(text):
    phoneNum = '-'.join([groups[0], groups[2], groups[4]])
    if groups[7] != '':
        phoneNum += ' x' + groups[7]
    matches.append(phoneNum)

for groups in email_address_regex.findall(text):
    emai_id = ''
    for group_strings in groups:
        emai_id += group_strings
    matches.append(emai_id)

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
