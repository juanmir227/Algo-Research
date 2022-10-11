import pandas as pd
import pickle
import os
import base64
import ast
from dotenv import load_dotenv
load_dotenv()

number_of_blocks = 300
with open(os.environ["SAVE_TXN_PATH"]+str(number_of_blocks),'rb') as fp:
    transacciones = pickle.load(fp)

zero_address = '0000000000000000000000000000000000000000000000000000000000' #uso esta adress como receiver cuando no hay

txn_type = []
txn_note = []
txn_block = []
snd_addresses = []
rcv_addresses = []
amount=[]
app_or_asset_id = []
for transaction in transacciones:
    type = transaction["txn"]["type"]
    txn_type.append(type)
    txn_block.append(transaction['block'])
    if 'amt' in transaction['txn']:
        amount.append(transaction['txn']['amt'])
    elif 'aamt' in transaction['txn']:
        amount.append(transaction['txn']['aamt'])
    else:
        amount.append('NA')
    if 'xaid' in transaction['txn']:
        app_or_asset_id.append(transaction['txn']['xaid'])
    elif 'apid' in transaction['txn']:
        app_or_asset_id.append(transaction['txn']['apid'])
    else:
        app_or_asset_id.append('NA')
    if 'note' in transaction['txn']:
        txn_note.append(transaction['txn']['note'])
    else:
        txn_note.append('NA')
    if 'arcv' in transaction["txn"].keys():
        snd_addresses.append(transaction["txn"]["snd"])
        rcv_addresses.append(transaction["txn"]["arcv"])
        
    elif 'rcv' in transaction["txn"].keys():
        snd_addresses.append(transaction["txn"]["snd"])
        rcv_addresses.append(transaction["txn"]["rcv"])
    else:
        snd_addresses.append(transaction["txn"]["snd"])
        rcv_addresses.append(zero_address)

notes = []

# for note in txn_note:
for note in txn_note:

    if note != 'NA':
        notes_b = base64.b64decode(note)
        notes.append(notes_b)
    else:
        notes.append(note)
#     print('hey')
#     notes_b = base64.b64decode(note)
    # note_str = notes_b.decode("UTF-8", errors = 'ignore')
    # notes.append(ast.literal_eval(note_str))
    # note_dict.append(ast.literal_eval(repr(note_bytes)))


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
    'App or Asset Id': app_or_asset_id,
}

df = pd.DataFrame(data)
print(df)

df.to_pickle(os.environ['SAVE_DF_PATH']+str(number_of_blocks))