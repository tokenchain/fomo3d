/* DO NOT EDIT THE BELOW FILE AS THIS IS LIKELY WILL BE GENERATED AGAIN AND REWRITE OVER IT */

// tslint:disable:no-consecutive-blank-lines ordered-imports align trailing-comma enum-naming
// tslint:disable:whitespace no-unbound-method no-trailing-whitespace
// tslint:disable:no-unused-variable

import * as ethers from "ethers"
// eslint-disable-next-line import/named
import {
  assert,
  schemas,
  // eslint-disable-next-line import/named
  SubscriptionManager,
  // eslint-disable-next-line import/named
  BaseContract,
  // eslint-disable-next-line import/named
  EventCallback,
  // eslint-disable-next-line import/named
  IndexedFilterValues,
  // eslint-disable-next-line import/named
  BlockRange,
  // eslint-disable-next-line import/named
  DecodedLogArgs,
  // eslint-disable-next-line import/named
  LogWithDecodedArgs,
  // eslint-disable-next-line import/named
  MethodAbi
} from "vue-blocklink"

import {
  BatchRequest,
  Extension,
  Log,
  PromiEvent,
  provider,
  Providers,
  RLPEncodedTransaction,
  Transaction,
  TransactionConfig,
  TransactionReceipt,
  Common,
  hardfork,
  chain,
  BlockNumber,
  LogsOptions,
  PastLogsOptions
} from "web3-core"

import { Utils, AbiItem } from "web3-utils"
import Web3 from "web3"
import BN from "BN.js"

// tslint:enable:no-unused-variable
export interface ContractInterface {
    CLAIM_TRANSACTION_TYPEHASH():Promise<string>
    DOMAIN_SEPARATOR():Promise<string>
    EIP712_DOMAIN_TYPEHASH():Promise<string>
    VAULTBUY_TRANSACTION_TYPEHASH():Promise<string>
    bnbBuy(_buy_num: BN,_team: number|BN,_rounds: BN,coin: BN):Promise<void>
    claim(_account: string,_number: BN,nonce: BN,v: number|BN,r: string,s: string,):Promise<void>
    end_time(index_0: BN,):Promise<BN>
    key_final_price():Promise<BN>
    key_increasing_price():Promise<BN>
    key_init_price():Promise<BN>
    nonceOf(account: string,):Promise<BN>
    owner():Promise<string>
    rounds():Promise<BN>
    setActionTime(_time: BN,):Promise<void>
    start_time(index_0: BN,):Promise<BN>
    team(index_0: string,index_1: BN,):Promise<BN>
    vaultBuy(_buy_num: BN,_team: number|BN,_rounds: BN,_account: string,nonce: BN,v: number|BN,r: string,s: string,coin: BN):Promise<void>
}





export enum fomo3dEvents {
    BnbBuy = 'BnbBuy',
    Claim = 'Claim',
    VaultBuy = 'VaultBuy',
}

export interface fomo3dBnbBuyEventArgs extends DecodedLogArgs {
    account: string;
    bnbvalue: BN;
    buy_num: BN;
    team: BN;
    rounds: BN;
}

export interface fomo3dClaimEventArgs extends DecodedLogArgs {
    account: string;
    claimvalue: BN;
}

export interface fomo3dVaultBuyEventArgs extends DecodedLogArgs {
    account: string;
    vaultvalue: BN;
    buy_num: BN;
    team: BN;
    rounds: BN;
}


export type fomo3dEventArgs =
    | fomo3dBnbBuyEventArgs
    | fomo3dClaimEventArgs
    | fomo3dVaultBuyEventArgs;




/* istanbul ignore next */
// tslint:disable:array-type
// tslint:disable:no-parameter-reassignment
// tslint:disable-next-line:class-name
export class fomo3dContract extends BaseContract implements ContractInterface{
    /**
     * @ignore
     */
public static deployedBytecode: string | undefined;
public static readonly contractName = 'fomo3d';
    private readonly _methodABIIndex: { [name: string]: number } = {};
    //todo: we will come back and fix it later not generic Error @https://www.typescriptlang.org/docs/handbook/2/conditional-types.html
    // @ts-ignore
    private readonly _subscriptionManager: SubscriptionManager<fomo3dEventArgs, fomo3dEvents>;


    public static Instance(): (fomo3dContract | any | boolean) {
        if (window && window.hasOwnProperty("__eth_contract_fomo3d")) {
          // @ts-ignore
          const obj = window.__eth_contract_fomo3d
          if (obj instanceof fomo3dContract) {
            return (obj) as fomo3dContract
          } else {
            return (obj) as fomo3dContract
          }
        } else {
          return false
        }
    }

    static async init(
        contract_address: string,
        supportedProvider: provider,
        ww3: Web3
        ):Promise<fomo3dContract>
    {
        const contractInstance = await new fomo3dContract(
            contract_address,
            supportedProvider,
            ww3
        );

        contractInstance.constructorArgs = [/** "_owner"
 **/];

        if (window && !window.hasOwnProperty("__eth_contract_fomo3d")) {
            // @ts-ignore
            window.__eth_contract_fomo3d = contractInstance
        }

        return contractInstance
    }

    /**
     * @returns The contract ABI
     */
    public static ABI(): AbiItem[] {
        const abi = [
            { 
                inputs: [
                    {
                        name: '_owner',
                        type: 'address',
                    },
                ],
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'constructor',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'account',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'bnbvalue',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'buy_num',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'team',
                        type: 'uint8',
                        indexed: false,
                    },
                    {
                        name: 'rounds',
                        type: 'uint256',
                        indexed: false,
                    },
                ],
                name: 'BnbBuy',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'account',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'claimvalue',
                        type: 'uint256',
                        indexed: false,
                    },
                ],
                name: 'Claim',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'account',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'vaultvalue',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'buy_num',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'team',
                        type: 'uint8',
                        indexed: false,
                    },
                    {
                        name: 'rounds',
                        type: 'uint256',
                        indexed: false,
                    },
                ],
                name: 'VaultBuy',
                outputs: [
                ],
                type: 'event',
            },
            { 
                inputs: [
                ],
                name: 'CLAIM_TRANSACTION_TYPEHASH',
                outputs: [
                    {
                        name: '',
                        type: 'bytes32',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'DOMAIN_SEPARATOR',
                outputs: [
                    {
                        name: '',
                        type: 'bytes32',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'EIP712_DOMAIN_TYPEHASH',
                outputs: [
                    {
                        name: '',
                        type: 'bytes32',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'VAULTBUY_TRANSACTION_TYPEHASH',
                outputs: [
                    {
                        name: '',
                        type: 'bytes32',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: '_buy_num',
                        type: 'uint256',
                    },
                    {
                        name: '_team',
                        type: 'uint8',
                    },
                    {
                        name: '_rounds',
                        type: 'uint64',
                    },
                ],
                name: 'bnbBuy',
                outputs: [
                ],
                stateMutability: 'payable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: '_account',
                        type: 'address',
                    },
                    {
                        name: '_number',
                        type: 'uint256',
                    },
                    {
                        name: 'nonce',
                        type: 'uint256',
                    },
                    {
                        name: 'v',
                        type: 'uint8',
                    },
                    {
                        name: 'r',
                        type: 'bytes32',
                    },
                    {
                        name: 's',
                        type: 'bytes32',
                    },
                ],
                name: 'claim',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'index_0',
                        type: 'uint256',
                    },
                ],
                name: 'end_time',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'key_final_price',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'key_increasing_price',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'key_init_price',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'account',
                        type: 'address',
                    },
                ],
                name: 'nonceOf',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'owner',
                outputs: [
                    {
                        name: '',
                        type: 'address',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'rounds',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: '_time',
                        type: 'uint256',
                    },
                ],
                name: 'setActionTime',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'index_0',
                        type: 'uint256',
                    },
                ],
                name: 'start_time',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'index_0',
                        type: 'address',
                    },
                    {
                        name: 'index_1',
                        type: 'uint256',
                    },
                ],
                name: 'team',
                outputs: [
                    {
                        name: '',
                        type: 'uint8',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: '_buy_num',
                        type: 'uint256',
                    },
                    {
                        name: '_team',
                        type: 'uint8',
                    },
                    {
                        name: '_rounds',
                        type: 'uint256',
                    },
                    {
                        name: '_account',
                        type: 'address',
                    },
                    {
                        name: 'nonce',
                        type: 'uint256',
                    },
                    {
                        name: 'v',
                        type: 'uint8',
                    },
                    {
                        name: 'r',
                        type: 'bytes32',
                    },
                    {
                        name: 's',
                        type: 'bytes32',
                    },
                ],
                name: 'vaultBuy',
                outputs: [
                ],
                stateMutability: 'payable',
                type: 'function',
            },
        ] as AbiItem[];
        return abi;
    }

    /**
     the listed content for the contract functions
    **/

    public async CLAIM_TRANSACTION_TYPEHASH(): Promise<string> {
        const self = this as any as fomo3dContract;


        const promizz = self._contract.methods.CLAIM_TRANSACTION_TYPEHASH(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async CLAIM_TRANSACTION_TYPEHASHGas(): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.CLAIM_TRANSACTION_TYPEHASH().estimateGas();
        return gasAmount;
    };


    public async DOMAIN_SEPARATOR(): Promise<string> {
        const self = this as any as fomo3dContract;


        const promizz = self._contract.methods.DOMAIN_SEPARATOR(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async DOMAIN_SEPARATORGas(): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.DOMAIN_SEPARATOR().estimateGas();
        return gasAmount;
    };


    public async EIP712_DOMAIN_TYPEHASH(): Promise<string> {
        const self = this as any as fomo3dContract;


        const promizz = self._contract.methods.EIP712_DOMAIN_TYPEHASH(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async EIP712_DOMAIN_TYPEHASHGas(): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.EIP712_DOMAIN_TYPEHASH().estimateGas();
        return gasAmount;
    };


    public async VAULTBUY_TRANSACTION_TYPEHASH(): Promise<string> {
        const self = this as any as fomo3dContract;


        const promizz = self._contract.methods.VAULTBUY_TRANSACTION_TYPEHASH(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async VAULTBUY_TRANSACTION_TYPEHASHGas(): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.VAULTBUY_TRANSACTION_TYPEHASH().estimateGas();
        return gasAmount;
    };


    public async bnbBuy(_buy_num: BN,_team: number|BN,_rounds: BN,valCoin: BN): Promise<void> {
        const self = this as any as fomo3dContract;

            assert.isNumberOrBigNumber('_buy_num', _buy_num);
            assert.isNumberOrBigNumber('_team', _team);
            assert.isBigNumber('_rounds', _rounds);

        const promizz = self._contract.methods.bnbBuy(
            _buy_num,
                    _team,
                    _rounds,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice, value: valCoin
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async bnbBuyGas(_buy_num: BN,_team: number|BN,_rounds: BN,): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.bnbBuy(_buy_num,_team,_rounds,).estimateGas();
        return gasAmount;
    };


    public async claim(_account: string,_number: BN,nonce: BN,v: number|BN,r: string,s: string,): Promise<void> {
        const self = this as any as fomo3dContract;

            assert.isString('_account', _account);
            assert.isNumberOrBigNumber('_number', _number);
            assert.isNumberOrBigNumber('nonce', nonce);
            assert.isNumberOrBigNumber('v', v);
            assert.isString('r', r);
            assert.isString('s', s);

        const promizz = self._contract.methods.claim(
            _account,
                    _number,
                    nonce,
                    v,
                    r,
                    s,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async claimGas(_account: string,_number: BN,nonce: BN,v: number|BN,r: string,s: string,): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.claim(_account,_number,nonce,v,r,s,).estimateGas();
        return gasAmount;
    };


    public async end_time(index_0: BN,): Promise<BN> {
        const self = this as any as fomo3dContract;

            assert.isNumberOrBigNumber('index_0', index_0);

        const promizz = self._contract.methods.end_time(
            index_0,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async end_timeGas(index_0: BN,): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.end_time(index_0,).estimateGas();
        return gasAmount;
    };


    public async key_final_price(): Promise<BN> {
        const self = this as any as fomo3dContract;


        const promizz = self._contract.methods.key_final_price(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async key_final_priceGas(): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.key_final_price().estimateGas();
        return gasAmount;
    };


    public async key_increasing_price(): Promise<BN> {
        const self = this as any as fomo3dContract;


        const promizz = self._contract.methods.key_increasing_price(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async key_increasing_priceGas(): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.key_increasing_price().estimateGas();
        return gasAmount;
    };


    public async key_init_price(): Promise<BN> {
        const self = this as any as fomo3dContract;


        const promizz = self._contract.methods.key_init_price(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async key_init_priceGas(): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.key_init_price().estimateGas();
        return gasAmount;
    };


    public async nonceOf(account: string,): Promise<BN> {
        const self = this as any as fomo3dContract;

            assert.isString('account', account);

        const promizz = self._contract.methods.nonceOf(
            account,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async nonceOfGas(account: string,): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.nonceOf(account,).estimateGas();
        return gasAmount;
    };


    public async owner(): Promise<string> {
        const self = this as any as fomo3dContract;


        const promizz = self._contract.methods.owner(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async ownerGas(): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.owner().estimateGas();
        return gasAmount;
    };


    public async rounds(): Promise<BN> {
        const self = this as any as fomo3dContract;


        const promizz = self._contract.methods.rounds(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async roundsGas(): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.rounds().estimateGas();
        return gasAmount;
    };


    public async setActionTime(_time: BN,): Promise<void> {
        const self = this as any as fomo3dContract;

            assert.isNumberOrBigNumber('_time', _time);

        const promizz = self._contract.methods.setActionTime(
            _time,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async setActionTimeGas(_time: BN,): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.setActionTime(_time,).estimateGas();
        return gasAmount;
    };


    public async start_time(index_0: BN,): Promise<BN> {
        const self = this as any as fomo3dContract;

            assert.isNumberOrBigNumber('index_0', index_0);

        const promizz = self._contract.methods.start_time(
            index_0,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async start_timeGas(index_0: BN,): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.start_time(index_0,).estimateGas();
        return gasAmount;
    };


    public async team(index_0: string,index_1: BN,): Promise<BN> {
        const self = this as any as fomo3dContract;

            assert.isString('index_0', index_0);
            assert.isNumberOrBigNumber('index_1', index_1);

        const promizz = self._contract.methods.team(
            index_0,
                    index_1,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async teamGas(index_0: string,index_1: BN,): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.team(index_0,index_1,).estimateGas();
        return gasAmount;
    };


    public async vaultBuy(_buy_num: BN,_team: number|BN,_rounds: BN,_account: string,nonce: BN,v: number|BN,r: string,s: string,valCoin: BN): Promise<void> {
        const self = this as any as fomo3dContract;

            assert.isNumberOrBigNumber('_buy_num', _buy_num);
            assert.isNumberOrBigNumber('_team', _team);
            assert.isNumberOrBigNumber('_rounds', _rounds);
            assert.isString('_account', _account);
            assert.isNumberOrBigNumber('nonce', nonce);
            assert.isNumberOrBigNumber('v', v);
            assert.isString('r', r);
            assert.isString('s', s);

        const promizz = self._contract.methods.vaultBuy(
            _buy_num,
                    _team,
                    _rounds,
                    _account,
                    nonce,
                    v,
                    r,
                    s,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice, value: valCoin
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async vaultBuyGas(_buy_num: BN,_team: number|BN,_rounds: BN,_account: string,nonce: BN,v: number|BN,r: string,s: string,): Promise<number>{
        const self = this as any as fomo3dContract;
        const gasAmount = await self._contract.methods.vaultBuy(_buy_num,_team,_rounds,_account,nonce,v,r,s,).estimateGas();
        return gasAmount;
    };


    /**
     * Subscribe to an event type emitted by the fomo3d contract.
     * @param eventName The fomo3d contract event you would like to subscribe to.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{maker: aUserAddressHex}`
     * @param callback Callback that gets called when a log is added/removed
     * @param isVerbose Enable verbose subscription warnings (e.g recoverable network issues encountered)
     * @return Subscription token used later to unsubscribe
     */
    public subscribe<ArgsType extends fomo3dEventArgs>(
        eventName: fomo3dEvents,
        indexFilterValues: IndexedFilterValues,
        callback: EventCallback<ArgsType>,
        isVerbose: boolean = false,
        blockPollingIntervalMs?: number,
    ): string {
        assert.doesBelongToStringEnum('eventName', eventName, fomo3dEvents);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        assert.isFunction('callback', callback);
        const subscriptionToken = this._subscriptionManager.subscribe<ArgsType>(
            this._address,
            eventName,
            indexFilterValues,
            fomo3dContract.ABI(),
            callback,
            isVerbose,
            blockPollingIntervalMs,
        );
        return subscriptionToken;
    }

    /**
     * Cancel a subscription
     * @param subscriptionToken Subscription token returned by `subscribe()`
     */
    public unsubscribe(subscriptionToken: string): void {
        this._subscriptionManager.unsubscribe(subscriptionToken);
    }

    /**
     * Cancels all existing subscriptions
     */
    public unsubscribeAll(): void {
        this._subscriptionManager.unsubscribeAll();
    }


    /**
     * Gets historical logs without creating a subscription
     * @param eventName The fomo3d contract event you would like to subscribe to.
     * @param blockRange Block range to get logs from.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{_from: aUserAddressHex}`
     * @return Array of logs that match the parameters
     */
    public async getLogsAsync<ArgsType extends fomo3dEventArgs>(
        eventName: fomo3dEvents,
        blockRange: BlockRange,
        indexFilterValues: IndexedFilterValues,
    ): Promise<Array<LogWithDecodedArgs<ArgsType>>> {
        assert.doesBelongToStringEnum('eventName', eventName, fomo3dEvents);
        assert.doesConformToSchema('blockRange', blockRange, schemas.blockRangeSchema);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        const logs = await this._subscriptionManager.getLogsAsync<ArgsType>(
            this._address,
            eventName,
            blockRange,
            indexFilterValues,
            fomo3dContract.ABI(),
        );
        return logs;
    }

    constructor(
        address: string,
        supportedProvider: provider,
        ww3: Web3
    ) {
        super('fomo3d', fomo3dContract.ABI(), address, supportedProvider,ww3);
        this._subscriptionManager = new SubscriptionManager(
            fomo3dContract.ABI(),
            supportedProvider,
        );

        fomo3dContract.ABI().forEach((item, index) => {
            if (item.type === 'function') {
                const methodAbi = item as MethodAbi;
                this._methodABIIndex[methodAbi.name] = index;
            }
        });


    }
}

// tslint:disable:max-file-line-count
// tslint:enable:no-unbound-method no-parameter-reassignment no-consecutive-blank-lines ordered-imports align
// tslint:enable:trailing-comma whitespace no-trailing-whitespace
