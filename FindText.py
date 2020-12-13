import numpy as np
import os
import pytesseract
from PIL import Image
import cv2
from skimage import io

os.system("cls" if os.name == 'nt' else 'clear')

print("Hello! This programm detect English text on photo\n")


while True:
    file = input("Input local url: ")
    os.system("cls" if os.name == 'nt' else 'clear')
    if os.path.exists(file) == True:
        print("File detect\n")
        filename, file_extension = os.path.splitext(file)
        if (file_extension == '.jpeg' or file_extension == '.png' or file_extension == '.jpg' or file_extension == '.pbm' or
        file_extension == '.pgm' or file_extension == '.ppm' or file_extension == '.tiff' or
        file_extension == '.bmp' or file_extension == '.gif' or file_extension == '.webp'):
            print("Processing . . .")
            img = io.imread(file)
            img_rgb  =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB )
            text = pytesseract.image_to_string(img_rgb, lang = "rus+eng")
            os.system("cls" if os.name == 'nt' else 'clear')
            print ("Text on photo: \n\n" + text)
            boof = input("\n\n\n\nSave this text in file?(yn) ")
            if boof == 'y':
                thread = open("./Texts/sys.txt", "r")
                boof = thread.read()
                thread.close()
                os.remove("./Texts/sys.txt")
                thread = open("./Texts/sys.txt", "w")
                boof = int(boof) + 1
                thread.write(str(boof))
                thread.close()
                thread = open("./Texts/" + str(boof) + ".txt", "w", encoding='utf-8')
                thread.write(text)
                thread.close()
                os.system("cls" if os.name == 'nt' else 'clear')
                print("Text saved in file " + str(boof) + ".txt")
            boof = input("\n\nContinue?(y or n) ")
            if boof == 'n': 
                break
                os.system("cls" if os.name == 'nt' else 'clear')
        else: 
            print("Wrong extension (all available extensions see in file README.md)\n\n")
            continue
    else:
        print("File dont detect, check url\n\n")
