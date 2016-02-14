#!/usr/bin/env python
import sys

def get_bytes(write_byte, already_written):

    write_byte = write_byte + 0x100
    already_written = already_written % 0x100

    padding = (write_byte - already_written) % 0x100
    if padding < 10:
        padding = padding + 0x100
    return padding

if __name__ == '__main__':
    if len(sys.argv) < 5:
        sys.exit('need addrs')
    already_written = 0
    if len(sys.argv) == 6:
        already_written = int(sys.argv[5])
    args = [ int(sys.argv[i], 16) for i in range(1, 5) ]
    for i in args:
        padding = get_bytes(i, already_written)
        already_written = already_written + padding
        print (already_written, padding)
