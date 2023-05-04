pragma solidity >=0.8.0 < 0.9.0;
//pragma experimental ABIEncoderV2

contract PatientRecord {

    uint256 privatePasswordDigits = 16;
    uint256 passwordModulus = 10 ** privatePasswordDigits;
    uint256 index = 0;
    uint256 tempPasswordStore = 0;

    struct People {
        uint256 id;
        uint8 diagnostic_Res;
        string aggregation;
    }

    People[] public people;
    mapping(uint256 => People) public idToPeople;
    mapping(uint256 => People) public privatePasswordToPeople;

    function helloWorld() external pure returns(string memory) {
        return "Hello World! This smart contract is writen by Jiayue Zhou.";
    }

    // Use sender address, current time, current index, and the aggregation to generate a 16 bits integer
    // random password
    function _generateRandomPrivatePassword(string memory _str) internal view returns (uint256) {
        uint256 rand = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp, index, _str)));
        return rand % passwordModulus;
    }

    // Upload a datapoint
    function storeData(uint8 diagnostic_Res, string memory aggregation)
    external {

        People memory newPeople = People(index, diagnostic_Res, aggregation);

        people.push(newPeople);
        idToPeople[index] = newPeople;

        uint256 password = _generateRandomPrivatePassword(aggregation);
        privatePasswordToPeople[password] = newPeople;
        tempPasswordStore = password;

        index++;
    }

    function getPassword() external returns(uint256){
        uint256 temp = tempPasswordStore;
        // Burn(Delete) after reading
        tempPasswordStore = 0;
        return temp;
    }

    function getData(uint256 id) external view returns(string memory) {
        return idToPeople[id].aggregation;
    }

    function getDataByPassword(uint256 pw) external view returns(People memory) {
        return privatePasswordToPeople[pw];
    }

    function getCovidResult(uint256 id) internal view returns(uint8) {
        return idToPeople[id].diagnostic_Res;
    }

    function getCovidResultByPassword(uint256 pw) external view returns(uint8) {
        return privatePasswordToPeople[pw].diagnostic_Res;
    }

    function getPeopleRecordNum(uint256 pw) internal view returns(uint256) {
        return privatePasswordToPeople[pw].id;
    }
    function getPeopleRecordTotalNum() external view returns(uint256) {
        return index;
    }
    function getTotal() external view returns(People[] memory) {
        return people;
    }
}