from algosdk.v2client import algod
import json
import time
import pickle
import os
from dotenv import load_dotenv
load_dotenv()
from progress.bar import Bar

#round  reference 23.739.705

def GetBlockInfo(client, block_number):
    blocks = []
    bar = Bar('Downloading', max=block_number)
    for i in range(block_number):
        # Retrieve block information                                                                                                                                              
        try:
            block = client.block_info(20000000+i)
        except Exception as e:
            print("Failed to get algod status: {}".format(e))
        blocks.append(block)
        bar.next()
    bar.finish()
    return blocks

algod_address = "https://mainnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": os.environ["PURESTAKE_API"],
}
algod_client = algod.AlgodClient(algod_token, algod_address, headers)
number_of_blocks = int(os.environ["NUMBER_OF_BLOCKS"])
blocks = GetBlockInfo(algod_client,number_of_blocks) #aca cambiando el numerito cambia la cantidad de bloques que bajo

with open(os.environ["SAVE_BLOCK_PATH"]+str(number_of_blocks), 'wb') as what:
    pickle.dump(blocks, what)