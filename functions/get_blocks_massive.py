from algosdk.v2client import algod
import json
import time
import pickle
import os
from dotenv import load_dotenv
load_dotenv()

#round  reference 23.739.705

def GetBlockInfo(client, block_number):
    blocks = []
    for i in range(block_number):
        # Retrieve latest block information                                                                                                                                              
        try:
            block = client.block_info(20000000+i)
            #print("Latest block: " + json.dumps(block, indent=2, sort_keys=True))
        except Exception as e:
            print("Failed to get algod status: {}".format(e))
        blocks.append(block)
    return blocks
        
        # with open('new_block_data/block'+str(i)+'.json', 'w', encoding = 'utf-8') as f:
        #      json.dump(block,f,ensure_ascii=False, indent = 4)


algod_address = "https://mainnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": os.environ["PURESTAKE_API"],
}

algod_client = algod.AlgodClient(algod_token, algod_address, headers)



# blocks = GetBlockInfo(algod_client,100)

# with open(os.environ["SAVE_BLOCK_PATH"], 'wb') as what:
#     pickle.dump(blocks, what)