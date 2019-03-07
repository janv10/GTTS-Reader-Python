from gtts import gTTS
import os
from error import * 
import PyPDF2

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


print ("-----------------------------------")
print ("Welcome to a python reader")
print ("Press 1 to read the inputted text.")
print ("Press 2 to read a .txt file")
print ("Press 3 to read a .pdf file")
print ("Press 4 to read a .png ")
print ("Press x to exit the program")
print ("-----------------------------------")

inputtedText = input("Please enter a number: ")
lan = 'en'

if (inputtedText == '1'):
    text = 'Welcome to a python reader. Please enter your text here...'
    tts = gTTS(text=text, lang=lan, slow=False)
    tts.save("welcome.mp3")
    os.system("mpg321 --speed 20 welcome.mp3")
elif (inputtedText == '2'):
    readFileName = input("Enter a file name: ")
    f = open(readFileName, "r")
    text = f.read()
    print (text)
    tts = gTTS(text=text, lang=lan, slow=False)
    tts.save("textreader.mp3")
    os.system("mpg321 textreader.mp3")
elif (inputtedText == '3'):
    readFileName = input("Enter a file name: ")
    f = open(readFileName, "rb")
    read_pdf = PyPDF2.PdfFileReader(f)
    number_of_pages = read_pdf.getNumPages()
    i = 0
    for i in range(number_of_pages):
        page = read_pdf.getPage(i)
        page_content = page.extractText()
        print (page_content)
        tts = gTTS(text=page_content, lang=lan, slow=False)
        tts.save("pdfreader.mp3")
        os.system("mpg321 pdfreader.mp3")
elif(inputtedText == '4'):
    readFileName = input("Enter a file name: ")
    text = pytesseract.image_to_string(Image.open(readFileName))
    print(text)
    tts = gTTS(text=text, lang=lan, slow=False)
    tts.save("pngreader.mp3")
    os.system("mpg321 pngreader.mp3")
elif (inputtedText == 'x'):
    print ("Thank you for using Reader. Now exiting...")
    sys.exit(0)
else:
    error1()
