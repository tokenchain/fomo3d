const HDWalletProvider = require("truffle-hdwallet-provider");
const mnemonic =  'mother citizen apart father resemble coral section pony floor brother fuel lottery';

module.exports = {
    networks: {
        development: {
            host: "127.0.0.1",
            port: 8545,
            gas: 9000000,
            network_id: "*" // Match any network id
        },
        // kovan: {
        //     gasPrice: 5000000000,
        //     provider: function() {
        //         return new HDWalletProvider(mnemonic,
        //             "https://kovan.infura.io/v3/314aa8d6c0f4433b8f5c43c3c7e5c1e4")
        //     },
        //     network_id: 3
        // },
        // ropsten: {
        //    // gas: 8000000,
        //     gasPrice: 8000000000,
        //     provider: function() {
        //         return new HDWalletProvider(mnemonic,
        //             "https://ropsten.infura.io/v3/314aa8d6c0f4433b8f5c43c3c7e5c1e4")
        //     },
        //     network_id: 2
        // },
        // rinkeby : {
        //     gasPrice: 8000000000,
        //     provider: function() {
        //         return new HDWalletProvider(mnemonic,
        //             "https://ropsten.infura.io/v3/314aa8d6c0f4433b8f5c43c3c7e5c1e4")
        //     },
        //     network_id: 4
        // },
        // mainnet: {
        //     gas: 7500000,
        //     gasPrice: 6000000000,
        //     provider: function() {
        //         return new HDWalletProvider(mnemonic,
        //             "https://mainnet.infura.io/v3/314aa8d6c0f4433b8f5c43c3c7e5c1e4")
        //     },
        //     network_id: 1
        // }
        // dev: {
        //     // gasPrice: 8000000000,
        //     provider: function() {
        //         return new HDWalletProvider(mnemonic, "http://127.0.0.1:8545")
        //     },
        //     // network_id: 0x539
        // }
    },
    compilers:{
        solc: {
            version: "0.4.24",
            parser: "solcjs",
            // optimizer: {
            //     enabled: true,
            //     runs: 200
            // },
            settings: {
                optimizer: {
                  enabled: true,
                  runs: 20  // Optimize for how many times you intend to run the code
                }
            },
        }
    }
    
};