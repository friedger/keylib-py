# -*- coding: utf-8 -*-
"""
    pybitcoin
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

from binascii import unhexlify, hexlify
from typing import Optional

from .b58check import b58check_encode, b58check_decode
from .hashing import bin_hash160


def bin_hash160_to_address(bin_hash160: bytes, version_byte: int = 0) -> bytes:
    return b58check_encode(bin_hash160, version_byte=version_byte)


def hex_hash160_to_address(hash160: bytes, version_byte: int = 0):
    return bin_hash160_to_address(
        unhexlify(hash160), version_byte=version_byte)


def script_hex_to_address(script: bytes, version_byte: int = 0) -> Optional[bytes]:
    if script[0:6] == b'76a914' and script[-4:] == b'88ac':
        bin_hash160 = unhexlify(script[6:-4])
        return bin_hash160_to_address(bin_hash160, version_byte=version_byte)
    return None


def address_to_bin_hash160(address: bytes) -> bytes:
    return b58check_decode(address)


def address_to_hex_hash160(address: bytes) -> bytes:
    return hexlify(address_to_bin_hash160(address))


def address_to_new_cryptocurrency(address: bytes, new_version_number: int):
    bin_hash160 = address_to_bin_hash160(address)
    return bin_hash160_to_address(bin_hash160, new_version_number)
