import pickle
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import networkx as nx
import os
from dotenv import load_dotenv
load_dotenv()


number_of_blocks = int(os.environ["NUMBER_OF_BLOCKS"])
df = pd.read_pickle(os.environ['SAVE_DF_PATH']+str(number_of_blocks))

G = nx.from_pandas_edgelist(df,'Sender Address', 'Receiver Address')

nx.write_gexf(G,os.environ["SAVE_GEPHI_PATH"] + str(number_of_blocks)+'.gexf')