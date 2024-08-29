# LibreRecall
![logo](https://github.com/IlNonoP/LibreRecall/assets/172937845/798030f6-af36-4c81-bf69-e86b3ee37ab2)

Hello! This is an alternative for Linux to Microsoft Recall! This project was born because OpenRecall didn't work for me (https://github.com/openrecall/openrecall) 

# Introduction
Every 30 seconds the program takes a screenshot and an OCR reads the screen and saves the text in a file with the same name as the screenshoot. On the house you can see the whole screenshot and the date:
![home](https://github.com/IlNonoP/LibreRecall/assets/172937845/cb03c9eb-b3d2-416b-8e1e-7ac641e6aaa0)
When we search for a word, LibreRecall finds that word in the txt file and shows the corresponding image on the page:
![serach](https://github.com/IlNonoP/LibreRecall/assets/172937845/5968d16d-3442-4287-8cc9-cce78e9a3e24)

# Installation
## Linux
You have two way to dowload the program:
1) You can use the relase section to download the latest version. After downloading, you can unzip the archive, place the program files and folders anywhere on the system as long as they are in the same directory.
2) You can clone the repository and go to the "Source" folder

Once this is done, you can start the "Gnu-linux_installer.py".
After that, you can run main.py. Connect to "127.0.0.1:[your port]" to use the program.
Your port is by default 5000, but you may have changed it in the configuration file.

# Config File
The configuration file (added in version 0.5) allows for greater user control. The file is created to work right away... so if you are not technical you can either jump during installation and leave the default options. You can reconfigure it either with a simple text editor or with the installation script (recommended). File looks like this:
```
LibreRecall, github link: https://github.com/IlNonoP/LibreRecall
PORT=5000 #defaul 5000
IMAGES_PATH="static/images/" #the directory where the images and.txt files will be saved. default static/images/ (must end with /)
TIME_BETWEEN_SCREENSHOT=30 #the time in seconds between screenshots
REMOTE_ACCESS=false #by default it is false, it allows you to connect to the web interface via the IP of the computer on which it is running
SERVER=false #by default is false. This option can turn off screenshoot function. LibreRecall. The program will only become a self-hosted web page, you just have to find a way to save the files created by LibreRecall on your PC in your server
```
Each option is already commented on, but let's see them specifically

**PORT**: Indicates the port on which the service will be displayed

**IMAGES_PATH**: Indicates the path where you want to save images

**TIME_BETWEEN_SCREENSHOT**: The expected time in seconds between screenshots

**REMOTE_ACCESS**: Ability or disable the possibility of accessing it via another PC

**SERVER**: It will disable Screenshot capture and will only serve as a web page to access the data

# Known Issues
[GNOME < 42] There is a confirmation screen for all the screenshot (Zorin OS ask always)

[Arch linux] Sometimes you may need to insert the "Tesseract-data-eng" package manually in addition to installing with the installation file

# Email:
IlNonoP@outlook.it



