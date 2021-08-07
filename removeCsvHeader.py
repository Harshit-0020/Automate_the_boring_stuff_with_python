import os
import csv

csvFiles = []
for files in os.listdir('.'):
    if files.endswith('.csv'):
        csvFiles.append(files)

for file in csvFiles:
    print('Reading data from ' + file + ' ...')
    data = []
    fileObj = open(file, 'r')
    csvReader = csv.reader(fileObj)
    for row in csvReader:
        if csvReader.line_num != 1:
            data.append(row)
    fileObj.close()
    print('Writing beginning for ' + file + ' ...')
    writing_file = open(file, 'w', newline='')
    csvWriter = csv.writer(writing_file)
    for row in data:
        csvWriter.writerow(row)
    writing_file.close()
    print('Writing ' + file + ' completed')
print('Done!')