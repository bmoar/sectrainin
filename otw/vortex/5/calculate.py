#!/usr/bin/env python

def get_bytes(write_byte, already_written):

    write_byte = write_byte + 0x100
    already_written = already_written % 0x100

    padding = (write_byte - already_written) % 0x100
    if padding < 10:
        padding = padding + 0x100
    return padding

if __name__ == '__main__':
    already_written = 0
    for i in [0x7f, 0x7f, 0x7f, 0x7f]:
        padding = get_bytes(i, already_written)
        already_written = already_written + padding
        print (already_written, padding)
