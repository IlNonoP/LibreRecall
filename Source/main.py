import subprocess
import time
import os

def take_screenshot():
    os.system("python3 take-screenshot.py")
    #subprocess.Popen(['python3', 'take-screenshot.py'])

def run_app():
    subprocess.Popen(['python3', 'app.py'])

if __name__ == "__main__":
    run_app()
    take_screenshot()       
          
