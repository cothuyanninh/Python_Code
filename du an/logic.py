import datetime
from PyPDF2 import PdfFileReader
import dateutil.parser


def converTime(small_data):
	
	return dateutil.parser.parse(small_data['timeUpload'])


def getNumberPagePdf(filepdf):
	pdf = PdfFileReader(open( filepdf ,'rb'))
	return pdf.getNumPages()

# getNumberPagePdf("./file/")