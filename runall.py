from readers import *

#print errors
from error import *  

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

#String Reader
if (inputtedText == '1'): 
    stringReader()

#.txt Reader
elif (inputtedText == '2'):
    txtReader()

#.pdf Reader 
elif (inputtedText == '3'):
    pdfReader()

#.png Reader
elif(inputtedText == '4'):
    pngReader()
elif (inputtedText == 'x'):
    print ("Thank you for using Reader. Now exiting...")
    sys.exit(0)
else:
    error1()
