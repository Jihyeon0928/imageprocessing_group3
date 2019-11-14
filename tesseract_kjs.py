##https://github.com/madmaze/pytesseract

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract' #full path to your tesseract excutable


img = Image.open('[Input your data name]')
print(img)

imgArr = Image.fromarray(img)
print(imgArr)

img2txt = pytesseract.image_to_string(imgArr)
print(img2txt)
f = open("[txt file name]", 'w')
f.write(img2txt)
f.close()

pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
print(pdf)
img2txt.save('[path]',format='PDF')
