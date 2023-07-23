import { ethers, run } from "hardhat";
import { ModelData, LLMBenchStore } from "../typechain/LLMBenchStore";
import fs from "fs";
import path from "path";

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Interacting with contracts with the account:", deployer.address);

  // The address we're connecting to.
  const CONTRACT_ADDRESS = "0x1898727d6a5a787C5Ed00596fA9740029c7C9494";

  const Contract = await ethers.getContractFactory("LLMBenchStore");
  const contract = Contract.attach(CONTRACT_ADDRESS) as LLMBenchStore;

  const jsonData = fs.readFileSync(
    path.resolve(__dirname, "../assets/total_hist_eval.json"),
    "utf-8"
  );

  const data = JSON.parse(jsonData);

  for (const monthYear of Object.keys(data)) {
    for (const modelName of Object.keys(data[monthYear])) {
      const modelData = data[monthYear][modelName];

      const modelDataToInsert: ModelData = {
        model: modelData.model,
        timestamp: modelData.timestamp,
        mathsolve_accuracy: ethers.utils.parseUnits(modelData.mathsolve_accuracy.toFixed(18), 'wei').toString(),
        mathsolve_verbosity: ethers.BigNumber.from(Math.floor(modelData.mathsolve_verbosity).toString()).toString(),
        codegen_directly_executable: ethers.utils.parseUnits(modelData.codegen_directly_executable.toFixed(18), 'wei').toString(),
        codegen_verbosity: ethers.BigNumber.from(Math.floor(modelData.codegen_verbosity).toString()).toString(),
        vizreason_exact_match: ethers.utils.parseUnits(modelData.vizreason_exact_match.toFixed(18), 'wei').toString(),
        vizreason_verbosity: ethers.BigNumber.from(Math.floor(modelData.vizreason_verbosity).toString()).toString(),
        sensitiveq_answer_rate: ethers.utils.parseUnits(modelData.sensitiveq_answer_rate.toFixed(18), 'wei').toString(),
        sensitiveq_verbosity: ethers.BigNumber.from(Math.floor(modelData.sensitiveq_verbosity).toString()).toString(),
      };

      await contract.storeModelData(monthYear, modelName, modelDataToInsert);
    }
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
