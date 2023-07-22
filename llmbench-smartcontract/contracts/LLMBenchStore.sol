// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

contract LLMBenchStore {

    address public owner;

    struct ModelData {
        string model;
        string timestamp;
        uint256 mathsolve_accuracy;
        uint256 mathsolve_verbosity;
        uint256 codegen_directly_executable;
        uint256 codegen_verbosity;
        uint256 vizreason_exact_match;
        uint256 vizreason_verbosity;
        uint256 sensitiveq_answer_rate;
        uint256 sensitiveq_verbosity;
    }
    
    mapping(string => mapping(string => ModelData)) public modelData;

    constructor() {
        owner = msg.sender;
    }
    
    function storeModelData(string memory monthYear, string memory modelName, ModelData memory newModelData) public {
        require(msg.sender == owner, "Only the owner can store data.");
        modelData[monthYear][modelName] = newModelData;
    }
    
    function getModelData(string memory monthYear, string memory modelName) public view returns (ModelData memory) {
        return modelData[monthYear][modelName];
    }
}
