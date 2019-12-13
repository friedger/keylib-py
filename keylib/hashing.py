# -*- coding: utf-8 -*-
"""
    pybitcoin
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import hashlib
from hashlib import sha256
from binascii import hexlify, unhexlify
from utilitybelt import is_hex


def bin_sha256(bin_s: bytes) -> bytes:
    return sha256(bin_s).digest()


def bin_checksum(bin_s: bytes) -> bytes:
    """ Takes in a binary string and returns a checksum. """
    return bin_sha256(bin_sha256(bin_s))[:4]


def bin_double_sha256(bin_s: bytes) -> bytes:
    return bin_sha256(bin_sha256(bin_s))


def bin_hash160(s: bytes, hex_format=False) -> bytes:
    """ s is in hex or binary format
    """
    if hex_format and is_hex(s):
        s = unhexlify(s)
    return hashlib.new('ripemd160', bin_sha256(s)).digest()


def hex_hash160(s: bytes, hex_format=False) -> bytes:
    """ s is in hex or binary format
    """
    if hex_format and is_hex(s):
        s = unhexlify(s)
    return hexlify(bin_hash160(s))


def reverse_hash(hash: bytes, hex_format=True) -> bytes:
    """ hash is in hex or binary format
    """
    if not hex_format:
        hash = hexlify(hash)
    return b"".join(reversed([hash[i:i+2] for i in range(0, len(hash), 2)]))


def hex_to_bin_reversed(s: bytes) -> bytes:
    return unhexlify(s)[::-1]


def bin_to_hex_reversed(s: bytes) -> bytes:
    return hexlify(s[::-1])