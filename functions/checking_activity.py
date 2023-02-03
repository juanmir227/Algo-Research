import pandas as pd
import numpy as np
import pickle
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime

number_of_blocks = 500
initial_block_number = 9000000

# with open(os.environ["SAVE_DF_PATH"] + "_" + str(initial_block_number) + "_" + str(number_of_blocks) + "_filtered") as fp:
#     df = pickle.load(fp)

df_9M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(9000000) + "_" + str(number_of_blocks) + "_filtered")
df_10M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(10000000) + "_" + str(number_of_blocks) + "_filtered")
df_11M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(11000000) + "_" + str(number_of_blocks) + "_filtered")
df_12M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(12000000) + "_" + str(number_of_blocks) + "_filtered")
df_13M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(13000000) + "_" + str(number_of_blocks) + "_filtered")
df_14M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(14000000) + "_" + str(number_of_blocks) + "_filtered")
df_15M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(15000000) + "_" + str(number_of_blocks) + "_filtered")
df_16M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(16000000) + "_" + str(number_of_blocks) + "_filtered")
df_17M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(17000000) + "_" + str(number_of_blocks) + "_filtered")
df_18M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(18000000) + "_" + str(number_of_blocks) + "_filtered")
df_19M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(19000000) + "_" + str(number_of_blocks) + "_filtered")
df_20M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(20000000) + "_" + str(number_of_blocks) + "_filtered")
df_21M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(21000000) + "_" + str(number_of_blocks) + "_filtered")
df_22M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(22000000) + "_" + str(number_of_blocks) + "_filtered")
df_23M = pd.read_pickle(os.environ["SAVE_DF_PATH"] + "_" + str(23000000) + "_" + str(number_of_blocks) + "_filtered")

address = []

df_merged = pd.concat([df_9M, df_10M, df_11M, df_12M, df_13M, df_14M, df_15M, df_16M, df_17M, df_18M, df_19M, df_20M, df_21M, df_22M, df_23M])

senders = df_merged['Sender Address'].tolist()
receivers = df_merged['Receiver Address'].tolist()

total_addresses = senders + receivers
unique_accounts = list(set(total_addresses))

total = []
chunk1 = []
chunk2 = []
chunk3 = []
chunk4 = []
chunk5 = []
chunk6 = []
chunk7 = []
chunk8 = []
chunk9 = []
chunk10 = []
chunk11 = []
chunk12 = []
chunk13 = []
chunk14 = []
chunk15 = []

for account in unique_accounts:
    check0 = account in df_9M['Sender Address'].tolist() or account in df_9M['Receiver Address'].tolist()
    check1 = account in df_10M['Sender Address'].tolist() or account in df_10M['Receiver Address'].tolist()
    check2 = account in df_11M['Sender Address'].tolist() or account in df_11M['Receiver Address'].tolist()
    check3 = account in df_12M['Sender Address'].tolist() or account in df_12M['Receiver Address'].tolist()
    check4 = account in df_13M['Sender Address'].tolist() or account in df_13M['Receiver Address'].tolist()
    check5 = account in df_14M['Sender Address'].tolist() or account in df_14M['Receiver Address'].tolist()
    check6 = account in df_15M['Sender Address'].tolist() or account in df_15M['Receiver Address'].tolist()
    check7 = account in df_16M['Sender Address'].tolist() or account in df_16M['Receiver Address'].tolist()
    check8 = account in df_17M['Sender Address'].tolist() or account in df_17M['Receiver Address'].tolist()
    check9 = account in df_18M['Sender Address'].tolist() or account in df_18M['Receiver Address'].tolist()
    check10 = account in df_19M['Sender Address'].tolist() or account in df_19M['Receiver Address'].tolist()
    check11 = account in df_20M['Sender Address'].tolist() or account in df_20M['Receiver Address'].tolist()
    check12 = account in df_21M['Sender Address'].tolist() or account in df_21M['Receiver Address'].tolist()
    check13 = account in df_22M['Sender Address'].tolist() or account in df_22M['Receiver Address'].tolist()
    check14 = account in df_23M['Sender Address'].tolist() or account in df_23M['Receiver Address'].tolist()
    
    chunk1.append(check0)
    chunk2.append(check1)
    chunk3.append(check2)
    chunk4.append(check3)
    chunk5.append(check4)
    chunk6.append(check5)
    chunk7.append(check6)
    chunk8.append(check7)
    chunk9.append(check8)
    chunk10.append(check9)
    chunk11.append(check10)
    chunk12.append(check11)
    chunk13.append(check12)
    chunk14.append(check13)
    chunk15.append(check14)
    sum = check0 + check1 + check2 + check3 + check4 + check5 + check6 + check7+ check8+ check9+check10+check11+check12+check13+check14
    total.append(sum)


conexions_df = pd.DataFrame(data = {
        'Address' : unique_accounts,
        'Chunk 1' : chunk1,
        'Chunk 2' : chunk2,
        'Chunk 3' : chunk3,
        'Chunk 4' : chunk4,
        'Chunk 5' : chunk5,
        'Chunk 6' : chunk6,
        'Chunk 7' : chunk7,
        'Chunk 8' : chunk8,
        'Chunk 9' : chunk9,
        'Chunk 10' : chunk10,
        'Chunk 11' : chunk11,
        'Chunk 12' : chunk12,
        'Chunk 13' : chunk13,
        'Chunk 14' : chunk14,
        'Total activity' : total,
            })

print(conexions_df)
print(len(unique_accounts))

conexions_df.to_pickle(os.environ["ACTIVITY_DF"] + "activitydf")