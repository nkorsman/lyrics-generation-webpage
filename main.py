from flask import Flask
from flask import url_for, render_template
from textgenrnn import textgenrnn
#import warnings
#warnings.filterwarnings("ignore")

app = Flask(__name__)

#def load_model():
#    global textgen
#    textgen = textgenrnn("textgenrnn_weights_4epochs.hdf5")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/foo', methods=['POST'])
def foo():
    textgen = textgenrnn("textgenrnn_weights_4epochs.hdf5")
    lyrics = textgen.generate(n=20, return_as_list=True)
    return "\n".join(lyrics)

if __name__ == "__main__":
    #load_model()
    app.run(threaded=False)
