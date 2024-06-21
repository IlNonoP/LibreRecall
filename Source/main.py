import subprocess
import time
import os


def take_screenshot():
    while True:    
        os.system("python3 take-screenshot.py")
        os.system("sleep 30")
   

def run_app():
    subprocess.Popen(['python3', 'app.py'])

if __name__ == "__main__":
    run_app()
    take_screenshot()       
          
