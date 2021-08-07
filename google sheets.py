import ezsheets

ss = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg/')
sheet = ss[0]
print('Finding the error...')
for rowNum in range(2, 15001):
    row = sheet.getRow(rowNum)
    try:
        beans_per_jar = int(row[0])
        jars = int(row[1])
        total_beans = int(row[2])
        beans_calculated = beans_per_jar * jars
        if beans_calculated != total_beans:
            print(f'Error in row number: {rowNum}')
            break
    except ValueError:
        print(f'Error in row number {rowNum}')
print('Error found!')
