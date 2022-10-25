import pickle
import os
from progress.bar import Bar
from dotenv import load_dotenv
load_dotenv()


def join_txns(block_data):
    transacciones = []
    bar = Bar('Processing', max=len(block_data))
    for block in block_data:
        for txn in block["block"]["txns"]:
            txn['block']= block['block']['rnd']
            transacciones.append(txn)
        bar.next()
    bar.finish()
    return transacciones



number_of_blocks = int(os.environ["NUMBER_OF_BLOCKS"])

with open(os.environ["SAVE_BLOCK_PATH"] + str(number_of_blocks),'rb') as f:
    data = pickle.load(f)

transacciones = join_txns(data)

with open(os.environ["SAVE_TXN_PATH"]+str(number_of_blocks), 'wb') as fp:
    pickle.dump(transacciones, fp)