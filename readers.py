from gtts import gTTS
import os

#PDF reader
import PyPDF2

#PNG text 
try:            
    from PIL import Image
except ImportError:
    import Image
import pytesseract




lan = 'en'
def stringReader():
    text = 'Welcome to a python reader. Please enter your text here...'
    tts = gTTS(text=text, lang=lan, slow=False)
    tts.save("stringreader.mp3")       #save
    os.system("mpg321 stringreader.mp3")     #play
    os.remove("stringreader.mp3")   #delete after use


def txtReader():
    readFileName = input("Enter a file name: ")
    f = open(readFileName, "r")
    text = f.read()
    print (text)
    tts = gTTS(text=text, lang=lan, slow=False) 
    tts.save("textreader.mp3")      
    os.system("mpg321 textreader.mp3") 
    os.remove("textreader.mp3") 


def pdfReader():
    readFileName = input("Enter a file name: ")
    f = open(readFileName, "rb")
    read_pdf = PyPDF2.PdfFileReader(f)
    number_of_pages = read_pdf.getNumPages()
    i = 0
    for i in range(number_of_pages):    # read all pages
        page = read_pdf.getPage(i)
        page_content = page.extractText()
        print (page_content)
        tts = gTTS(text=page_content, lang=lan, slow=False)
        tts.save("pdfreader.mp3")
        os.system("mpg321 pdfreader.mp3")
        os.remove("pdfreader.mp3")

def pngReader():
    readFileName = input("Enter a file name: ")
    text = pytesseract.image_to_string(Image.open(readFileName))
    print(text)
    tts = gTTS(text=text, lang=lan, slow=False)
    tts.save("pngreader.mp3")
    os.system("mpg321 pngreader.mp3")
    os.remove("pngreader.mp3")