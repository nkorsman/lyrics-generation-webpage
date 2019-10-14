from flask import Flask
import os
from flask import url_for, render_template, send_from_directory
from textgenrnn import textgenrnn

app = Flask(__name__)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/foo', methods=['POST'])
def foo():
    textgen = textgenrnn("textgenrnn_weights_4epochs.hdf5")
    lyrics = textgen.generate(n=20, return_as_list=True)
    return "\n".join(lyrics)

if __name__ == "__main__":
    app.run(threaded=False)
