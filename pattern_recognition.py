import cv2
import pytesseract
from PIL import Image

# img = cv2.imread('pattern.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
# custom_oem_psm_config = '--oem 3 --psm 6'  # Optimal for text in images with noisy text
# config = f'--psm 6 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# text = pytesseract.image_to_string(img, config=custom_oem_psm_config)
# print(text)

image = Image.open("pattern.png")  # cropping image
cropped_image = image.crop((1000, 0, 1400, 150))  # coordinates
cropped_image.save("cropped_pattern.png")
text = pytesseract.image_to_string(cropped_image)
print(text)

