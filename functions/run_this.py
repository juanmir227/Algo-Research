from algosdk.v2client import algod
import json
import time
import pickle
import os
from dotenv import load_dotenv
load_dotenv()
from progress.bar import Bar

from get_blocks import GetBlockInfo



algod_address = "https://mainnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": os.environ["PURESTAKE_API"],
}

algod_client = algod.AlgodClient(algod_token, algod_address, headers)

initial_block_number = int(os.environ["INITIAL_BLOCK_NUMBER"])
number_of_blocks = int(os.environ["NUMBER_OF_BLOCKS"])
blocks = GetBlockInfo(algod_client,initial_block_number,number_of_blocks)
