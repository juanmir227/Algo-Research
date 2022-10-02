import pickle

with open("new_block_data/block_data.pickle", 'rb') as what:
    bloques = pickle.load(what)

print(bloques[0]["block"])
