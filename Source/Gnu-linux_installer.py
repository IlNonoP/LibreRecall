import os
import subprocess


def set_librerecall():
   

    os.system("clear")
    
    print("Now it's time to configure LibreRecall")
    print("in which port do you want to perform LibreRecall? press enter to default")
    print("default = 5000")
    porta = input("Write and press enter: ")
    if porta == "":
        porta = "5000"
    print("Port: {}".format(porta))
    input("Press enter to continue")
    os.system("clear")

    print("In which directory do you want to save images? press enter to default")
    print("default = static/images/")
    directory = input("Write and press enter: ")
    if directory == "":
        directory = "static/images/"
    if directory.endswith("/") == False:
        directory = directory +"/"
    print("Directory: {}".format(directory))
    input("Press enter to continue")
    os.system("clear")

    print("Now, every how many seconds do you want the Screenshot taken? press enter for default")
    print("default = 30")
    time = input("Write and press enter: ")
    if time == "":
        time = "30"
    print("Time: {}".format(time))
    input("Press enter to continue")


    while True:
        os.system("clear")
        print("Do you want enable server mode? press enter for default")
        print("default = false")
        server_mode = input("Write true or false, and press enter: ")
        if server_mode == "True" or server_mode == "true":
            server_mode = "true"
            break
        elif server_mode == "False" or server_mode == "false" or server_mode == "":
            server_mode = "false"
            break
        else:            
            input("Invalid option, press enter to continue")
    print("Server mode: {}".format(server_mode))
    input("Press enter to continue")
    

    while True:
        os.system("clear")
        print("Last question, do you want to be able to access the service from your local network or do you only want to access it from this computer? press enter for default")
        print("default = false")
        address = input("Write true or false, and press enter: ")
        if address == "True" or address == "true":
            address = "true"
            break
        elif address == "False" or address == "false" or address == "":
            address = "false"
            break
        else:            
            input("Invalid option, press enter to continue")

    

    os.system("rm LibreRecall.conf")
    file_config = open("LibreRecall.conf", "w")
    file_config.write("LibreRecall, github link: https://github.com/IlNonoP/LibreRecall")
    file_config.write("\nPORT={} #defaul 5000".format(porta))
    file_config.write('\nIMAGES_PATH="{}" #the directory where the images and.txt files will be saved. default static/images/ (must end with /)'.format(directory))
    file_config.write("\nTIME_BETWEEN_SCREENSHOT={} #the time in seconds between screenshots".format(time))
    file_config.write("\nREMOTE_ACCESS={} #by default it is false, it allows you to connect to the web interface via the IP of the computer on which it is running".format(address))
    file_config.write("\nSERVER={} #by default is false. This option can turn off screenshoot function. LibreRecall. The program will only become a self-hosted web page, you just have to find a way to save the files created by LibreRecall on your PC in your server".format(server_mode))
    file_config.close()
    os.system("clear")
    print("Excellent! Configuration file created! You can find it in the same execution directory as the script, if you extracted everything in the same folder you're fine like this. If you want to edit it you can open it at any time, otherwise restart the installation script and select 'Config LibreRecall'")  
    input("Press enter to continue...")



while True:
    os.system("clear")
    print("Select your distribution")
    print("1 = Debian/Ubuntu")
    print("2 = Arch")
    print("3 = Config LibreRecall")
    scelta = input("Write and click enter: ")
    if scelta == "1":
        os.system("sudo apt install flameshot tesseract-ocr tesseract-ocr-eng python3-pip")
        os.system("pip install pillow pyautogui pytesseract flask --break-system-package")
        print(" ")
        print("Packages installation finished")
        os.system("sleep 3")
        break
        

    elif scelta == "2":
        os.system("sudo pacman -S flameshot tesseract tesseract-data-eng python-pip tesseract-data-eng")
        os.system("pip install pillow pyautogui pytesseract flask --break-system-package")
        print(" ")
        print("Packages installation finished")
        os.system("sleep 3")
        break

    elif scelta == "3":
        set_librerecall()
        exit()

        
    else:
        print("Not an option")
        os.system("sleep 3")
        exit()

while True:
    os.system("clear")
    risposta = input("Do you want edit the configation? Y/N: ")
    if risposta.lower() == "y":
        set_librerecall()
        break
    elif risposta.lower() == "n":
        break
    else:
        print("Invalid option")
        input("Press enter to continue...")




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
os.system("clear")
print('Now you must turn of notification in the next pannel. go to the "General" section and deselect "Desktop Notification", after that close the setting of flameshot')
input("Press Enter to continue...")
os.system('flameshot config -f "screen"')
os.system("flameshot config")
os.system("clear")
print("Oh yes! librecall is finally ready! Now all you have to do is start the 'main.py' file and wait for the magic! If you have any problems, try resetting the configuration file, perhaps it has been set badly :-). If not, don't hesitate to make yourself heard on GitHub!")
input("Press enter to close the installer...")
