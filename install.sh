#!/bin/bash
pip install virtualenv
virtualenv /usr/local/bin/cryptoenv
source /usr/local/bin/cryptoenv/bin/activate
pip install -r requirements.txt
chmod a+x cryptoo
cp cryptoo /usr/local/bin/
cp cryptoo.1 /usr/local/share/man/man1/
echo "cryptoo CLI is successfully installed"
