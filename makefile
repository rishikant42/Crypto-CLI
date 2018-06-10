main:
	chmod a+x cryptoo
	chmod a+x src/crypto.py

install: main
	cp cryptoo /usr/local/bin/
	cp -r src /usr/local/bin/cryptoosrc
	cp cryptoo.1 /usr/local/share/man/man1/
	cp cryptoo_completion /usr/local/etc/bash_completion.d/cryptoo
	echo "cryptoo CLI is successfully installed"

uninstall:
	rm /usr/local/bin/cryptoo
	rm -rf /usr/local/bin/cryptoosrc
	rm /usr/local/share/man/man1/cryptoo.1
	rm /usr/local/etc/bash_completion.d/cryptoo
	echo "cryptoo CLI is successfully uninstalled"
