// Code generated - DO NOT EDIT.
// This file is a generated binding and any manual changes will be lost.

package fomo3d

import (
	"errors"
	"math/big"
	"strings"

	ethereum "github.com/ethereum/go-ethereum"
	"github.com/ethereum/go-ethereum/accounts/abi"
	"github.com/ethereum/go-ethereum/accounts/abi/bind"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/event"
)

// Reference imports to suppress errors if they are not otherwise used.
var (
	_ = errors.New
	_ = big.NewInt
	_ = strings.NewReader
	_ = ethereum.NotFound
	_ = bind.Bind
	_ = common.Big1
	_ = types.BloomLookup
	_ = event.NewSubscription
)

// Fomo3dMetaData contains all meta data concerning the Fomo3d contract.
var Fomo3dMetaData = &bind.MetaData{
	ABI: "[{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_owner\",\"type\":\"address\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"bnbvalue\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"buy_num\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"enumfomo3d.group\",\"name\":\"team\",\"type\":\"uint8\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"rounds\",\"type\":\"uint256\"}],\"name\":\"BnbBuy\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"claimvalue\",\"type\":\"uint256\"}],\"name\":\"Claim\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"vaultvalue\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"buy_num\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"enumfomo3d.group\",\"name\":\"team\",\"type\":\"uint8\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"rounds\",\"type\":\"uint256\"}],\"name\":\"VaultBuy\",\"type\":\"event\"},{\"inputs\":[],\"name\":\"CLAIM_TRANSACTION_TYPEHASH\",\"outputs\":[{\"internalType\":\"bytes32\",\"name\":\"\",\"type\":\"bytes32\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"DOMAIN_SEPARATOR\",\"outputs\":[{\"internalType\":\"bytes32\",\"name\":\"\",\"type\":\"bytes32\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"EIP712_DOMAIN_TYPEHASH\",\"outputs\":[{\"internalType\":\"bytes32\",\"name\":\"\",\"type\":\"bytes32\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"VAULTBUY_TRANSACTION_TYPEHASH\",\"outputs\":[{\"internalType\":\"bytes32\",\"name\":\"\",\"type\":\"bytes32\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_buy_num\",\"type\":\"uint256\"},{\"internalType\":\"enumfomo3d.group\",\"name\":\"_team\",\"type\":\"uint8\"},{\"internalType\":\"uint64\",\"name\":\"_rounds\",\"type\":\"uint64\"}],\"name\":\"bnbBuy\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"addresspayable\",\"name\":\"_account\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_number\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"nonce\",\"type\":\"uint256\"},{\"internalType\":\"uint8\",\"name\":\"v\",\"type\":\"uint8\"},{\"internalType\":\"bytes32\",\"name\":\"r\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"s\",\"type\":\"bytes32\"}],\"name\":\"claim\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"end_time\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"key_final_price\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"key_increasing_price\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"key_init_price\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"}],\"name\":\"nonceOf\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"rounds\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_time\",\"type\":\"uint256\"}],\"name\":\"setActionTime\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"start_time\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"team\",\"outputs\":[{\"internalType\":\"enumfomo3d.group\",\"name\":\"\",\"type\":\"uint8\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_buy_num\",\"type\":\"uint256\"},{\"internalType\":\"enumfomo3d.group\",\"name\":\"_team\",\"type\":\"uint8\"},{\"internalType\":\"uint256\",\"name\":\"_rounds\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"_account\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"nonce\",\"type\":\"uint256\"},{\"internalType\":\"uint8\",\"name\":\"v\",\"type\":\"uint8\"},{\"internalType\":\"bytes32\",\"name\":\"r\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"s\",\"type\":\"bytes32\"}],\"name\":\"vaultBuy\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"}]",
}

// Fomo3dABI is the input ABI used to generate the binding from.
// Deprecated: Use Fomo3dMetaData.ABI instead.
var Fomo3dABI = Fomo3dMetaData.ABI

// Fomo3d is an auto generated Go binding around an Ethereum contract.
type Fomo3d struct {
	Fomo3dCaller     // Read-only binding to the contract
	Fomo3dTransactor // Write-only binding to the contract
	Fomo3dFilterer   // Log filterer for contract events
}

// Fomo3dCaller is an auto generated read-only Go binding around an Ethereum contract.
type Fomo3dCaller struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// Fomo3dTransactor is an auto generated write-only Go binding around an Ethereum contract.
type Fomo3dTransactor struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// Fomo3dFilterer is an auto generated log filtering Go binding around an Ethereum contract events.
type Fomo3dFilterer struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// Fomo3dSession is an auto generated Go binding around an Ethereum contract,
// with pre-set call and transact options.
type Fomo3dSession struct {
	Contract     *Fomo3d           // Generic contract binding to set the session for
	CallOpts     bind.CallOpts     // Call options to use throughout this session
	TransactOpts bind.TransactOpts // Transaction auth options to use throughout this session
}

// Fomo3dCallerSession is an auto generated read-only Go binding around an Ethereum contract,
// with pre-set call options.
type Fomo3dCallerSession struct {
	Contract *Fomo3dCaller // Generic contract caller binding to set the session for
	CallOpts bind.CallOpts // Call options to use throughout this session
}

// Fomo3dTransactorSession is an auto generated write-only Go binding around an Ethereum contract,
// with pre-set transact options.
type Fomo3dTransactorSession struct {
	Contract     *Fomo3dTransactor // Generic contract transactor binding to set the session for
	TransactOpts bind.TransactOpts // Transaction auth options to use throughout this session
}

// Fomo3dRaw is an auto generated low-level Go binding around an Ethereum contract.
type Fomo3dRaw struct {
	Contract *Fomo3d // Generic contract binding to access the raw methods on
}

// Fomo3dCallerRaw is an auto generated low-level read-only Go binding around an Ethereum contract.
type Fomo3dCallerRaw struct {
	Contract *Fomo3dCaller // Generic read-only contract binding to access the raw methods on
}

// Fomo3dTransactorRaw is an auto generated low-level write-only Go binding around an Ethereum contract.
type Fomo3dTransactorRaw struct {
	Contract *Fomo3dTransactor // Generic write-only contract binding to access the raw methods on
}

// NewFomo3d creates a new instance of Fomo3d, bound to a specific deployed contract.
func NewFomo3d(address common.Address, backend bind.ContractBackend) (*Fomo3d, error) {
	contract, err := bindFomo3d(address, backend, backend, backend)
	if err != nil {
		return nil, err
	}
	return &Fomo3d{Fomo3dCaller: Fomo3dCaller{contract: contract}, Fomo3dTransactor: Fomo3dTransactor{contract: contract}, Fomo3dFilterer: Fomo3dFilterer{contract: contract}}, nil
}

// NewFomo3dCaller creates a new read-only instance of Fomo3d, bound to a specific deployed contract.
func NewFomo3dCaller(address common.Address, caller bind.ContractCaller) (*Fomo3dCaller, error) {
	contract, err := bindFomo3d(address, caller, nil, nil)
	if err != nil {
		return nil, err
	}
	return &Fomo3dCaller{contract: contract}, nil
}

// NewFomo3dTransactor creates a new write-only instance of Fomo3d, bound to a specific deployed contract.
func NewFomo3dTransactor(address common.Address, transactor bind.ContractTransactor) (*Fomo3dTransactor, error) {
	contract, err := bindFomo3d(address, nil, transactor, nil)
	if err != nil {
		return nil, err
	}
	return &Fomo3dTransactor{contract: contract}, nil
}

// NewFomo3dFilterer creates a new log filterer instance of Fomo3d, bound to a specific deployed contract.
func NewFomo3dFilterer(address common.Address, filterer bind.ContractFilterer) (*Fomo3dFilterer, error) {
	contract, err := bindFomo3d(address, nil, nil, filterer)
	if err != nil {
		return nil, err
	}
	return &Fomo3dFilterer{contract: contract}, nil
}

// bindFomo3d binds a generic wrapper to an already deployed contract.
func bindFomo3d(address common.Address, caller bind.ContractCaller, transactor bind.ContractTransactor, filterer bind.ContractFilterer) (*bind.BoundContract, error) {
	parsed, err := abi.JSON(strings.NewReader(Fomo3dABI))
	if err != nil {
		return nil, err
	}
	return bind.NewBoundContract(address, parsed, caller, transactor, filterer), nil
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_Fomo3d *Fomo3dRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _Fomo3d.Contract.Fomo3dCaller.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_Fomo3d *Fomo3dRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _Fomo3d.Contract.Fomo3dTransactor.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_Fomo3d *Fomo3dRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _Fomo3d.Contract.Fomo3dTransactor.contract.Transact(opts, method, params...)
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_Fomo3d *Fomo3dCallerRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _Fomo3d.Contract.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_Fomo3d *Fomo3dTransactorRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _Fomo3d.Contract.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_Fomo3d *Fomo3dTransactorRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _Fomo3d.Contract.contract.Transact(opts, method, params...)
}

// CLAIMTRANSACTIONTYPEHASH is a free data retrieval call binding the contract method 0x7d15daf9.
//
// Solidity: function CLAIM_TRANSACTION_TYPEHASH() view returns(bytes32)
func (_Fomo3d *Fomo3dCaller) CLAIMTRANSACTIONTYPEHASH(opts *bind.CallOpts) ([32]byte, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "CLAIM_TRANSACTION_TYPEHASH")

	if err != nil {
		return *new([32]byte), err
	}

	out0 := *abi.ConvertType(out[0], new([32]byte)).(*[32]byte)

	return out0, err

}

// CLAIMTRANSACTIONTYPEHASH is a free data retrieval call binding the contract method 0x7d15daf9.
//
// Solidity: function CLAIM_TRANSACTION_TYPEHASH() view returns(bytes32)
func (_Fomo3d *Fomo3dSession) CLAIMTRANSACTIONTYPEHASH() ([32]byte, error) {
	return _Fomo3d.Contract.CLAIMTRANSACTIONTYPEHASH(&_Fomo3d.CallOpts)
}

// CLAIMTRANSACTIONTYPEHASH is a free data retrieval call binding the contract method 0x7d15daf9.
//
// Solidity: function CLAIM_TRANSACTION_TYPEHASH() view returns(bytes32)
func (_Fomo3d *Fomo3dCallerSession) CLAIMTRANSACTIONTYPEHASH() ([32]byte, error) {
	return _Fomo3d.Contract.CLAIMTRANSACTIONTYPEHASH(&_Fomo3d.CallOpts)
}

// DOMAINSEPARATOR is a free data retrieval call binding the contract method 0x3644e515.
//
// Solidity: function DOMAIN_SEPARATOR() view returns(bytes32)
func (_Fomo3d *Fomo3dCaller) DOMAINSEPARATOR(opts *bind.CallOpts) ([32]byte, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "DOMAIN_SEPARATOR")

	if err != nil {
		return *new([32]byte), err
	}

	out0 := *abi.ConvertType(out[0], new([32]byte)).(*[32]byte)

	return out0, err

}

// DOMAINSEPARATOR is a free data retrieval call binding the contract method 0x3644e515.
//
// Solidity: function DOMAIN_SEPARATOR() view returns(bytes32)
func (_Fomo3d *Fomo3dSession) DOMAINSEPARATOR() ([32]byte, error) {
	return _Fomo3d.Contract.DOMAINSEPARATOR(&_Fomo3d.CallOpts)
}

// DOMAINSEPARATOR is a free data retrieval call binding the contract method 0x3644e515.
//
// Solidity: function DOMAIN_SEPARATOR() view returns(bytes32)
func (_Fomo3d *Fomo3dCallerSession) DOMAINSEPARATOR() ([32]byte, error) {
	return _Fomo3d.Contract.DOMAINSEPARATOR(&_Fomo3d.CallOpts)
}

// EIP712DOMAINTYPEHASH is a free data retrieval call binding the contract method 0xc7977be7.
//
// Solidity: function EIP712_DOMAIN_TYPEHASH() view returns(bytes32)
func (_Fomo3d *Fomo3dCaller) EIP712DOMAINTYPEHASH(opts *bind.CallOpts) ([32]byte, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "EIP712_DOMAIN_TYPEHASH")

	if err != nil {
		return *new([32]byte), err
	}

	out0 := *abi.ConvertType(out[0], new([32]byte)).(*[32]byte)

	return out0, err

}

// EIP712DOMAINTYPEHASH is a free data retrieval call binding the contract method 0xc7977be7.
//
// Solidity: function EIP712_DOMAIN_TYPEHASH() view returns(bytes32)
func (_Fomo3d *Fomo3dSession) EIP712DOMAINTYPEHASH() ([32]byte, error) {
	return _Fomo3d.Contract.EIP712DOMAINTYPEHASH(&_Fomo3d.CallOpts)
}

// EIP712DOMAINTYPEHASH is a free data retrieval call binding the contract method 0xc7977be7.
//
// Solidity: function EIP712_DOMAIN_TYPEHASH() view returns(bytes32)
func (_Fomo3d *Fomo3dCallerSession) EIP712DOMAINTYPEHASH() ([32]byte, error) {
	return _Fomo3d.Contract.EIP712DOMAINTYPEHASH(&_Fomo3d.CallOpts)
}

// VAULTBUYTRANSACTIONTYPEHASH is a free data retrieval call binding the contract method 0x0233cb9e.
//
// Solidity: function VAULTBUY_TRANSACTION_TYPEHASH() view returns(bytes32)
func (_Fomo3d *Fomo3dCaller) VAULTBUYTRANSACTIONTYPEHASH(opts *bind.CallOpts) ([32]byte, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "VAULTBUY_TRANSACTION_TYPEHASH")

	if err != nil {
		return *new([32]byte), err
	}

	out0 := *abi.ConvertType(out[0], new([32]byte)).(*[32]byte)

	return out0, err

}

// VAULTBUYTRANSACTIONTYPEHASH is a free data retrieval call binding the contract method 0x0233cb9e.
//
// Solidity: function VAULTBUY_TRANSACTION_TYPEHASH() view returns(bytes32)
func (_Fomo3d *Fomo3dSession) VAULTBUYTRANSACTIONTYPEHASH() ([32]byte, error) {
	return _Fomo3d.Contract.VAULTBUYTRANSACTIONTYPEHASH(&_Fomo3d.CallOpts)
}

// VAULTBUYTRANSACTIONTYPEHASH is a free data retrieval call binding the contract method 0x0233cb9e.
//
// Solidity: function VAULTBUY_TRANSACTION_TYPEHASH() view returns(bytes32)
func (_Fomo3d *Fomo3dCallerSession) VAULTBUYTRANSACTIONTYPEHASH() ([32]byte, error) {
	return _Fomo3d.Contract.VAULTBUYTRANSACTIONTYPEHASH(&_Fomo3d.CallOpts)
}

// EndTime is a free data retrieval call binding the contract method 0x4dd3d46a.
//
// Solidity: function end_time(uint256 ) view returns(uint256)
func (_Fomo3d *Fomo3dCaller) EndTime(opts *bind.CallOpts, arg0 *big.Int) (*big.Int, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "end_time", arg0)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// EndTime is a free data retrieval call binding the contract method 0x4dd3d46a.
//
// Solidity: function end_time(uint256 ) view returns(uint256)
func (_Fomo3d *Fomo3dSession) EndTime(arg0 *big.Int) (*big.Int, error) {
	return _Fomo3d.Contract.EndTime(&_Fomo3d.CallOpts, arg0)
}

// EndTime is a free data retrieval call binding the contract method 0x4dd3d46a.
//
// Solidity: function end_time(uint256 ) view returns(uint256)
func (_Fomo3d *Fomo3dCallerSession) EndTime(arg0 *big.Int) (*big.Int, error) {
	return _Fomo3d.Contract.EndTime(&_Fomo3d.CallOpts, arg0)
}

// KeyFinalPrice is a free data retrieval call binding the contract method 0xb123deb8.
//
// Solidity: function key_final_price() view returns(uint256)
func (_Fomo3d *Fomo3dCaller) KeyFinalPrice(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "key_final_price")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// KeyFinalPrice is a free data retrieval call binding the contract method 0xb123deb8.
//
// Solidity: function key_final_price() view returns(uint256)
func (_Fomo3d *Fomo3dSession) KeyFinalPrice() (*big.Int, error) {
	return _Fomo3d.Contract.KeyFinalPrice(&_Fomo3d.CallOpts)
}

// KeyFinalPrice is a free data retrieval call binding the contract method 0xb123deb8.
//
// Solidity: function key_final_price() view returns(uint256)
func (_Fomo3d *Fomo3dCallerSession) KeyFinalPrice() (*big.Int, error) {
	return _Fomo3d.Contract.KeyFinalPrice(&_Fomo3d.CallOpts)
}

// KeyIncreasingPrice is a free data retrieval call binding the contract method 0xe1c32065.
//
// Solidity: function key_increasing_price() view returns(uint256)
func (_Fomo3d *Fomo3dCaller) KeyIncreasingPrice(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "key_increasing_price")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// KeyIncreasingPrice is a free data retrieval call binding the contract method 0xe1c32065.
//
// Solidity: function key_increasing_price() view returns(uint256)
func (_Fomo3d *Fomo3dSession) KeyIncreasingPrice() (*big.Int, error) {
	return _Fomo3d.Contract.KeyIncreasingPrice(&_Fomo3d.CallOpts)
}

// KeyIncreasingPrice is a free data retrieval call binding the contract method 0xe1c32065.
//
// Solidity: function key_increasing_price() view returns(uint256)
func (_Fomo3d *Fomo3dCallerSession) KeyIncreasingPrice() (*big.Int, error) {
	return _Fomo3d.Contract.KeyIncreasingPrice(&_Fomo3d.CallOpts)
}

// KeyInitPrice is a free data retrieval call binding the contract method 0x5b833c60.
//
// Solidity: function key_init_price() view returns(uint256)
func (_Fomo3d *Fomo3dCaller) KeyInitPrice(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "key_init_price")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// KeyInitPrice is a free data retrieval call binding the contract method 0x5b833c60.
//
// Solidity: function key_init_price() view returns(uint256)
func (_Fomo3d *Fomo3dSession) KeyInitPrice() (*big.Int, error) {
	return _Fomo3d.Contract.KeyInitPrice(&_Fomo3d.CallOpts)
}

// KeyInitPrice is a free data retrieval call binding the contract method 0x5b833c60.
//
// Solidity: function key_init_price() view returns(uint256)
func (_Fomo3d *Fomo3dCallerSession) KeyInitPrice() (*big.Int, error) {
	return _Fomo3d.Contract.KeyInitPrice(&_Fomo3d.CallOpts)
}

// NonceOf is a free data retrieval call binding the contract method 0xed2a2d64.
//
// Solidity: function nonceOf(address account) view returns(uint256)
func (_Fomo3d *Fomo3dCaller) NonceOf(opts *bind.CallOpts, account common.Address) (*big.Int, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "nonceOf", account)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// NonceOf is a free data retrieval call binding the contract method 0xed2a2d64.
//
// Solidity: function nonceOf(address account) view returns(uint256)
func (_Fomo3d *Fomo3dSession) NonceOf(account common.Address) (*big.Int, error) {
	return _Fomo3d.Contract.NonceOf(&_Fomo3d.CallOpts, account)
}

// NonceOf is a free data retrieval call binding the contract method 0xed2a2d64.
//
// Solidity: function nonceOf(address account) view returns(uint256)
func (_Fomo3d *Fomo3dCallerSession) NonceOf(account common.Address) (*big.Int, error) {
	return _Fomo3d.Contract.NonceOf(&_Fomo3d.CallOpts, account)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_Fomo3d *Fomo3dCaller) Owner(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "owner")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_Fomo3d *Fomo3dSession) Owner() (common.Address, error) {
	return _Fomo3d.Contract.Owner(&_Fomo3d.CallOpts)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_Fomo3d *Fomo3dCallerSession) Owner() (common.Address, error) {
	return _Fomo3d.Contract.Owner(&_Fomo3d.CallOpts)
}

// Rounds is a free data retrieval call binding the contract method 0xa2e800ad.
//
// Solidity: function rounds() view returns(uint256)
func (_Fomo3d *Fomo3dCaller) Rounds(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "rounds")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// Rounds is a free data retrieval call binding the contract method 0xa2e800ad.
//
// Solidity: function rounds() view returns(uint256)
func (_Fomo3d *Fomo3dSession) Rounds() (*big.Int, error) {
	return _Fomo3d.Contract.Rounds(&_Fomo3d.CallOpts)
}

// Rounds is a free data retrieval call binding the contract method 0xa2e800ad.
//
// Solidity: function rounds() view returns(uint256)
func (_Fomo3d *Fomo3dCallerSession) Rounds() (*big.Int, error) {
	return _Fomo3d.Contract.Rounds(&_Fomo3d.CallOpts)
}

// StartTime is a free data retrieval call binding the contract method 0x89346abf.
//
// Solidity: function start_time(uint256 ) view returns(uint256)
func (_Fomo3d *Fomo3dCaller) StartTime(opts *bind.CallOpts, arg0 *big.Int) (*big.Int, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "start_time", arg0)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// StartTime is a free data retrieval call binding the contract method 0x89346abf.
//
// Solidity: function start_time(uint256 ) view returns(uint256)
func (_Fomo3d *Fomo3dSession) StartTime(arg0 *big.Int) (*big.Int, error) {
	return _Fomo3d.Contract.StartTime(&_Fomo3d.CallOpts, arg0)
}

// StartTime is a free data retrieval call binding the contract method 0x89346abf.
//
// Solidity: function start_time(uint256 ) view returns(uint256)
func (_Fomo3d *Fomo3dCallerSession) StartTime(arg0 *big.Int) (*big.Int, error) {
	return _Fomo3d.Contract.StartTime(&_Fomo3d.CallOpts, arg0)
}

// Team is a free data retrieval call binding the contract method 0x43cfdbfc.
//
// Solidity: function team(address , uint256 ) view returns(uint8)
func (_Fomo3d *Fomo3dCaller) Team(opts *bind.CallOpts, arg0 common.Address, arg1 *big.Int) (uint8, error) {
	var out []interface{}
	err := _Fomo3d.contract.Call(opts, &out, "team", arg0, arg1)

	if err != nil {
		return *new(uint8), err
	}

	out0 := *abi.ConvertType(out[0], new(uint8)).(*uint8)

	return out0, err

}

// Team is a free data retrieval call binding the contract method 0x43cfdbfc.
//
// Solidity: function team(address , uint256 ) view returns(uint8)
func (_Fomo3d *Fomo3dSession) Team(arg0 common.Address, arg1 *big.Int) (uint8, error) {
	return _Fomo3d.Contract.Team(&_Fomo3d.CallOpts, arg0, arg1)
}

// Team is a free data retrieval call binding the contract method 0x43cfdbfc.
//
// Solidity: function team(address , uint256 ) view returns(uint8)
func (_Fomo3d *Fomo3dCallerSession) Team(arg0 common.Address, arg1 *big.Int) (uint8, error) {
	return _Fomo3d.Contract.Team(&_Fomo3d.CallOpts, arg0, arg1)
}

// BnbBuy is a paid mutator transaction binding the contract method 0x391a788d.
//
// Solidity: function bnbBuy(uint256 _buy_num, uint8 _team, uint64 _rounds) payable returns()
func (_Fomo3d *Fomo3dTransactor) BnbBuy(opts *bind.TransactOpts, _buy_num *big.Int, _team uint8, _rounds uint64) (*types.Transaction, error) {
	return _Fomo3d.contract.Transact(opts, "bnbBuy", _buy_num, _team, _rounds)
}

// BnbBuy is a paid mutator transaction binding the contract method 0x391a788d.
//
// Solidity: function bnbBuy(uint256 _buy_num, uint8 _team, uint64 _rounds) payable returns()
func (_Fomo3d *Fomo3dSession) BnbBuy(_buy_num *big.Int, _team uint8, _rounds uint64) (*types.Transaction, error) {
	return _Fomo3d.Contract.BnbBuy(&_Fomo3d.TransactOpts, _buy_num, _team, _rounds)
}

// BnbBuy is a paid mutator transaction binding the contract method 0x391a788d.
//
// Solidity: function bnbBuy(uint256 _buy_num, uint8 _team, uint64 _rounds) payable returns()
func (_Fomo3d *Fomo3dTransactorSession) BnbBuy(_buy_num *big.Int, _team uint8, _rounds uint64) (*types.Transaction, error) {
	return _Fomo3d.Contract.BnbBuy(&_Fomo3d.TransactOpts, _buy_num, _team, _rounds)
}

// Claim is a paid mutator transaction binding the contract method 0x0d48a771.
//
// Solidity: function claim(address _account, uint256 _number, uint256 nonce, uint8 v, bytes32 r, bytes32 s) returns()
func (_Fomo3d *Fomo3dTransactor) Claim(opts *bind.TransactOpts, _account common.Address, _number *big.Int, nonce *big.Int, v uint8, r [32]byte, s [32]byte) (*types.Transaction, error) {
	return _Fomo3d.contract.Transact(opts, "claim", _account, _number, nonce, v, r, s)
}

// Claim is a paid mutator transaction binding the contract method 0x0d48a771.
//
// Solidity: function claim(address _account, uint256 _number, uint256 nonce, uint8 v, bytes32 r, bytes32 s) returns()
func (_Fomo3d *Fomo3dSession) Claim(_account common.Address, _number *big.Int, nonce *big.Int, v uint8, r [32]byte, s [32]byte) (*types.Transaction, error) {
	return _Fomo3d.Contract.Claim(&_Fomo3d.TransactOpts, _account, _number, nonce, v, r, s)
}

// Claim is a paid mutator transaction binding the contract method 0x0d48a771.
//
// Solidity: function claim(address _account, uint256 _number, uint256 nonce, uint8 v, bytes32 r, bytes32 s) returns()
func (_Fomo3d *Fomo3dTransactorSession) Claim(_account common.Address, _number *big.Int, nonce *big.Int, v uint8, r [32]byte, s [32]byte) (*types.Transaction, error) {
	return _Fomo3d.Contract.Claim(&_Fomo3d.TransactOpts, _account, _number, nonce, v, r, s)
}

// SetActionTime is a paid mutator transaction binding the contract method 0x1a486c19.
//
// Solidity: function setActionTime(uint256 _time) returns()
func (_Fomo3d *Fomo3dTransactor) SetActionTime(opts *bind.TransactOpts, _time *big.Int) (*types.Transaction, error) {
	return _Fomo3d.contract.Transact(opts, "setActionTime", _time)
}

// SetActionTime is a paid mutator transaction binding the contract method 0x1a486c19.
//
// Solidity: function setActionTime(uint256 _time) returns()
func (_Fomo3d *Fomo3dSession) SetActionTime(_time *big.Int) (*types.Transaction, error) {
	return _Fomo3d.Contract.SetActionTime(&_Fomo3d.TransactOpts, _time)
}

// SetActionTime is a paid mutator transaction binding the contract method 0x1a486c19.
//
// Solidity: function setActionTime(uint256 _time) returns()
func (_Fomo3d *Fomo3dTransactorSession) SetActionTime(_time *big.Int) (*types.Transaction, error) {
	return _Fomo3d.Contract.SetActionTime(&_Fomo3d.TransactOpts, _time)
}

// VaultBuy is a paid mutator transaction binding the contract method 0xb2b2f051.
//
// Solidity: function vaultBuy(uint256 _buy_num, uint8 _team, uint256 _rounds, address _account, uint256 nonce, uint8 v, bytes32 r, bytes32 s) payable returns()
func (_Fomo3d *Fomo3dTransactor) VaultBuy(opts *bind.TransactOpts, _buy_num *big.Int, _team uint8, _rounds *big.Int, _account common.Address, nonce *big.Int, v uint8, r [32]byte, s [32]byte) (*types.Transaction, error) {
	return _Fomo3d.contract.Transact(opts, "vaultBuy", _buy_num, _team, _rounds, _account, nonce, v, r, s)
}

// VaultBuy is a paid mutator transaction binding the contract method 0xb2b2f051.
//
// Solidity: function vaultBuy(uint256 _buy_num, uint8 _team, uint256 _rounds, address _account, uint256 nonce, uint8 v, bytes32 r, bytes32 s) payable returns()
func (_Fomo3d *Fomo3dSession) VaultBuy(_buy_num *big.Int, _team uint8, _rounds *big.Int, _account common.Address, nonce *big.Int, v uint8, r [32]byte, s [32]byte) (*types.Transaction, error) {
	return _Fomo3d.Contract.VaultBuy(&_Fomo3d.TransactOpts, _buy_num, _team, _rounds, _account, nonce, v, r, s)
}

// VaultBuy is a paid mutator transaction binding the contract method 0xb2b2f051.
//
// Solidity: function vaultBuy(uint256 _buy_num, uint8 _team, uint256 _rounds, address _account, uint256 nonce, uint8 v, bytes32 r, bytes32 s) payable returns()
func (_Fomo3d *Fomo3dTransactorSession) VaultBuy(_buy_num *big.Int, _team uint8, _rounds *big.Int, _account common.Address, nonce *big.Int, v uint8, r [32]byte, s [32]byte) (*types.Transaction, error) {
	return _Fomo3d.Contract.VaultBuy(&_Fomo3d.TransactOpts, _buy_num, _team, _rounds, _account, nonce, v, r, s)
}

// Fomo3dBnbBuyIterator is returned from FilterBnbBuy and is used to iterate over the raw logs and unpacked data for BnbBuy events raised by the Fomo3d contract.
type Fomo3dBnbBuyIterator struct {
	Event *Fomo3dBnbBuy // Event containing the contract specifics and raw log

	contract *bind.BoundContract // Generic contract to use for unpacking event data
	event    string              // Event name to use for unpacking event data

	logs chan types.Log        // Log channel receiving the found contract events
	sub  ethereum.Subscription // Subscription for errors, completion and termination
	done bool                  // Whether the subscription completed delivering logs
	fail error                 // Occurred error to stop iteration
}

// Next advances the iterator to the subsequent event, returning whether there
// are any more events found. In case of a retrieval or parsing error, false is
// returned and Error() can be queried for the exact failure.
func (it *Fomo3dBnbBuyIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(Fomo3dBnbBuy)
			if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
				it.fail = err
				return false
			}
			it.Event.Raw = log
			return true

		default:
			return false
		}
	}
	// Iterator still in progress, wait for either a data or an error event
	select {
	case log := <-it.logs:
		it.Event = new(Fomo3dBnbBuy)
		if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
			it.fail = err
			return false
		}
		it.Event.Raw = log
		return true

	case err := <-it.sub.Err():
		it.done = true
		it.fail = err
		return it.Next()
	}
}

// Error returns any retrieval or parsing error occurred during filtering.
func (it *Fomo3dBnbBuyIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *Fomo3dBnbBuyIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// Fomo3dBnbBuy represents a BnbBuy event raised by the Fomo3d contract.
type Fomo3dBnbBuy struct {
	Account  common.Address
	Bnbvalue *big.Int
	BuyNum   *big.Int
	Team     uint8
	Rounds   *big.Int
	Raw      types.Log // Blockchain specific contextual infos
}

// FilterBnbBuy is a free log retrieval operation binding the contract event 0xdc1d38813fcbeaafbe45a7fdf21cec51686cfd391babbe144e71ae44155438e7.
//
// Solidity: event BnbBuy(address account, uint256 bnbvalue, uint256 buy_num, uint8 team, uint256 rounds)
func (_Fomo3d *Fomo3dFilterer) FilterBnbBuy(opts *bind.FilterOpts) (*Fomo3dBnbBuyIterator, error) {

	logs, sub, err := _Fomo3d.contract.FilterLogs(opts, "BnbBuy")
	if err != nil {
		return nil, err
	}
	return &Fomo3dBnbBuyIterator{contract: _Fomo3d.contract, event: "BnbBuy", logs: logs, sub: sub}, nil
}

// WatchBnbBuy is a free log subscription operation binding the contract event 0xdc1d38813fcbeaafbe45a7fdf21cec51686cfd391babbe144e71ae44155438e7.
//
// Solidity: event BnbBuy(address account, uint256 bnbvalue, uint256 buy_num, uint8 team, uint256 rounds)
func (_Fomo3d *Fomo3dFilterer) WatchBnbBuy(opts *bind.WatchOpts, sink chan<- *Fomo3dBnbBuy) (event.Subscription, error) {

	logs, sub, err := _Fomo3d.contract.WatchLogs(opts, "BnbBuy")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(Fomo3dBnbBuy)
				if err := _Fomo3d.contract.UnpackLog(event, "BnbBuy", log); err != nil {
					return err
				}
				event.Raw = log

				select {
				case sink <- event:
				case err := <-sub.Err():
					return err
				case <-quit:
					return nil
				}
			case err := <-sub.Err():
				return err
			case <-quit:
				return nil
			}
		}
	}), nil
}

// ParseBnbBuy is a log parse operation binding the contract event 0xdc1d38813fcbeaafbe45a7fdf21cec51686cfd391babbe144e71ae44155438e7.
//
// Solidity: event BnbBuy(address account, uint256 bnbvalue, uint256 buy_num, uint8 team, uint256 rounds)
func (_Fomo3d *Fomo3dFilterer) ParseBnbBuy(log types.Log) (*Fomo3dBnbBuy, error) {
	event := new(Fomo3dBnbBuy)
	if err := _Fomo3d.contract.UnpackLog(event, "BnbBuy", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// Fomo3dClaimIterator is returned from FilterClaim and is used to iterate over the raw logs and unpacked data for Claim events raised by the Fomo3d contract.
type Fomo3dClaimIterator struct {
	Event *Fomo3dClaim // Event containing the contract specifics and raw log

	contract *bind.BoundContract // Generic contract to use for unpacking event data
	event    string              // Event name to use for unpacking event data

	logs chan types.Log        // Log channel receiving the found contract events
	sub  ethereum.Subscription // Subscription for errors, completion and termination
	done bool                  // Whether the subscription completed delivering logs
	fail error                 // Occurred error to stop iteration
}

// Next advances the iterator to the subsequent event, returning whether there
// are any more events found. In case of a retrieval or parsing error, false is
// returned and Error() can be queried for the exact failure.
func (it *Fomo3dClaimIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(Fomo3dClaim)
			if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
				it.fail = err
				return false
			}
			it.Event.Raw = log
			return true

		default:
			return false
		}
	}
	// Iterator still in progress, wait for either a data or an error event
	select {
	case log := <-it.logs:
		it.Event = new(Fomo3dClaim)
		if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
			it.fail = err
			return false
		}
		it.Event.Raw = log
		return true

	case err := <-it.sub.Err():
		it.done = true
		it.fail = err
		return it.Next()
	}
}

// Error returns any retrieval or parsing error occurred during filtering.
func (it *Fomo3dClaimIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *Fomo3dClaimIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// Fomo3dClaim represents a Claim event raised by the Fomo3d contract.
type Fomo3dClaim struct {
	Account    common.Address
	Claimvalue *big.Int
	Raw        types.Log // Blockchain specific contextual infos
}

// FilterClaim is a free log retrieval operation binding the contract event 0x47cee97cb7acd717b3c0aa1435d004cd5b3c8c57d70dbceb4e4458bbd60e39d4.
//
// Solidity: event Claim(address account, uint256 claimvalue)
func (_Fomo3d *Fomo3dFilterer) FilterClaim(opts *bind.FilterOpts) (*Fomo3dClaimIterator, error) {

	logs, sub, err := _Fomo3d.contract.FilterLogs(opts, "Claim")
	if err != nil {
		return nil, err
	}
	return &Fomo3dClaimIterator{contract: _Fomo3d.contract, event: "Claim", logs: logs, sub: sub}, nil
}

// WatchClaim is a free log subscription operation binding the contract event 0x47cee97cb7acd717b3c0aa1435d004cd5b3c8c57d70dbceb4e4458bbd60e39d4.
//
// Solidity: event Claim(address account, uint256 claimvalue)
func (_Fomo3d *Fomo3dFilterer) WatchClaim(opts *bind.WatchOpts, sink chan<- *Fomo3dClaim) (event.Subscription, error) {

	logs, sub, err := _Fomo3d.contract.WatchLogs(opts, "Claim")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(Fomo3dClaim)
				if err := _Fomo3d.contract.UnpackLog(event, "Claim", log); err != nil {
					return err
				}
				event.Raw = log

				select {
				case sink <- event:
				case err := <-sub.Err():
					return err
				case <-quit:
					return nil
				}
			case err := <-sub.Err():
				return err
			case <-quit:
				return nil
			}
		}
	}), nil
}

// ParseClaim is a log parse operation binding the contract event 0x47cee97cb7acd717b3c0aa1435d004cd5b3c8c57d70dbceb4e4458bbd60e39d4.
//
// Solidity: event Claim(address account, uint256 claimvalue)
func (_Fomo3d *Fomo3dFilterer) ParseClaim(log types.Log) (*Fomo3dClaim, error) {
	event := new(Fomo3dClaim)
	if err := _Fomo3d.contract.UnpackLog(event, "Claim", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// Fomo3dVaultBuyIterator is returned from FilterVaultBuy and is used to iterate over the raw logs and unpacked data for VaultBuy events raised by the Fomo3d contract.
type Fomo3dVaultBuyIterator struct {
	Event *Fomo3dVaultBuy // Event containing the contract specifics and raw log

	contract *bind.BoundContract // Generic contract to use for unpacking event data
	event    string              // Event name to use for unpacking event data

	logs chan types.Log        // Log channel receiving the found contract events
	sub  ethereum.Subscription // Subscription for errors, completion and termination
	done bool                  // Whether the subscription completed delivering logs
	fail error                 // Occurred error to stop iteration
}

// Next advances the iterator to the subsequent event, returning whether there
// are any more events found. In case of a retrieval or parsing error, false is
// returned and Error() can be queried for the exact failure.
func (it *Fomo3dVaultBuyIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(Fomo3dVaultBuy)
			if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
				it.fail = err
				return false
			}
			it.Event.Raw = log
			return true

		default:
			return false
		}
	}
	// Iterator still in progress, wait for either a data or an error event
	select {
	case log := <-it.logs:
		it.Event = new(Fomo3dVaultBuy)
		if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
			it.fail = err
			return false
		}
		it.Event.Raw = log
		return true

	case err := <-it.sub.Err():
		it.done = true
		it.fail = err
		return it.Next()
	}
}

// Error returns any retrieval or parsing error occurred during filtering.
func (it *Fomo3dVaultBuyIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *Fomo3dVaultBuyIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// Fomo3dVaultBuy represents a VaultBuy event raised by the Fomo3d contract.
type Fomo3dVaultBuy struct {
	Account    common.Address
	Vaultvalue *big.Int
	BuyNum     *big.Int
	Team       uint8
	Rounds     *big.Int
	Raw        types.Log // Blockchain specific contextual infos
}

// FilterVaultBuy is a free log retrieval operation binding the contract event 0xd06722fa6ab200ab6e8e199efdc755a39e2ee43a449b77b085789a2aeec3f6aa.
//
// Solidity: event VaultBuy(address account, uint256 vaultvalue, uint256 buy_num, uint8 team, uint256 rounds)
func (_Fomo3d *Fomo3dFilterer) FilterVaultBuy(opts *bind.FilterOpts) (*Fomo3dVaultBuyIterator, error) {

	logs, sub, err := _Fomo3d.contract.FilterLogs(opts, "VaultBuy")
	if err != nil {
		return nil, err
	}
	return &Fomo3dVaultBuyIterator{contract: _Fomo3d.contract, event: "VaultBuy", logs: logs, sub: sub}, nil
}

// WatchVaultBuy is a free log subscription operation binding the contract event 0xd06722fa6ab200ab6e8e199efdc755a39e2ee43a449b77b085789a2aeec3f6aa.
//
// Solidity: event VaultBuy(address account, uint256 vaultvalue, uint256 buy_num, uint8 team, uint256 rounds)
func (_Fomo3d *Fomo3dFilterer) WatchVaultBuy(opts *bind.WatchOpts, sink chan<- *Fomo3dVaultBuy) (event.Subscription, error) {

	logs, sub, err := _Fomo3d.contract.WatchLogs(opts, "VaultBuy")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(Fomo3dVaultBuy)
				if err := _Fomo3d.contract.UnpackLog(event, "VaultBuy", log); err != nil {
					return err
				}
				event.Raw = log

				select {
				case sink <- event:
				case err := <-sub.Err():
					return err
				case <-quit:
					return nil
				}
			case err := <-sub.Err():
				return err
			case <-quit:
				return nil
			}
		}
	}), nil
}

// ParseVaultBuy is a log parse operation binding the contract event 0xd06722fa6ab200ab6e8e199efdc755a39e2ee43a449b77b085789a2aeec3f6aa.
//
// Solidity: event VaultBuy(address account, uint256 vaultvalue, uint256 buy_num, uint8 team, uint256 rounds)
func (_Fomo3d *Fomo3dFilterer) ParseVaultBuy(log types.Log) (*Fomo3dVaultBuy, error) {
	event := new(Fomo3dVaultBuy)
	if err := _Fomo3d.contract.UnpackLog(event, "VaultBuy", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}
