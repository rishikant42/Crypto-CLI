#!/bin/bash
chmod a+x cryptoo

chmod a+x src/crypto.py

cp cryptoo /usr/local/bin/

cp -r src /usr/local/bin/cryptoosrc

cp cryptoo.1 /usr/local/share/man/man1/

if [ ! -d /usr/local/etc/bash_completion.d/ ]; then
    mkdir -p /usr/local/etc/bash_completion.d
fi

cp cryptoo_completion /usr/local/etc/bash_completion.d/cryptoo

echo "cryptoo CLI is successfully installed"
