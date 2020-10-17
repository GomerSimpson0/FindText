import numpy as np
import os
import pytesseract
from PIL import Image
import cv2
from skimage import io

os.system("cls")

print(" Вас приветствует программа распознования текста на фотографии\n")


while True:
	file = input(" Введите путь до фотографии: ")
	os.system("cls")
	if os.path.exists(file) == True:
		print(" Файл успешно обнаружен\n")
		filename, file_extension = os.path.splitext(file)
		if (file_extension == '.png' or file_extension == '.jpg' or file_extension == '.pbm' or
		    file_extension == '.pgm' or file_extension == '.ppm' or file_extension == '.tiff' or
		    file_extension == '.bmp' or file_extension == '.gif' or file_extension == '.webp'):
			print(" Обработка . . .")
			img = io.imread(file)
			img_rgb  =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB )
			text = pytesseract.image_to_string(img_rgb, lang = "rus+eng")
			os.system("cls")
			print (" Текст, который был на фотографии: \n\n" + text)
			boof = input("\n\n\n\n Сохранить этот текст в файл?(y or n) ")
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
				os.system("cls")
				print(" Ваш текст сохранён в файл " + str(boof) + ".txt")
			boof = input("\n\n Продолжить?(y or n) ")
			if boof == 'n':
				break
			os.system("cls")
		else: 
			print(" Неверное расширение файла (все расширения смотреть в файле README.txt)\n\n")
			continue
	else: print(" Файл не найден, проверьте путь до файла\n\n")