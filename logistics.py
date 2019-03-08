import sys
def instructions():
    print ("-----------------------------------")
    print ("Welcome to a python reader")
    print ("Press 1 to read the inputted text.")
    print ("Press 2 to read a .txt file")
    print ("Press 3 to read a .pdf file")
    print ("Press 4 to read a .png file ")
    print ("Press 5 to read a .jpg file")
    print ("Press 6 to read an .epub file")
    print ("Press x to exit the program")
    print ("-----------------------------------")

def error1():
    print ("\nERROR: Sorry invalid input. Please try again...")
    sys.exit(0)