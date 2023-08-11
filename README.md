<h2>A Patients Medical Records System</h2>



<h3>Building the application</h3>
I recommend to use **Ganache** for testing the smart contract. Once built
your personal blockchain, you should replace the TEST_URL 
, MY_ADDRESS, PRIVATE_KEY in the initialize_my_contract.py.
You should also change the import_existing_data.py for importing
existing data and deploying the smart contract to the blockchain.

Now the smart contract is on your blockchain! You will find that 
the BALANCE of your chosen account is deducted. That is because
deploying contracts cost some gas fee. 

You can check all that information in Ganache.

Then you can run server.py to run the back-end
and use npm to run the front-end. Once running the website,
you are also able to monitor the status of accounts by
**Metamask**.





<h3>Back-End</h3>
I use **Flask** to build the back-end and **Solidity** to build the
smart contract. 
patientRecordContract.sol is the Solidity file, and I use aggregation.py
to aggregation all features together for better store on blockchain.

contractAddress is a file that stores the smart contract address.
model.py is a machine learning model that gets the whole dataset from
the blockchain and predict one given datapoint to positive or negative.
In our dataset, we predict if one is positive or negative 
for covid-19. 
With the number of data increasing by uploading from doctors, the machine learning model
is also supposed to have more data to train itself.

<h3>Front-end</h3>
I use **Vue.js** for the front-end. I have two views for patients and doctors.
The front-end is responsible for users to enter data and interact with the back-end
to get the information from the blockchain or the machine learning model.

Use doctors' portal, you can query a data from the blockchain by a private code(password).
It is a 16 bits integer and will be rendered randomly once the data is uploaded to
the blockchain. Also, as doctors, they are able to upload and store data to the blockchain
while patients can only enter a datapoint and get a predicted result.
(The datapoint entered by the patient will not be stored on the blockchain)



![image](https://github.com/Jiayue-Zhou/Patients-Medical-Records-System/blob/master/image_for_introduction/introduction_gif.gif)
