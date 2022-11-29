import pickle
import numpy
from varname import nameof


myvars = locals()


lists = ['created_apps', 'total_transaction_amount', 'total_sender_number', 'total_receiver_number', 'total_active_accounts', 'mean_transaction_amount_per_sender',
'mean_transaction_amount_per_receiver', 'mean_amount_of_unique_receiver_for_sender', 'mean_amount_of_unique_sender_for_receiver', 'only_sender_accounts',
'only_receiver_accounts', 'percent_of_senders_only_senders', 'percent_of_receivers_only_receivers', 'percent_of_accounts_only_senders', 'percent_of_accounts_only_receivers',
'sender_average_transacted_accounts', 'receiver_average_transacted_accounts','sender_average_transacted_with_same_accounts', 'receiver_average_transacted_with_same_accounts',
'most_frequent_ids', 'percentage_of_total_transactions_per_asset', 'unique_senders_per_asset', 'unique_receivers_per_asset', 'unique_accounts_per_asset',
'percentage_of_total_accounts_per_asset', 'transactions_one_algo', 'involved_accounts_per_type', 'involved_senders_per_type', 'involved_receivers_per_type',
'percentage_of_total_accounts_per_type', 'transaction_amount_in_microalgo', 'closing_transactions_count', 'more_than_one_algo',
'more_than_one_algo_percentage', 'mean_amount_of_algo_sent']


for i, listed in enumerate(lists):
    temp = listed + '=' + '1'
    exec(temp)
    with open('/home/juaneto8/Documents/Projects/Algorand/data_acquisition/lists_csv/' + listed, 'rb') as fp:
         listed = pickle.load(fp)
    print(listed)

print(total_transaction_amount)