# Crypto-CLI

A `cryptoo` Unix/Linux CLI to perform cryptographic operations. Source code is written in Python. 

---

### Features:
```
* Support multiple hash algorithms(sha256, sha512, md5).

* Symmetric encryption/decryption.

* Asymmetric encryption (Public key cryptography).

* Digital signature & verification.

* Fancy bash(tab) completion. Yes, Its really fancy.

* Manual page ($ man cryptoo).
```
### Install instructions:
```
$ git clone https://github.com/rishikant42/Crypto-CLI
$ cd Crypto-CLI
$ ./install.sh

Add following lines to ~/.bashrc (or ~/.bash_profile)

if [ -f /usr/local/etc/bash_completion.d/cryptoo ]; then
  source /usr/local/etc/bash_completion.d/cryptoo
fi

Or do copy-paste given line in your shell

echo "if [ -f /usr/local/etc/bash_completion.d/cryptoo ]; then source /usr/local/etc/bash_completion.d/cryptoo; fi" >> ~/.bash_profile
```

### Examples:

### Cryptographic Hash

```
$ cryptoo generate_hash --msg mypassword
89e01536ac207279409d4de1e5253e01f4a1769e696db0d6062ca9b8f56767c8

$ cryptoo verify_hash --msg mypassword --digest 89e01536ac207279409d4de1e5253e01f4a1769e696db0d6062ca9b8f56767c8
True
```

==> Can specify hashing algorithm from command line. Current choices are `sha256, sha512 and md5`. Default hashing algo is `sha256`.

```
$ cryptoo generate_hash --msg mypassword --algo md5
34819d7beeabb9260a5c854bc85b3e44

$ cryptoo verify_hash --msg mypassword --digest 34819d7beeabb9260a5c854bc85b3e44 --algo md5
True
```

### Symmetric encryption (Algo: DES3)

```
* Lets create a simple plaintext file for test

$ echo "Hello world" > in.txt

$ cryptoo enc_des3 --textfile in.txt --secret mysecret
Ciphertext file 'cipher.txt' is successfully created

$ ls cipher.txt
cipher.txt

 $ cryptoo dec_des3 --cipherfile cipher.txt --secret mysecret
Plaintext file 'plain.txt' is successfully created

$ cat plain.txt
Hello world
```

### Public key cryptography(Algo: RSA)

```
$ echo "Hello world" > in.txt

* Lets create a private-public key pairs

$ cryptoo generate_key_pairs
Private-Public key pairs (pvtkey.pem & pubkey.pem) are successfully created

$ ls pvtkey.pem pubkey.pem
pubkey.pem	pvtkey.pem

$ cryptoo encrypt --textfile in.txt --pubkey pubkey.pem
Ciphertext file 'cipher.txt' is successfully created

$ cryptoo decrypt --cipherfile cipher.txt --pvtkey pvtkey.pem 
Plaintext file 'plain.txt' is successfully created

$ cat plain.txt
Hello world
```

### Digital sign & verify

```
$ echo "Hello world" > in.txt
$ cryptoo generate_key_pairs
Private-Public key pairs (pvtkey.pem & pubkey.pem) are successfully created

$ cryptoo sign --pvtkey pvtkey.pem --textfile in.txt
Signature file 'sign.txt' is successfully created

$ ls sign.txt
sign.txt

$ cryptoo sign_verify --pubkey pubkey.pem --textfile in.txt --signfile sign.txt 
True
```

### Uninstall instructions:
```
$ ./uninstall.sh

    OR

$ make uninstall
```

### ToDo:
```
* Large size file encryption-decryption.

* Proper error handling.

* Implementation of JWT.

* Option to specify name of output file.

* Option to pass text from command line.

* More hashing algo choices.

```

### License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
