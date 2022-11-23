import os
import pickle
from functions.txns_dataframe import make_df
import pandas as pd
from datetime import datetime

initial_block_number = 20000000
number_of_blocks = 500
with open(os.environ["SAVE_TXN_PATH"]+"_"+str(initial_block_number)+"_"+str(number_of_blocks), 'rb') as fp:
    transacciones = pickle.load(fp)

#genero el dataframe y lo guardo
# data = make_df(transacciones)
# df = pd.DataFrame(data)
# df.to_pickle(os.environ['SAVE_DF_PATH']+"_"+str(initial_block_number)+"_"+str(number_of_blocks))
print(transacciones[0])