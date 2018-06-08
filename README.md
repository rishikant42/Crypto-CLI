# Crypto-CLI

A `cryptoo` Unix/Linux CLI to perform cryptographic operations. Source code is written in Python.

---

### Prerequisite:
* `pip`: https://pypi.org/project/pip/
* System should have `pip` CLI

---

### Install instructions:
```
$ git clone https://github.com/rishikant42/Crypto-CLI
$ cd Crypto-CLI
$ ./install.sh
```

### Example:

```
$ cryptoo generate_hash --msg mypassword
89e01536ac207279409d4de1e5253e01f4a1769e696db0d6062ca9b8f56767c8

$ cryptoo verify_hash --msg mypassword --digest 89e01536ac207279409d4de1e5253e01f4a1769e696db0d6062ca9b8f56767c8
True

$ cryptoo generate_key_pairs
Private-Public key pairs are successfully created

$ ls pubkey.pem pvtkey.pem
pubkey.pem  pvtkey.pem

$ echo "Hello World" > in.txt

$ cryptoo encrypt --in in.txt --pubkey pubkey.pem
Cipher file for given plain file is successfully created

$ ls cipher.txt
cipher.txt

$ decrypt --in cipher.txt --pvtkey pvtkey.pem
Plain file for given cipher file is successfully created

$ cat plain.txt
Hello World
```
