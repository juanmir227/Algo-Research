import base64
from dotenv import load_dotenv
load_dotenv()

def make_df(transacciones):
    txn_type = []
    txn_note = []
    txn_block = []
    snd_addresses = []
    rcv_addresses = []
    amount=[]
    asset_id = []
    zero_address = "0000000000000000000000000000000000000000000000000000000000"
    for transaction in transacciones:

        type = transaction['txn']['type']
        txn_type.append(type)
        txn_block.append(transaction['block'])
        if 'note' in transaction['txn']:
            txn_note.append(transaction['txn']['note'])
        else:
            txn_note.append('NA')
        if 'amt' in transaction['txn']:
            amount.append(transaction['txn']['amt'])
        elif 'aamt' in transaction['txn']:
            amount.append(transaction['txn']['aamt'])
        else:
            amount.append('NA')

        #divido por types lo que hago con cada uno

        if type == 'pay':
            if 'close' in transaction['txn']:
                snd_addresses.append(transaction['txn']['snd'])
                rcv_addresses.append(transaction['txn']['close'])
                asset_id.append('NA')
            else:
                snd_addresses.append(transaction['txn']['snd'])
                rcv_addresses.append(transaction['txn']['rcv'])
                asset_id.append('NA')

        if type == 'keyreg':
            snd_addresses.append(transaction['txn']['snd'])
            rcv_addresses.append(zero_address)
            asset_id.append('NA')
    
        if type == 'acfg':
            if 'caid' in transaction:
                snd_addresses.append(transaction['txn']['snd'])
                rcv_addresses.append(transaction['caid'])
                asset_id.append(transaction['caid'])
            else:
                try:
                    snd_addresses.append(transaction['txn']['snd'])
                    rcv_addresses.append(transaction['txn']['caid'])
                    asset_id.append(transaction['txn']['caid'])
                except KeyError:
                    snd_addresses.append(transaction['txn']['snd'])
                    rcv_addresses.append("NA")
                    asset_id.append('NA')

        if type == 'axfer':
            if 'asnd' in transaction['txn']:
                snd_addresses.append(transaction['txn']['snd'])
                rcv_addresses.append(transaction['txn']['asnd'])
                asset_id.append('NA')
            else:
                try:
                    snd_addresses.append(transaction['txn']['snd'])
                    rcv_addresses.append(transaction['txn']['arcv'])
                    asset_id.append(transaction['txn']['xaid'])
                except KeyError:
                    snd_addresses.append(transaction['txn']['snd'])
                    rcv_addresses.append("NA")
                    asset_id.append("NA")

        if type == 'afrz':
            snd_addresses.append(transaction['txn']['snd'])
            rcv_addresses.append(transaction['txn']['fadd'])
            asset_id.append(transaction['txn']['faid'])

        if type == 'appl':
            if 'apid' in transaction:
                snd_addresses.append(transaction['txn']['snd'])
                rcv_addresses.append(transaction['apid'])
                asset_id.append('NA')
            else:
                try:
                    snd_addresses.append(transaction['txn']['snd'])
                    rcv_addresses.append(transaction['txn']['apid'])
                    asset_id.append('NA')
                except KeyError:
                    snd_addresses.append(transaction['txn']['snd'])
                    rcv_addresses.append("NA")
                    asset_id.append('NA')
    notes = []

    for note in txn_note:

        if note != 'NA':
            notes_b = base64.b64decode(note)
            notes.append(notes_b)
        else:
            notes.append(note)
    data = {
        'Sender Address': snd_addresses,
        'Receiver Address': rcv_addresses,
        'Transaction Type': txn_type,
        'Transaction note': notes,
        'Transaction block': txn_block,
        'Transaction Amount': amount,
        'Asset Id': asset_id,
    }
    return data