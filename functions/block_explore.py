import pickle
import os
from progress.bar import Bar
from dotenv import load_dotenv
load_dotenv()

with open(os.environ["SAVE_BLOCK_PATH"],'rb') as f:
    data = pickle.load(f)

print(data[1]["block"]["txns"][0]['txn'])