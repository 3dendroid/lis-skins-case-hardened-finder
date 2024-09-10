import os
import re

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'


def crop_and_recognize_digits_from_folder(folder_path, output_file):
    all_digits = []

    for filename in os.listdir (folder_path):
        if filename.lower ().endswith (('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join (folder_path, filename)
            try:
                image = Image.open (image_path)
                cropped_image = image.crop ((880, 880, 950, 930))
                text = pytesseract.image_to_string (cropped_image)
                digits = re.findall (r'\d+', text)
                all_digits.extend (digits)
                print (f"Digits from {filename}: {digits}")
            except Exception as e:
                print (f"An error occurred while processing {filename}: {e}")
    with open (output_file, 'w', encoding='utf-8') as file:
        file.write ("\n".join (all_digits))

    print (f"All digits have been saved to {output_file}.")


folder_path = r"C:\Users\GIGACHAD\PycharmProjects\lis-skins-case-hardened-finder\screenshots"
output_file = r"C:\Users\GIGACHAD\PycharmProjects\lis-skins-case-hardened-finder\texts\patterns.txt"

crop_and_recognize_digits_from_folder (folder_path, output_file)
