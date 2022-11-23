from algosdk.v2client import algod
import pickle
import os
from dotenv import load_dotenv
load_dotenv()
from get_blocks import GetBlockInfo
from acquire_txns import join_txns
from txns_dataframe import make_df
import pandas as pd
import networkx as nx

## La idea es runearlo varias veces e iterar sobre distintos valores iniciles de bloque para tener varios de estos chunks y
## de esa manera poder comparar como van cambiando las estadisticas a medida que avanza el tiempo


### Genero el cliente para descargar los bloques
algod_address = "https://mainnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": os.environ["PURESTAKE_API"],
}

algod_client = algod.AlgodClient(algod_token, algod_address, headers)
###


#defino bloque inicial y cuantos bloques quiero descargar
# 9 millones es el bloque minimo para arrancar, antes de eso no funciona, se ve que estructuraban los bloques diferente
# o todavia no habia transacciones, no se la verdad.

initial_number = 24000000
number_of_blocks = 500
#genero chunk de 5 bloques cada 1 millon de bloques
while initial_number <= 24000000:
    initial_block_number = initial_number
    initial_number = initial_number + 1000000
    #descargo los bloques y los guardo
    blocks = GetBlockInfo(algod_client,initial_block_number,number_of_blocks)
    with open(os.environ["SAVE_BLOCK_PATH"]+"_"+str(initial_block_number)+'_'+str(number_of_blocks), 'wb') as what:
        pickle.dump(blocks, what)

    #genero toda la lista de transacciones y las guardo
    transacciones = join_txns(blocks)
    with open(os.environ["SAVE_TXN_PATH"]+"_"+str(initial_block_number)+"_"+str(number_of_blocks), 'wb') as fp:
        pickle.dump(transacciones, fp)

    #genero el dataframe y lo guardo
    data = make_df(transacciones)
    df = pd.DataFrame(data)
    df.to_pickle(os.environ['SAVE_DF_PATH']+"_"+str(initial_block_number)+"_"+str(number_of_blocks))

    #genero el gephi y lo guardo
    G = nx.from_pandas_edgelist(df,'Sender Address', 'Receiver Address')
    nx.write_gexf(G,os.environ["SAVE_GEPHI_PATH"]+"_"+str(initial_block_number)+"_" + str(number_of_blocks)+'.gexf')