import pickle
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_pickle(os.environ["ACTIVITY_DF"] + "activitydf")

activity = df['Total activity'].tolist()
arr_activity = np.array(activity)
print(len(arr_activity))
plt.hist(arr_activity, bins = 15)
plt.show()

