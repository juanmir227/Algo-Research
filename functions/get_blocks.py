from algosdk.v2client import algod
import json
import time
import pickle
import os
from dotenv import load_dotenv
load_dotenv()
from progress.bar import Bar

#round  reference 23.739.705

def GetBlockInfo(client,initial_block_number, block_number):
    blocks = []
    bar = Bar('Downloading', max=block_number)
    for i in range(block_number):
        # Retrieve block information                                                                                                                                              
        try:
            block = client.block_info(initial_block_number+i)
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

initial_block_number = int(os.environ["INITIAL_BLOCK_NUMBER"])
number_of_blocks = int(os.environ["NUMBER_OF_BLOCKS"])
blocks = GetBlockInfo(algod_client,initial_block_number,number_of_blocks)

with open(os.environ["SAVE_BLOCK_PATH"]+"_"+str(initial_block_number)+'_'+str(number_of_blocks), 'wb') as what:
    pickle.dump(blocks, what)