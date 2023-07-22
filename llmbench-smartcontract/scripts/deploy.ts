import { ethers, run } from 'hardhat';

async function main() {
  // get the deployer signers
  const [deployer] = await ethers.getSigners();

  console.log(
    'Deploying contracts with the account:',
    deployer.address
  );

  // Get provider from ethers
  const provider = ethers.provider;

  console.log('Account balance:', (await provider.getBalance(deployer.address)).toString());

  // Get the Contract Factory
  const LLMBenchStore = await ethers.getContractFactory('LLMBenchStore');
  
  // Deploy the contract
  const llmbenchstore = await LLMBenchStore.deploy();

  console.log('LLMBenchStore address:', llmbenchstore.address);

  // Wait for the contract to be mined
  await llmbenchstore.deployed();

  console.log('LLMBenchStore deployed to:', llmbenchstore.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
