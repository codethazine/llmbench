// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

contract LLMBenchStore {
    
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
    
    function storeModelData(string memory monthYear, string memory modelName, ModelData memory newModelData) public {
        modelData[monthYear][modelName] = newModelData;
    }
    
    function getModelData(string memory monthYear, string memory modelName) public view returns (ModelData memory) {
        return modelData[monthYear][modelName];
    }
}
