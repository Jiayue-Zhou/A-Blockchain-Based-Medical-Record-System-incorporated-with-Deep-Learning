import json
from web3 import Web3
from solcx import compile_standard, install_solc, get_installable_solc_versions


def initialize():
    TEST_URL = "HTTP://127.0.0.1:8545"
    MY_ADDRESS = "0xC50F355114394794Be1288544ebC6A3862d737fC"
    PRIVATE_KEY = "0xc49c8d008b038509f8c1f5549d3fdd6d996943db03439ca70a599b6425f558a4"
    CHAIN_ID = 1337
    # load_dotenv()

    with open("contractAddress", "r") as f:
        CONTRACT_ADDRESS = f.readline()

    print(f'Smart Contract Address is {CONTRACT_ADDRESS}')

    # CONTRACT_ADDRESS = "0x5E42C3942729A715FC1C564ee35B32bEfAf82627"

    with open("./patientRecordContract.sol", "r") as file:
        my_file = file.read()

    # print("The lastest version of solc is ")
    # print(get_installable_solc_versions())

    install_solc("0.8.0");

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"patientRecordContract.sol": {"content": my_file}},
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                    }
                }
            },
        },
    )
    abi = json.loads(
        compiled_sol["contracts"]["patientRecordContract.sol"]["PatientRecord"]["metadata"]
    )["output"]["abi"]

    w3 = Web3(Web3.HTTPProvider(TEST_URL, request_kwargs={'timeout': 60}))

    my_contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

    return MY_ADDRESS, CHAIN_ID, w3, PRIVATE_KEY, my_contract
