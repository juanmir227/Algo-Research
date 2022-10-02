import json
import pickle
import os
from dotenv import load_dotenv
load_dotenv()


transacciones = []

def join_txns():
    for i in range(10):

        f = open("block_data/block"+str(i)+".json")

        data = json.load(f)

        for i in data["block"]["txns"]:
            transacciones.append(i)

join_txns()
print(transacciones)

with open("block_data_joined/transacciones", 'wb') as fp:
    pickle.dump(transacciones, fp)