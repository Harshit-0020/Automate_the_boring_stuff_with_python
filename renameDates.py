#! python3
# renameDates.py - Renames files with American MM-DD-YYYY format
# to European DD-MM-YYYY format.

import shutil
import os
import re

# Create a regex that matches the filename with the American date format.
datePattern = re.compile(r'''
    ^(.*?)                  # all text before the date
    ((0|1)?\d)-             # one or two digits for the month. Here 0|1 can be written as [01]
    ((0|1|2|3)?\d)-         # one or two or three digits for the day. Here 0|1|2|3 can be written as [0123]
    ((19|20)\d\d)           # four digits for the year
    (.*?)$                  # all text after the date
''', re.VERBOSE)

# Loop over the files in the working directory.
for amerFile in os.listdir('.'):
    mo = datePattern.search(amerFile)
    # Skip files without a date.
    if mo is None:
        continue

    # Get different parts of the filename.
    partBeforeDate = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    remainingSuffix = mo.group(8)

    # Form the European style filename.
    euroFilename = partBeforeDate + day + '-' + month + '-' + year + remainingSuffix

    # Get the full, absolute file path.
    absWorkingDir = os.path.abspath('.')
    amerFilepath = os.path.join(absWorkingDir, amerFile)
    euroFilepath = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f"Renaming {amerFilepath} to {euroFilepath} ...")

    # shutil.move(amerFilepath, euroFilepath)
