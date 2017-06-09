#!/home/brucelau/apps/virtualenv/bin/python

#get args
import sys

pdf_filenames = sys.argv[1:]
assert pdf_filenames

#reading pdfs
from pdfrw import PdfReader
"""
x = PdfReader('source/07922XXX2258-2017Apr13-2017May15.pdf')
print x.keys()
print x.Info
print x.Root.keys()
print len(x.pages)
print x.pages[0]
print x.pages[0].Contents
print x.pages[0].Contents.stream

"""

#writing pdfs
from pdfrw import PdfWriter
writer = PdfWriter()
#y.addpage(x.pages[0])
#y.write('out.pdf')

for pdf_filename in pdf_filenames:
    writer.addpages(PdfReader(pdf_filename).pages)

from pdfrw import IndirectPdfDict
writer.trailer.Info = IndirectPdfDict(
        Title='pdf bundle',
        Author='Adobe',
        Subject='pdf',
        Creator='Adobe',
        )
writer.write('out.pdf')
