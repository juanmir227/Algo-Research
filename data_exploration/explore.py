import pickle
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_pickle('txn_data_frame/txn_dataframe.pickle')
# print(df)
# sb.displot(df, x = 'Transaction Type')
# plt.show()

# txn_type = df['Transaction Type'].tolist()

# print(txn_type)
# types = set(txn_type)
# print(types)
# #sb.displot(txn_type, x=types)
sender = df['Sender Address'].tolist()
receiver = df['Receiver Address'].tolist()

total = sender + receiver



# result = sorted(total, key = total.count, reverse = True)
# resultado = list(set(result))

# #print(resultado[:10])


# a = df['Receiver Address']
# print (a)

new_df = df.groupby(['Receiver Address'])['Sender Address'].count().reset_index(
  name='Count').sort_values(['Count'], ascending=False)

print(new_df.iloc[0,0])

#Highest frequency address ZW3ISEHZUHPO7OZGMKLKIIMKVICOUDRCERI454I3DB2BH52HGLSO67W754 for senders
#Highest frequency address C7RYOGEWDT7HZM3HKPSMU7QGWTRWR3EPOQTJ2OHXGYLARD3X62DNWELS34 for receivers

