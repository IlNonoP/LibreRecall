import os
from PIL import Image
import pytesseract
from datetime import datetime

# Esegui lo screenshot utilizzando flameshot
os.system("flameshot full --path static/images --delay 0")


#leggi config e prendi il nome della lingua
file = open("config.txt", "r")
content = file.readlines()
language = content[0]
language = language.replace('OCR_LANGUAGE="', "")
language =language.replace('"', "")


# OCR dell'immagine catturata
image_path = 'static/images/screen.png'
ocr_text = pytesseract.image_to_string(Image.open(image_path), lang='ita_old')
# print(ocr_text)

# Genera un nome univoco per i file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
name_png = f"{timestamp}.png"
name_txt = f"{timestamp}.txt"

# Rinomina lo screenshot catturato
os.system(f"mv {image_path} static/images/{name_png}")

# Scrivi il testo OCR su un file di testo
with open(f"static/images/{name_txt}", 'w') as file:
    file.write(ocr_text)
