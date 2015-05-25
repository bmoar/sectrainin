#!/usr/bin/env bash

ssh krypton1@krypton.labs.overthewire.org <<EOF
cd /krypton/krypton1 && cat krypton2 | python3 -c 'import sys; print("".join([ chr(ord(c) + 13) if ord(c) < 78 else chr(ord(c) - 13) for c in sys.stdin.read()]))'
EOF
