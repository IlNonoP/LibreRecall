import os
import subprocess
while True:
    os.system("clear")
    print("Select your distribution")
    print("1 = Debian/Ubuntu")
    print("2 = Arch")
    scelta = input("Write and click enter: ")
    if scelta == "1":
        os.system("sudo apt install flameshot tesseract-ocr tesseract-ocr-eng python3-pip")
        os.system("pip install pillow pyautogui pytesseract flask --break-system-package")
        print(" ")
        print("Packages installation finished")
        os.system("sleep 3")
        break
        

    elif scelta == "2":
        os.system("sudo pacman -S flameshot tesseract-ocr tesseract-data-eng python-pip tesseract-data-eng")
        os.system("pip install pillow pyautogui pytesseract flask --break-system-package")
        print(" ")
        print("Packages installation finished")
        os.system("sleep 3")
        break
        
    else:
        print("Not an option")
        os.system("sleep 3")
        exit()

#gnome controll
DE = subprocess.check_output("echo $XDG_CURRENT_DESKTOP", shell=True)
DE = DE.decode('utf-8').strip()

if "GNOME" in DE or "gnome" in DE:
    while True:
        os.system("clear")
        print("you're currently using Gnome... to continue Screenshots sound is required to be turned off, otherwise you'd hear it every 30 seconds. Do you want to turn it off?")
        risposta = input("Y or N: ")
        risposta = risposta.lower()
        if risposta == "y":            
            os.system("sudo mv /usr/share/sounds/freedesktop/stereo/camera-shutter.oga /usr/share/sounds/freedesktop/stereo/camera-shutter-disabled.oga")
            print("Screenshoot_sound: OFF")
            os.system("sleep 2")
            break
        elif risposta == "n":
            print("the installation will continue anyway... but you will hear this sound every time, to remove it restart the installer")
            input("Press Enter to continue...")
            break
        else:
            print("Invalid answer")



#flameshot manual config
os.system('flameshot config -f "screen"')
os.system("clear")
print('Now you must turn of notification in the next pannel. go to the "General" section and deselect "Desktop Notification"')
input("Press Enter to continue...")
os.system("flameshot config")

