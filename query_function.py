from aggregation import decode
from initialize_my_contract import initialize

_, _, _, _, my_contract = initialize()


def query_for_one_record(pw):
    pp = my_contract.functions.getDataByPassword(pw).call()
    print(pp)
    feats = decode(pp[2])
    covid_res = pp[1]
    feats.insert(1, covid_res)
    print(feats)
    return feats
