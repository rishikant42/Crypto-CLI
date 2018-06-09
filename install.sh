#!/bin/bash
chmod a+x cryptoo
chmod a+x src/crypto.py
cp cryptoo /usr/local/bin/
cp cryptoo.1 /usr/local/share/man/man1/
echo "cryptoo CLI is successfully installed"
