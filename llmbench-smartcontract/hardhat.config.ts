import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import * as dotenv from 'dotenv';
dotenv.config();

//https://hardhat.org/hardhat-runner/docs/config#json-rpc-based-networks

//Note: keep your mnemonic and private keys securely
//Read more: https://hardhat.org/hardhat-runner/docs/config#hd-wallet-config
//1) You can configure private keys or mnemonic:
//let accounts = ["your private key here"]
let accounts = { mnemonic: process.env.MNEMONIC, }

const config: HardhatUserConfig = {
  solidity: "0.8.17",
  //2) select the default network "gnosis" or "chiado"npx hardhat run scripts/deploy.ts --network chiado
  defaultNetwork: "gnosis",
  networks: {
    hardhat: {
    },
    gnosis: {
      url: "https://rpc.gnosischain.com",
      accounts: accounts,
    },
    chiado: {
      url: "https://rpc.chiadochain.net",
      gasPrice: 1000000000,
      accounts: accounts,
    },
  },
  etherscan: {
    customChains: [
      {
        network: "chiado",
        chainId: 10200,
        urls: {
          //Blockscout
          apiURL: "https://blockscout.com/gnosis/chiado/api",
          browserURL: "https://blockscout.com/gnosis/chiado",
        },
      },
      {
        network: "gnosis",
        chainId: 100,
        urls: {
          // 3) Select to what explorer verify the contracts
          // Gnosisscan
          apiURL: "https://api.gnosisscan.io/api",
          browserURL: "https://gnosisscan.io/",
          // Blockscout
          //apiURL: "https://blockscout.com/xdai/mainnet/api",
          //browserURL: "https://blockscout.com/xdai/mainnet",
        },
      },
    ],
    apiKey: {
      //4) Insert your Gnosisscan API key
      //blockscout explorer verification does not require keys
      chiado: process.env.CHIADO_API_KEY || "",
      gnosis: process.env.GNOSIS_API_KEY || "",
    },
  }
};

export default config;
