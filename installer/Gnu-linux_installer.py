import os
print("Select your distribution")
print("1 = Debian/Ubuntu")
print("2 = Arch")
scelta = input("Write and click enter: ")
if scelta == "1":
    os.system("sudo apt install flameshot tesseract-ocr tesseract-ocr-eng python3-pip")
    s.system("pip install pillow pyautogui pytesseract flask")
    

elif scelta == "2":
    os.system("sudo pacman -S flameshot tesseract-ocr tesseract-data-eng python3-pip")
    s.system("pip install pillow pyautogui pytesseract flask --break-system-package")
    
else:
    print("Not an option")
    os.system("sleep 3")
    exit()



os.system('flameshot config -f "screen"')
os.system("clear")
print("Now you must turn of notification in this pannel")
print("sleep 3")
os.system("flameshot config")
