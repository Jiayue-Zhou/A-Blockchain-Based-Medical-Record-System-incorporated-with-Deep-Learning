from initialize_my_contract import initialize
from model import predict
import pandas as pd

from process_data import pre_process_for_model
from aggregation import decode

_, _, _, _, my_contract = initialize()


def take_all_data_from_blockchain():
    result = []
    pp = my_contract.functions.getTotal().call()
    for i in range(len(pp)):
        feats = decode(pp[i][2])
        dig_res = pp[i][1]
        feats.append(dig_res)
        feats_int = list(map(int, feats))
        result.append(feats_int)
    dataset = pre_process_for_model(result)
    print(f'We have {dataset.shape[0]} for current records number.')
    return dataset
    # algo(kk, dp)


def predict_for_datapoint(datapoint):
    print(f'Get the datapoint\n {datapoint}')
    print("Waiting...")

    result = predict(datapoint)
    res_ans = ["Low", "Medium", "High"]
    return res_ans[result]


# For test this function
if __name__ == '__main__':
    dp = pd.read_csv('C:/Users/jiayue/Desktop/dp.csv')
    print(predict_for_datapoint(dp))
