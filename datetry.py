from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import os
import pickle
dates = []
initial_block_number = 11000000
number_of_blocks = 500
with open(os.environ["SAVE_TXN_PATH"]+"_"+str(initial_block_number)+'_'+str(number_of_blocks), 'rb') as what:
    transactions = pickle.load(what)

for  i,txn in enumerate(transactions):
    print(txn['date'])
    dates.append(txn['date'])
print(len(dates))




# for block in blocks:
#     dates.append(block['block']['ts'])
#     print(block['block']['ts'])
# print(len(dates))

# date = datetime.fromtimestamp(blocks[0]['block']['ts'])
# print(str(date))
# print(str(date)[:10])