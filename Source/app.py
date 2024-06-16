import os
from flask import Flask, render_template, request
import operator

app = Flask(__name__)

# Funzione per ottenere tutti i file PNG nella directory images, ordinati per data di modifica (dal più recente al più vecchio)
def get_png_files():
    png_files = []
    image_dir = os.path.join(os.getcwd(), 'static', 'images')
    for filename in os.listdir(image_dir):
        if filename.lower().endswith('.png'):
            png_files.append(filename)
    
    # Ordina i file PNG per data di modifica (dal più recente al più vecchio)
    png_files.sort(key=lambda x: os.path.getmtime(os.path.join(image_dir, x)), reverse=True)
    
    return png_files

# Funzione per cercare parole chiave nei file .txt e ritornare i file PNG corrispondenti
def search_files(keyword):
    matching_png_files = []
    txt_files = get_txt_filenames()
    print(f"TXT Files found: {txt_files}")  # Debug print
    for txt_file in txt_files:
        txt_path = os.path.join(os.getcwd(), 'static', 'images', txt_file + '.txt')
        if os.path.exists(txt_path):
            print(f"Searching in {txt_file}.txt")  # Debug print
            with open(txt_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if keyword.lower() in content.lower():
                    matching_png_files.append(txt_file + '.png')
        else:
            print(f"File {txt_file}.txt does not exist!")  # Debug print
    return matching_png_files

# Funzione per ottenere tutti i nomi dei file .txt nella directory
def get_txt_filenames():
    txt_files = []
    current_dir = os.path.join(os.getcwd(), 'static', 'images')
    for filename in os.listdir(current_dir):
        if filename.lower().endswith('.txt'):
            txt_files.append(filename[:-4])  # Rimuove l'estensione .txt
    return txt_files

# Route per la pagina principale
@app.route('/')
def index():
    return render_template('index.html', png_files=get_png_files())

# Route per la ricerca
@app.route('/search', methods=['POST'])
def search():
    search_text = request.form['search_text']
    matching_png_files = search_files(search_text)
    return render_template('search_results.html', png_files=matching_png_files, search_text=search_text)

if __name__ == '__main__':
    app.run(debug=True)
