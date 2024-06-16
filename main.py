import subprocess
import time

def take_screenshot():
    subprocess.Popen(['python', 'take-screenshot.py'])

def run_app():
    subprocess.Popen(['python', 'app.py'])

if __name__ == "__main__":
    while True:
        take_screenshot()
        run_app()
        time.sleep(30)  
