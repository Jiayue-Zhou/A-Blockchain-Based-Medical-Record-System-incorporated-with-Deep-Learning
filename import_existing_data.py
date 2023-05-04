import json
from web3 import Web3
from solcx import compile_standard, install_solc
from transaction import transaction_upload
from process_data import processing_data
from server import train

TEST_URL = "HTTP://127.0.0.1:8545"
MY_ADDRESS = "0xC50F355114394794Be1288544ebC6A3862d737fC"
PRIVATE_KEY = "0xc49c8d008b038509f8c1f5549d3fdd6d996943db03439ca70a599b6425f558a4"
CHAIN_ID = 1337
# load_dotenv()

with open("./patientRecordContract.sol", "r") as file:
    smart_contract_file = file.read()

install_solc("0.8.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"patientRecordContract.sol": {"content": smart_contract_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol["contracts"]["patientRecordContract.sol"]["PatientRecord"]["evm"][
    "bytecode"
]["object"]

abi = json.loads(
    compiled_sol["contracts"]["patientRecordContract.sol"]["PatientRecord"]["metadata"]
)["output"]["abi"]

w3 = Web3(Web3.HTTPProvider(TEST_URL))

MyContract = w3.eth.contract(abi=abi, bytecode=bytecode)

nonce = w3.eth.get_transaction_count(MY_ADDRESS)

transaction = MyContract.constructor().build_transaction(
    {
        "chainId": CHAIN_ID,
        "gasPrice": w3.eth.gas_price,
        "from": MY_ADDRESS,
        "nonce": nonce,
    }
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
print("Deploying Contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")

with open("contractAddress", "w") as f:
    f.write(tx_receipt.contractAddress)

my_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

result = processing_data()

cnt = 1
for pp in result:
    print(f'People with age {pp.features[0]} has been uploaded.({cnt}/{len(result)})')
    transaction_upload(MY_ADDRESS, w3, my_contract, CHAIN_ID, PRIVATE_KEY, pp)
    cnt = cnt + 1


# Train model
train()
