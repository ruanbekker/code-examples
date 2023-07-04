#!/usr/bin/env python3

"""
pip install eth_keys
pip install eth-hash[pycryptodome]
"""

import os
from eth_keys import keys

private_key = keys.PrivateKey(os.urandom(32))

public_key = private_key.public_key
eth_address = public_key.to_checksum_address()

print(f"Private key: {private_key}")
print(f"Public key: {public_key}")
print(f"Ethereum address: {eth_address}")

"""
Validate:
curl -XPOST -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0x746C9474d98C8A99280fC0E9DA7d706B647163DE", "latest"],"id":1}' http://localhost:8545
"""
