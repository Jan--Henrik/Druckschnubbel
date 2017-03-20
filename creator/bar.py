import sys
import barcode
from barcode.writer import ImageWriter

def printBarcode(name="abort"):
	print("MEOW")
	EAN = barcode.get_barcode_class('code128')
	print(EAN)
	ean = EAN(name, writer=ImageWriter())
	print(ean)
	ean.save('app/uploads/bcode.png')
