import { ethers } from "hardhat";

async function main() {
  const llmbenchstore = await ethers.deployContract("LLMBenchStore")
  await llmbenchstore.waitForDeployment();
  console.log("LLMBenchStore deployed to:", await llmbenchstore.getAddress());
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
