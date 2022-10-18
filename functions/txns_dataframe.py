import pandas as pd
import pickle
import os
import base64
import ast
from dotenv import load_dotenv
load_dotenv()

number_of_blocks = int(os.environ["NUMBER_OF_BLOCKS"])
with open(os.environ["SAVE_TXN_PATH"]+str(number_of_blocks),'rb') as fp:
    transacciones = pickle.load(fp)

txn_type = []
txn_note = []
txn_block = []
snd_addresses = []
rcv_addresses = []
amount=[]
asset_id = []


for transaction in transacciones:
    #agrego el tipo de transaccion
    txn_type.append(transaction["txn"]["type"])
    #agrego el numero de bloque
    txn_block.append(transaction['block'])
    #lleno el vector de amount
    if 'amt' in transaction['txn']:
        amount.append(transaction['txn']['amt'])
    elif 'aamt' in transaction['txn']:
        amount.append(transaction['txn']['aamt'])
    else:
        amount.append('NA')
    #lleno el vector de asset id
    if 'xaid' in transaction['txn']:
        asset_id.append(transaction['txn']['xaid'])
    else:
        asset_id.append('NA')
    #si interactua con un aplicacion en reciever agrego el id de la aplicacion
    if 'apid' in transaction['txn']:
        snd_addresses.append(transaction["txn"]["snd"])
        rcv_addresses.append(transaction['txn']['apid'])
    #si existe una nota en la transaccion la guardo no se para que
    if 'note' in transaction['txn']:
        txn_note.append(transaction['txn']['note'])
    else:
        txn_note.append('NA')
    #lleno los receivers y los senders
    if 'arcv' in transaction["txn"]:
        snd_addresses.append(transaction["txn"]["snd"])
        rcv_addresses.append(transaction["txn"]["arcv"])
        
    elif 'rcv' in transaction["txn"]:
        snd_addresses.append(transaction["txn"]["snd"])
        rcv_addresses.append(transaction["txn"]["rcv"])
    elif 'caid' in transaction:
        snd_addresses.append(transaction['txn']['snd'])
        rcv_addresses.append(transaction['caid'])


notes = []

# for note in txn_note:
for note in txn_note:

    if note != 'NA':
        notes_b = base64.b64decode(note)
        notes.append(notes_b)
    else:
        notes.append(note)


# dict_str = note_bytes.decode('UTF-8')
# note = ast.literal_eval(dict_str)

# note_deco = []
# for i in range(len(txn_note)):
#     note = txn_note[i]
#     note.byte_str.decode('UTF-8')

data = {
    'Sender Address': snd_addresses,
    'Receiver Address': rcv_addresses,
    'Transaction Type': txn_type,
    'Transaction note': notes,
    'Transaction block': txn_block,
    'Transaction Amount': amount,
    'Asset Id': asset_id,
}

df = pd.DataFrame(data)
print(df)

df.to_pickle(os.environ['SAVE_DF_PATH']+str(number_of_blocks))