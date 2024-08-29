import subprocess
import time
import os

#def data from config file
file_config = open('LibreRecall.conf', 'r') 
data_config = file_config.readlines() 
sleep_time = data_config[3].split('=', 1)[1]
sleep_time = sleep_time.split(' ', 1)[0]

server_mode = data_config[5].split('=', 1)[1]
server_mode = server_mode.split(' ', 1)[0]



def take_screenshot():
    while True:    
        os.system("python3 take-screenshot.py")
        comando = "sleep "+ sleep_time
        os.system(comando)
   

def run_app():
    subprocess.Popen(['python3', 'app.py'])

if __name__ == "__main__":
    run_app()
    if server_mode == "true":
        print("Server mode enable")   
    else:
        take_screenshot()  
          
