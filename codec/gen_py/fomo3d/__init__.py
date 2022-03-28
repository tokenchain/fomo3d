"""Generated wrapper for fomo3d Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)
import time
from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider
from web3.exceptions import ContractLogicError
from moody.m.bases import ContractMethod, Validator, ContractBase, Signatures
from moody.m.tx_params import TxParams
from moody.libeb import MiliDoS
from moody import Bolors

# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for fomo3d below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        fomo3dValidator,
    )
except ImportError:

    class fomo3dValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class ClaimTransactionTypehashMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the CLAIM_TRANSACTION_TYPEHASH method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("CLAIM_TRANSACTION_TYPEHASH")



    def block_call(self, debug:bool=False) -> Union[bytes, str]:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return Union[bytes, str](returned)
    def block_send(self, _gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: claim_transaction_typehash")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, claim_transaction_typehash: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, claim_transaction_typehash. Reason: Unknown")


    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class DomainSeparatorMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the DOMAIN_SEPARATOR method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("DOMAIN_SEPARATOR")



    def block_call(self, debug:bool=False) -> Union[bytes, str]:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return Union[bytes, str](returned)
    def block_send(self, _gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: domain_separator")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, domain_separator: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, domain_separator. Reason: Unknown")


    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class Eip712DomainTypehashMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the EIP712_DOMAIN_TYPEHASH method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("EIP712_DOMAIN_TYPEHASH")



    def block_call(self, debug:bool=False) -> Union[bytes, str]:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return Union[bytes, str](returned)
    def block_send(self, _gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: eip712_domain_typehash")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, eip712_domain_typehash: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, eip712_domain_typehash. Reason: Unknown")


    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class VaultbuyTransactionTypehashMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the VAULTBUY_TRANSACTION_TYPEHASH method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("VAULTBUY_TRANSACTION_TYPEHASH")



    def block_call(self, debug:bool=False) -> Union[bytes, str]:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return Union[bytes, str](returned)
    def block_send(self, _gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: vaultbuy_transaction_typehash")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, vaultbuy_transaction_typehash: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, vaultbuy_transaction_typehash. Reason: Unknown")


    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class BnbBuyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the bnbBuy method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("bnbBuy")

    def validate_and_normalize_inputs(self, buy_num: int, team: int, rounds: int)->any:
        """Validate the inputs to the bnbBuy method."""
        self.validator.assert_valid(
            method_name='bnbBuy',
            parameter_name='_buy_num',
            argument_value=buy_num,
        )
        # safeguard against fractional inputs
        buy_num = int(buy_num)
        self.validator.assert_valid(
            method_name='bnbBuy',
            parameter_name='_team',
            argument_value=team,
        )
        self.validator.assert_valid(
            method_name='bnbBuy',
            parameter_name='_rounds',
            argument_value=rounds,
        )
        return (buy_num, team, rounds)



    def block_send(self, buy_num: int, team: int, rounds: int,_gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(buy_num, team, rounds)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: bnb_buy")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, bnb_buy: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, bnb_buy. Reason: Unknown")


    def send_transaction(self, buy_num: int, team: int, rounds: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (buy_num, team, rounds) = self.validate_and_normalize_inputs(buy_num, team, rounds)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(buy_num, team, rounds).transact(tx_params.as_dict())

    def build_transaction(self, buy_num: int, team: int, rounds: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (buy_num, team, rounds) = self.validate_and_normalize_inputs(buy_num, team, rounds)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(buy_num, team, rounds).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, buy_num: int, team: int, rounds: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (buy_num, team, rounds) = self.validate_and_normalize_inputs(buy_num, team, rounds)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(buy_num, team, rounds).estimateGas(tx_params.as_dict())

class ClaimMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the claim method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("claim")

    def validate_and_normalize_inputs(self, account: str, number: int, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str])->any:
        """Validate the inputs to the claim method."""
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='_account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='_number',
            argument_value=number,
        )
        # safeguard against fractional inputs
        number = int(number)
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='nonce',
            argument_value=nonce,
        )
        # safeguard against fractional inputs
        nonce = int(nonce)
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='v',
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='r',
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='s',
            argument_value=s,
        )
        return (account, number, nonce, v, r, s)



    def block_send(self, account: str, number: int, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str],_gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(account, number, nonce, v, r, s)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: claim")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, claim: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, claim. Reason: Unknown")


    def send_transaction(self, account: str, number: int, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, number, nonce, v, r, s) = self.validate_and_normalize_inputs(account, number, nonce, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, number, nonce, v, r, s).transact(tx_params.as_dict())

    def build_transaction(self, account: str, number: int, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, number, nonce, v, r, s) = self.validate_and_normalize_inputs(account, number, nonce, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, number, nonce, v, r, s).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, number: int, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, number, nonce, v, r, s) = self.validate_and_normalize_inputs(account, number, nonce, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, number, nonce, v, r, s).estimateGas(tx_params.as_dict())

class EndTimeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the end_time method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("end_time")

    def validate_and_normalize_inputs(self, index_0: int)->any:
        """Validate the inputs to the end_time method."""
        self.validator.assert_valid(
            method_name='end_time',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)



    def block_call(self,index_0: int, debug:bool=False) -> int:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, index_0: int,_gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: end_time")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, end_time: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, end_time. Reason: Unknown")


    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class KeyFinalPriceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the key_final_price method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("key_final_price")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: key_final_price")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, key_final_price: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, key_final_price. Reason: Unknown")


    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class KeyIncreasingPriceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the key_increasing_price method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("key_increasing_price")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: key_increasing_price")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, key_increasing_price: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, key_increasing_price. Reason: Unknown")


    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class KeyInitPriceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the key_init_price method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("key_init_price")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: key_init_price")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, key_init_price: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, key_init_price. Reason: Unknown")


    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class NonceOfMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the nonceOf method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("nonceOf")

    def validate_and_normalize_inputs(self, account: str)->any:
        """Validate the inputs to the nonceOf method."""
        self.validator.assert_valid(
            method_name='nonceOf',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (account)



    def block_call(self,account: str, debug:bool=False) -> int:
        _fn = self._underlying_method(account)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, account: str,_gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(account)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: nonce_of")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, nonce_of: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, nonce_of. Reason: Unknown")


    def send_transaction(self, account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(self, account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(tx_params.as_dict())

class OwnerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the owner method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("owner")



    def block_call(self, debug:bool=False) -> str:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, _gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: owner")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, owner: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, owner. Reason: Unknown")


    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class RoundsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the rounds method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("rounds")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: rounds")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, rounds: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, rounds. Reason: Unknown")


    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class SetActionTimeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setActionTime method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setActionTime")

    def validate_and_normalize_inputs(self, time: int)->any:
        """Validate the inputs to the setActionTime method."""
        self.validator.assert_valid(
            method_name='setActionTime',
            parameter_name='_time',
            argument_value=time,
        )
        # safeguard against fractional inputs
        time = int(time)
        return (time)



    def block_send(self, time: int,_gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(time)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_action_time")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_action_time: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_action_time. Reason: Unknown")


    def send_transaction(self, time: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (time) = self.validate_and_normalize_inputs(time)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time).transact(tx_params.as_dict())

    def build_transaction(self, time: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (time) = self.validate_and_normalize_inputs(time)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, time: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (time) = self.validate_and_normalize_inputs(time)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time).estimateGas(tx_params.as_dict())

class StartTimeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the start_time method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("start_time")

    def validate_and_normalize_inputs(self, index_0: int)->any:
        """Validate the inputs to the start_time method."""
        self.validator.assert_valid(
            method_name='start_time',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)



    def block_call(self,index_0: int, debug:bool=False) -> int:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, index_0: int,_gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: start_time")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, start_time: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, start_time. Reason: Unknown")


    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class TeamMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the team method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("team")

    def validate_and_normalize_inputs(self, index_0: str, index_1: int)->any:
        """Validate the inputs to the team method."""
        self.validator.assert_valid(
            method_name='team',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name='team',
            parameter_name='index_1',
            argument_value=index_1,
        )
        # safeguard against fractional inputs
        index_1 = int(index_1)
        return (index_0, index_1)



    def block_call(self,index_0: str, index_1: int, debug:bool=False) -> int:
        _fn = self._underlying_method(index_0, index_1)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, index_0: str, index_1: int,_gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0, index_1)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: team")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, team: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, team. Reason: Unknown")


    def send_transaction(self, index_0: str, index_1: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, index_1: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, index_1: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(tx_params.as_dict())

class VaultBuyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the vaultBuy method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("vaultBuy")

    def validate_and_normalize_inputs(self, buy_num: int, team: int, rounds: int, account: str, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str])->any:
        """Validate the inputs to the vaultBuy method."""
        self.validator.assert_valid(
            method_name='vaultBuy',
            parameter_name='_buy_num',
            argument_value=buy_num,
        )
        # safeguard against fractional inputs
        buy_num = int(buy_num)
        self.validator.assert_valid(
            method_name='vaultBuy',
            parameter_name='_team',
            argument_value=team,
        )
        self.validator.assert_valid(
            method_name='vaultBuy',
            parameter_name='_rounds',
            argument_value=rounds,
        )
        # safeguard against fractional inputs
        rounds = int(rounds)
        self.validator.assert_valid(
            method_name='vaultBuy',
            parameter_name='_account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='vaultBuy',
            parameter_name='nonce',
            argument_value=nonce,
        )
        # safeguard against fractional inputs
        nonce = int(nonce)
        self.validator.assert_valid(
            method_name='vaultBuy',
            parameter_name='v',
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name='vaultBuy',
            parameter_name='r',
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name='vaultBuy',
            parameter_name='s',
            argument_value=s,
        )
        return (buy_num, team, rounds, account, nonce, v, r, s)



    def block_send(self, buy_num: int, team: int, rounds: int, account: str, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str],_gaswei:int,_pricewei:int,_valeth:int=0,_debugtx: bool = False,_receipList: bool = False) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(buy_num, team, rounds, account, nonce, v, r, s)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': _gaswei,
                'gasPrice': _pricewei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if _debugtx:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if _receipList is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.waitForTransactionReceipt(txHash)
                    if _debugtx:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                print(f"======== TX blockHash ✅")
                if tx_receipt is not None:
                    print(f"{Bolors.OK}{tx_receipt.blockHash.hex()}{Bolors.RESET}")
                else:
                    print(f"{Bolors.WARNING}{txHash.hex()}{Bolors.RESET} - broadcast hash")

            if _receipList is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: vault_buy")

        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, vault_buy: {message}")
            else:
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, vault_buy. Reason: Unknown")


    def send_transaction(self, buy_num: int, team: int, rounds: int, account: str, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (buy_num, team, rounds, account, nonce, v, r, s) = self.validate_and_normalize_inputs(buy_num, team, rounds, account, nonce, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(buy_num, team, rounds, account, nonce, v, r, s).transact(tx_params.as_dict())

    def build_transaction(self, buy_num: int, team: int, rounds: int, account: str, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (buy_num, team, rounds, account, nonce, v, r, s) = self.validate_and_normalize_inputs(buy_num, team, rounds, account, nonce, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(buy_num, team, rounds, account, nonce, v, r, s).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, buy_num: int, team: int, rounds: int, account: str, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (buy_num, team, rounds, account, nonce, v, r, s) = self.validate_and_normalize_inputs(buy_num, team, rounds, account, nonce, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(buy_num, team, rounds, account, nonce, v, r, s).estimateGas(tx_params.as_dict())

class SignatureGenerator(Signatures):
    """
        The signature is generated for this and it is installed.
    """
    def __init__(self, abi: any):
        super().__init__(abi)

    def claim_transaction_typehash(self) -> str:
        return self._function_signatures["CLAIM_TRANSACTION_TYPEHASH"]
    def domain_separator(self) -> str:
        return self._function_signatures["DOMAIN_SEPARATOR"]
    def eip712_domain_typehash(self) -> str:
        return self._function_signatures["EIP712_DOMAIN_TYPEHASH"]
    def vaultbuy_transaction_typehash(self) -> str:
        return self._function_signatures["VAULTBUY_TRANSACTION_TYPEHASH"]
    def bnb_buy(self) -> str:
        return self._function_signatures["bnbBuy"]
    def claim(self) -> str:
        return self._function_signatures["claim"]
    def end_time(self) -> str:
        return self._function_signatures["end_time"]
    def key_final_price(self) -> str:
        return self._function_signatures["key_final_price"]
    def key_increasing_price(self) -> str:
        return self._function_signatures["key_increasing_price"]
    def key_init_price(self) -> str:
        return self._function_signatures["key_init_price"]
    def nonce_of(self) -> str:
        return self._function_signatures["nonceOf"]
    def owner(self) -> str:
        return self._function_signatures["owner"]
    def rounds(self) -> str:
        return self._function_signatures["rounds"]
    def set_action_time(self) -> str:
        return self._function_signatures["setActionTime"]
    def start_time(self) -> str:
        return self._function_signatures["start_time"]
    def team(self) -> str:
        return self._function_signatures["team"]
    def vault_buy(self) -> str:
        return self._function_signatures["vaultBuy"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class fomo3d(ContractBase):
    """Wrapper class for fomo3d Solidity contract."""
    _fn_claim_transaction_typehash: ClaimTransactionTypehashMethod
    """Constructor-initialized instance of
    :class:`ClaimTransactionTypehashMethod`.
    """

    _fn_domain_separator: DomainSeparatorMethod
    """Constructor-initialized instance of
    :class:`DomainSeparatorMethod`.
    """

    _fn_eip712_domain_typehash: Eip712DomainTypehashMethod
    """Constructor-initialized instance of
    :class:`Eip712DomainTypehashMethod`.
    """

    _fn_vaultbuy_transaction_typehash: VaultbuyTransactionTypehashMethod
    """Constructor-initialized instance of
    :class:`VaultbuyTransactionTypehashMethod`.
    """

    _fn_bnb_buy: BnbBuyMethod
    """Constructor-initialized instance of
    :class:`BnbBuyMethod`.
    """

    _fn_claim: ClaimMethod
    """Constructor-initialized instance of
    :class:`ClaimMethod`.
    """

    _fn_end_time: EndTimeMethod
    """Constructor-initialized instance of
    :class:`EndTimeMethod`.
    """

    _fn_key_final_price: KeyFinalPriceMethod
    """Constructor-initialized instance of
    :class:`KeyFinalPriceMethod`.
    """

    _fn_key_increasing_price: KeyIncreasingPriceMethod
    """Constructor-initialized instance of
    :class:`KeyIncreasingPriceMethod`.
    """

    _fn_key_init_price: KeyInitPriceMethod
    """Constructor-initialized instance of
    :class:`KeyInitPriceMethod`.
    """

    _fn_nonce_of: NonceOfMethod
    """Constructor-initialized instance of
    :class:`NonceOfMethod`.
    """

    _fn_owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    _fn_rounds: RoundsMethod
    """Constructor-initialized instance of
    :class:`RoundsMethod`.
    """

    _fn_set_action_time: SetActionTimeMethod
    """Constructor-initialized instance of
    :class:`SetActionTimeMethod`.
    """

    _fn_start_time: StartTimeMethod
    """Constructor-initialized instance of
    :class:`StartTimeMethod`.
    """

    _fn_team: TeamMethod
    """Constructor-initialized instance of
    :class:`TeamMethod`.
    """

    _fn_vault_buy: VaultBuyMethod
    """Constructor-initialized instance of
    :class:`VaultBuyMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: fomo3dValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__()
        self.contract_address = contract_address
        web3 = core_lib.w3

        if not validator:
            validator = fomo3dValidator(web3, contract_address)




        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                         middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._web3_eth = web3.eth
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=fomo3d.abi()).functions
        signed = SignatureGenerator(fomo3d.abi())
        validator.bindSignatures(signed)
        self.SIGNATURES = signed
        self._fn_claim_transaction_typehash = ClaimTransactionTypehashMethod(core_lib, contract_address, functions.CLAIM_TRANSACTION_TYPEHASH, validator)
        self._fn_domain_separator = DomainSeparatorMethod(core_lib, contract_address, functions.DOMAIN_SEPARATOR, validator)
        self._fn_eip712_domain_typehash = Eip712DomainTypehashMethod(core_lib, contract_address, functions.EIP712_DOMAIN_TYPEHASH, validator)
        self._fn_vaultbuy_transaction_typehash = VaultbuyTransactionTypehashMethod(core_lib, contract_address, functions.VAULTBUY_TRANSACTION_TYPEHASH, validator)
        self._fn_bnb_buy = BnbBuyMethod(core_lib, contract_address, functions.bnbBuy, validator)
        self._fn_claim = ClaimMethod(core_lib, contract_address, functions.claim, validator)
        self._fn_end_time = EndTimeMethod(core_lib, contract_address, functions.end_time, validator)
        self._fn_key_final_price = KeyFinalPriceMethod(core_lib, contract_address, functions.key_final_price, validator)
        self._fn_key_increasing_price = KeyIncreasingPriceMethod(core_lib, contract_address, functions.key_increasing_price, validator)
        self._fn_key_init_price = KeyInitPriceMethod(core_lib, contract_address, functions.key_init_price, validator)
        self._fn_nonce_of = NonceOfMethod(core_lib, contract_address, functions.nonceOf, validator)
        self._fn_owner = OwnerMethod(core_lib, contract_address, functions.owner, validator)
        self._fn_rounds = RoundsMethod(core_lib, contract_address, functions.rounds, validator)
        self._fn_set_action_time = SetActionTimeMethod(core_lib, contract_address, functions.setActionTime, validator)
        self._fn_start_time = StartTimeMethod(core_lib, contract_address, functions.start_time, validator)
        self._fn_team = TeamMethod(core_lib, contract_address, functions.team, validator)
        self._fn_vault_buy = VaultBuyMethod(core_lib, contract_address, functions.vaultBuy, validator)

    
    
    def event_bnb_buy(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event bnb_buy in contract fomo3d
        Get log entry for BnbBuy event.
                :param tx_hash: hash of transaction emitting BnbBuy event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=fomo3d.abi()).events.BnbBuy().processReceipt(tx_receipt)
    
    
    def event_claim(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event claim in contract fomo3d
        Get log entry for Claim event.
                :param tx_hash: hash of transaction emitting Claim event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=fomo3d.abi()).events.Claim().processReceipt(tx_receipt)
    
    
    def event_vault_buy(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event vault_buy in contract fomo3d
        Get log entry for VaultBuy event.
                :param tx_hash: hash of transaction emitting VaultBuy event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=fomo3d.abi()).events.VaultBuy().processReceipt(tx_receipt)

    
    
    
    def claim_transaction_typehash(self) -> Union[bytes, str]:
        """
        Implementation of claim_transaction_typehash in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_claim_transaction_typehash.block_call()
    
    
    
    def domain_separator(self) -> Union[bytes, str]:
        """
        Implementation of domain_separator in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_domain_separator.block_call()
    
    
    
    def eip712_domain_typehash(self) -> Union[bytes, str]:
        """
        Implementation of eip712_domain_typehash in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_eip712_domain_typehash.block_call()
    
    
    
    def vaultbuy_transaction_typehash(self) -> Union[bytes, str]:
        """
        Implementation of vaultbuy_transaction_typehash in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_vaultbuy_transaction_typehash.block_call()
    
    
    
    def bnb_buy(self, buy_num: int, team: int, rounds: int, wei:int=0) -> None:
        """
        Implementation of bnb_buy in contract fomo3d
        Method of the function
    
    
    
        """
    
    
        return self._fn_bnb_buy.block_send(buy_num, team, rounds, self.call_contract_fee_amount,self.call_contract_fee_price,wei,self.call_contract_debug_flag,self.call_contract_enforce_tx_receipt)
    
    
    
    
    
    
    def claim(self, account: str, number: int, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str]) -> None:
        """
        Implementation of claim in contract fomo3d
        Method of the function
    
    
    
        """
    
        return self._fn_claim.block_send(account, number, nonce, v, r, s, self.call_contract_fee_amount,self.call_contract_fee_price,0,self.call_contract_debug_flag, self.call_contract_enforce_tx_receipt)
    
    
    
    
    
    
    
    def end_time(self, index_0: int) -> int:
        """
        Implementation of end_time in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_end_time.block_call(index_0)
    
    
    
    def key_final_price(self) -> int:
        """
        Implementation of key_final_price in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_key_final_price.block_call()
    
    
    
    def key_increasing_price(self) -> int:
        """
        Implementation of key_increasing_price in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_key_increasing_price.block_call()
    
    
    
    def key_init_price(self) -> int:
        """
        Implementation of key_init_price in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_key_init_price.block_call()
    
    
    
    def nonce_of(self, account: str) -> int:
        """
        Implementation of nonce_of in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_nonce_of.block_call(account)
    
    
    
    def owner(self) -> str:
        """
        Implementation of owner in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_owner.block_call()
    
    
    
    def rounds(self) -> int:
        """
        Implementation of rounds in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_rounds.block_call()
    
    
    
    def set_action_time(self, time: int) -> None:
        """
        Implementation of set_action_time in contract fomo3d
        Method of the function
    
    
    
        """
    
        return self._fn_set_action_time.block_send(time, self.call_contract_fee_amount,self.call_contract_fee_price,0,self.call_contract_debug_flag, self.call_contract_enforce_tx_receipt)
    
    
    
    
    
    
    
    def start_time(self, index_0: int) -> int:
        """
        Implementation of start_time in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_start_time.block_call(index_0)
    
    
    
    def team(self, index_0: str, index_1: int) -> int:
        """
        Implementation of team in contract fomo3d
        Method of the function
    
    
    
        """
    
    
    
    
    
        return self._fn_team.block_call(index_0, index_1)
    
    
    
    def vault_buy(self, buy_num: int, team: int, rounds: int, account: str, nonce: int, v: int, r: Union[bytes, str], s: Union[bytes, str], wei:int=0) -> None:
        """
        Implementation of vault_buy in contract fomo3d
        Method of the function
    
    
    
        """
    
    
        return self._fn_vault_buy.block_send(buy_num, team, rounds, account, nonce, v, r, s, self.call_contract_fee_amount,self.call_contract_fee_price,wei,self.call_contract_debug_flag,self.call_contract_enforce_tx_receipt)
    
    
    

    def CallContractWait(self, t_long:int)-> "fomo3d":
        self._fn_claim_transaction_typehash.setWait(t_long)
        self._fn_domain_separator.setWait(t_long)
        self._fn_eip712_domain_typehash.setWait(t_long)
        self._fn_vaultbuy_transaction_typehash.setWait(t_long)
        self._fn_bnb_buy.setWait(t_long)
        self._fn_claim.setWait(t_long)
        self._fn_end_time.setWait(t_long)
        self._fn_key_final_price.setWait(t_long)
        self._fn_key_increasing_price.setWait(t_long)
        self._fn_key_init_price.setWait(t_long)
        self._fn_nonce_of.setWait(t_long)
        self._fn_owner.setWait(t_long)
        self._fn_rounds.setWait(t_long)
        self._fn_set_action_time.setWait(t_long)
        self._fn_start_time.setWait(t_long)
        self._fn_team.setWait(t_long)
        self._fn_vault_buy.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"bnbvalue","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"buy_num","type":"uint256"},{"indexed":false,"internalType":"enum fomo3d.group","name":"team","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"rounds","type":"uint256"}],"name":"BnbBuy","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"claimvalue","type":"uint256"}],"name":"Claim","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"vaultvalue","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"buy_num","type":"uint256"},{"indexed":false,"internalType":"enum fomo3d.group","name":"team","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"rounds","type":"uint256"}],"name":"VaultBuy","type":"event"},{"inputs":[],"name":"CLAIM_TRANSACTION_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"EIP712_DOMAIN_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"VAULTBUY_TRANSACTION_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_buy_num","type":"uint256"},{"internalType":"enum fomo3d.group","name":"_team","type":"uint8"},{"internalType":"uint64","name":"_rounds","type":"uint64"}],"name":"bnbBuy","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_account","type":"address"},{"internalType":"uint256","name":"_number","type":"uint256"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"end_time","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"key_final_price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"key_increasing_price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"key_init_price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"nonceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rounds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_time","type":"uint256"}],"name":"setActionTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"start_time","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"uint256","name":"index_1","type":"uint256"}],"name":"team","outputs":[{"internalType":"enum fomo3d.group","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_buy_num","type":"uint256"},{"internalType":"enum fomo3d.group","name":"_team","type":"uint8"},{"internalType":"uint256","name":"_rounds","type":"uint256"},{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"vaultBuy","outputs":[],"stateMutability":"payable","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
