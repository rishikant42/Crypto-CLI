main:
	chmod a+x cryptoo
	chmod a+x src/crypto.py

install: main
	cp cryptoo /usr/local/bin/
	cp cryptoo.1 /usr/local/share/man/man1/
	echo "cryptoo CLI is successfully installed"

uninstall:
	rm /usr/local/bin/cryptoo
	rm /usr/local/share/man/man1/cryptoo.1
	echo "cryptoo CLI is successfully uninstalled"
