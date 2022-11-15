from PIL import Image
from pytesseract import pytesseract


image = Image.open('text.png')
image = image.resize((400,200))
image.save('new.png')

#tesseract has to be installed locally 
path_to_tesseract = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(image)
#print the text line by line
print(text)