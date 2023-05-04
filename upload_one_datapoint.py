from initialize_my_contract import initialize
from process_data import processing_data
from transaction import transaction_upload


MY_ADDRESS, CHAIN_ID, w3, PRIVATE_KEY, my_contract = initialize()

result = processing_data()

def upload_fun(dp):
    print(f'People with age {dp.features[0]} has been uploaded.')
    password = transaction_upload(MY_ADDRESS, w3, my_contract, CHAIN_ID, PRIVATE_KEY, dp)
    total_num = my_contract.functions.getPeopleRecordTotalNum().call()
    return total_num, password
