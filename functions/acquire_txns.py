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