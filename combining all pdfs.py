import PyPDF2
import os

currentDirFiles = os.listdir('.')
pdfFiles = []
for fileNames in currentDirFiles:
    if fileNames.endswith('.pdf'):
        pdfFiles.append(fileNames)

pdfFiles.sort(key=str.lower)

CombinedPdfFileObj = open('CombinedPdf.pdf', 'wb')
CombinedPdfWriterObj = PyPDF2.PdfFileWriter()

firstPageadded = False
for file in pdfFiles:
    firstPage = 0
    fileObj = open(file, 'rb')
    pdfFileReader = PyPDF2.PdfFileReader(fileObj)
    if pdfFileReader.isEncrypted:
        password = input(f'Please enter the password for {file}: ')
        pdfFileReader.decrypt(password)
    if firstPageadded:
        firstPage = 1
    if not firstPageadded:
        firstPage = 0
    for pageNum in range(firstPage, pdfFileReader.numPages):
        pagetToBeAdded = pdfFileReader.getPage(pageNum)
        CombinedPdfWriterObj.addPage(pagetToBeAdded)

CombinedPdfWriterObj.write(CombinedPdfFileObj)
CombinedPdfFileObj.close()
