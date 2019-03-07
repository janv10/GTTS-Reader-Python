#Google Text to Speech lib
from gtts import gTTS
import os

from readers import *
#PDF reader
import PyPDF2

#PNG text 
try:            
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#print errors
from error import *  

