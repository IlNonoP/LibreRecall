import os
from flask import Flask, render_template, send_from_directory, request, url_for

file_config = open('LibreRecall.conf', 'r')
data_config = file_config.readlines()
image_directory = data_config[2].split('"', 1)[1]
image_directory = image_directory.split('"', 1)[0]


app = Flask(__name__)

def get_png_files():
    png_files = []
    image_dir = image_directory
    for filename in os.listdir(image_dir):
        if filename.lower().endswith('.png'):
            png_files.append(filename)
    
    png_files.sort(key=lambda x: os.path.getmtime(os.path.join(image_dir, x)), reverse=True)
    
    return png_files

# Funzione per cercare parole chiave nei file .txt e ritornare i file PNG corrispondenti, ordinati per data di modifica
def search_files(keyword):
    matching_png_files = []
    txt_files = get_txt_filenames()
    image_dir = image_directory

    print(f"TXT Files found: {txt_files}")  # Debug print
    for txt_file in txt_files:
        txt_path = os.path.join(image_dir, txt_file + '.txt')
        if os.path.exists(txt_path):
            print(f"Searching in {txt_file}.txt")  # Debug print
            with open(txt_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if keyword.lower() in content.lower():
                    matching_png_files.append(txt_file + '.png')
        else:
            print(f"File {txt_file}.txt does not exist!")  # Debug print

    # Ordina i file PNG corrispondenti per data di modifica (dal più recente al più vecchio)
    matching_png_files.sort(key=lambda x: os.path.getmtime(os.path.join(image_dir, x)), reverse=True)

    return matching_png_files


def get_txt_filenames():
    txt_files = []
    current_dir = image_directory
    for filename in os.listdir(current_dir):
        if filename.lower().endswith('.txt'):
            txt_files.append(filename[:-4])  # Remove .txt extension
    return txt_files

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(image_directory, filename)


@app.route('/')
def index():
    png_files = get_png_files()
    return render_template('index.html', png_files=png_files)

# Route per la ricerca
@app.route('/search', methods=['POST'])
def search():
    search_text = request.form['search_text']
    matching_png_files = search_files(search_text)
    return render_template('search_results.html', png_files=matching_png_files, search_text=search_text)




if __name__ == '__main__':
     #set address
    file_config = open('LibreRecall.conf', 'r') 
    data_config = file_config.readlines()
    expose=data_config[4].split('=', 1)[1]
    if expose.startswith("true"):
        address = "0.0.0.0"
    else:
        address = "127.0.0.1"  

     #set port
    file_config = open('LibreRecall.conf', 'r') 
    data_config = file_config.readlines()
    porta=data_config[1].split('=', 1)[1]
    porta = porta.split(" #", 1)[0] 
    
   
    app.run(host=address, port=porta, debug=False)
