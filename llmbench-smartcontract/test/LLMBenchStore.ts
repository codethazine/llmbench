import { expect } from "chai";
import { ethers } from "hardhat";

describe("LLMBenchStore", function () {
  it("Should store and retrieve model data correctly", async function () {
    // Deploying the contract
    const LLMBenchStore = await ethers.getContractFactory("LLMBenchStore");
    const llmBenchStore = await LLMBenchStore.deploy();
    await llmBenchStore.deployed();

    // Prepare test data
    const monthYear = "July2023";
    const modelName = "Model1";

    const newModelData = {
      model: "model",
      timestamp: "timestamp",
      mathsolve_accuracy: 10,
      mathsolve_verbosity: 10,
      codegen_directly_executable: 10,
      codegen_verbosity: 10,
      vizreason_exact_match: 10,
      vizreason_verbosity: 10,
      sensitiveq_answer_rate: 10,
      sensitiveq_verbosity: 10
    };

    // Call the contract function
    await llmBenchStore.storeModelData(monthYear, modelName, newModelData);

    // Retrieve the data and test
    const retrievedModelData = await llmBenchStore.getModelData(monthYear, modelName);

    // Since solidity can't return a struct containing a string in an external function,
    // we have to manually get each field and compare. If you have a public variable
    // of struct type, you can use that instead.
    expect(retrievedModelData.model).to.equal(newModelData.model);
    expect(retrievedModelData.timestamp).to.equal(newModelData.timestamp);
    expect(retrievedModelData.mathsolve_accuracy).to.equal(newModelData.mathsolve_accuracy);
    expect(retrievedModelData.mathsolve_verbosity).to.equal(newModelData.mathsolve_verbosity);
    expect(retrievedModelData.codegen_directly_executable).to.equal(newModelData.codegen_directly_executable);
    expect(retrievedModelData.codegen_verbosity).to.equal(newModelData.codegen_verbosity);
    expect(retrievedModelData.vizreason_exact_match).to.equal(newModelData.vizreason_exact_match);
    expect(retrievedModelData.vizreason_verbosity).to.equal(newModelData.vizreason_verbosity);
    expect(retrievedModelData.sensitiveq_answer_rate).to.equal(newModelData.sensitiveq_answer_rate);
    expect(retrievedModelData.sensitiveq_verbosity).to.equal(newModelData.sensitiveq_verbosity);
  });
});
