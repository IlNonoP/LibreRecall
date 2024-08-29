import os
from PIL import Image
import pytesseract
from datetime import datetime

#set data from LibreRecall.conf
file_config = open('LibreRecall.conf', 'r') 
data_config = file_config.readlines() 
image_directory = data_config[2].split('"', 1)[1]
image_directory = image_directory.split('"', 1)[0]
print(image_directory)


os.makedirs(os.path.dirname(image_directory), exist_ok=True)


  
os.system('while xset q | grep -q "Monitor is Off"; do sleep 1; done') #solo se è sbloccato

    # Esegui lo screenshot
comando = "flameshot full --path {} --delay 0".format(image_directory)
os.system(comando)       
   


    # OCR dell'immagine catturata
image_path = '{}/screen.png'.format(image_directory)
ocr_text = pytesseract.image_to_string(Image.open(image_path))
ocr_text = ocr_text.lower()
    # print(ocr_text)

    # Genera un nome univoco per i file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
name_png = f"{timestamp}.png"
name_txt = f"{timestamp}.txt"

    # Rinomina lo screenshot catturato
os.system(f"mv {image_path} {image_directory}/{name_png}")
    # Scrivi il testo OCR su un file di testo
with open(f"{image_directory}{name_txt}", 'w') as file:
    file.write(ocr_text)

