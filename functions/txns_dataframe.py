import pandas as pd
import pickle
import os
from dotenv import load_dotenv
load_dotenv()

with open(os.environ["SAVE_BLOCK_PATH"],'rb') as fp:
    transacciones = pickle.load(fp)

zero_address = '0000000000000000000000000000000000000000000000000000000000' #uso esta adress como receiver cuando no hay

txn_type=[]
total_addresses = []
snd_addresses = []
rcv_addresses = []

for i in range(len(transacciones)):
    txn_type.append(transacciones[i]["txn"]["type"])
    if 'arcv' in transacciones[i]["txn"].keys():
        total_addresses.append(transacciones[i]["txn"]["snd"])
        total_addresses.append(transacciones[i]["txn"]["arcv"])
        snd_addresses.append(transacciones[i]["txn"]["snd"])
        rcv_addresses.append(transacciones[i]["txn"]["arcv"])
        
    elif 'rcv' in transacciones[i]["txn"].keys():
        total_addresses.append(transacciones[i]["txn"]["snd"])
        total_addresses.append(transacciones[i]["txn"]["rcv"])
        snd_addresses.append(transacciones[i]["txn"]["snd"])
        rcv_addresses.append(transacciones[i]["txn"]["rcv"])
    else:
        snd_addresses.append(transacciones[i]["txn"]["snd"])
        rcv_addresses.append(zero_address)
        total_addresses.append(transacciones[i]["txn"]["snd"])
        total_addresses.append(zero_address)
 
# print(txn_type)
# print(total_addresses)
# print(len(rcv_addresses))
# print(len(snd_addresses))
print(list(set(snd_addresses)))

data = {
    'Sender Address': snd_addresses,
    'Receiver Address': rcv_addresses,
    'Transaction Type': txn_type,
}
df = pd.DataFrame(data)
df

print(df)
