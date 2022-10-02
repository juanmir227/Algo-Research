import pickle
import os
from progress.bar import Bar
from dotenv import load_dotenv
load_dotenv()


def join_txns(block_data):
    transacciones = []
    bar = Bar('Processing', max=len(block_data))
    for i in range(len(block_data)):
        block = block_data[i]
        for j in block["block"]["txns"]:
            transacciones.append(j)
        bar.next()
    bar.finish()
    return transacciones

with open(os.environ["SAVE_BLOCK_PATH"],'rb') as f:
    data = pickle.load(f)

transacciones = join_txns(data)

print(len(transacciones))

with open("new_block_data/txns_data.pickle", 'wb') as fp:
    pickle.dump(transacciones, fp)