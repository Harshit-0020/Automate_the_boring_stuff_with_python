import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
MinutesPdfReader = PyPDF2.PdfFileReader(pdfFileObj)
MinutesFirstPage = MinutesPdfReader.getPage(0)

WaterFileObj = open('watermark.pdf', 'rb')
watermarkedfReader = PyPDF2.PdfFileReader(WaterFileObj)
watermarkFirstPage = watermarkedfReader.getPage(0)

MinutesFirstPage.mergePage(watermarkFirstPage)

pdfWriterObj = PyPDF2.PdfFileWriter()
pdfWriterObj.addPage(MinutesFirstPage)

for pageNum in range(1, MinutesPdfReader.numPages):
    pageObj = MinutesPdfReader.getPage(pageNum)
    pdfWriterObj.addPage(pageObj)

WatermarkedMinutesPdf = open('WatermarkedMinutesPdf.pdf', 'wb')
pdfWriterObj.write(WatermarkedMinutesPdf)
WatermarkedMinutesPdf.close()
pdfFileObj.close()
WaterFileObj.close()
