from algosdk.v2client import algod
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()

def GetBlockInfo(client):
    for i in range(10):

        try:
            status = client.status()
            #print("Status: " + json.dumps(status, indent=2, sort_keys=True))
        except Exception as e:
            print("Failed to get algod status: {}".format(e))

        # Retrieve latest block information                                                                                                                                               
        last_round = status.get("last-round")
        #print(last_round)
        try:
            block = client.block_info(last_round)
            print("Latest block: " + json.dumps(block, indent=2, sort_keys=True))
        except Exception as e:
            print("Failed to get algod status: {}".format(e))
        
        with open('block_data/block'+str(i)+'.json', 'w', encoding = 'utf-8') as f:
            json.dump(block,f,ensure_ascii=False, indent = 4)
        time.sleep(10)



algod_address = "https://mainnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": os.environ["PURESTAKE_API"],
}

algod_client = algod.AlgodClient(algod_token, algod_address, headers)

GetBlockInfo(algod_client)