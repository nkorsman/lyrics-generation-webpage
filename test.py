from textgenrnn import textgenrnn
textgen = textgenrnn("textgenrnn_weights_4epochs.hdf5")
lyrics = textgen.generate(n=10, return_as_list=True)
print(lyrics)
