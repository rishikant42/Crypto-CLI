from ast import literal_eval

from Crypto.Cipher import DES3

from keys_handler import generate_key_pairs, import_key

def encrypt(key_file, in_file):
    key = import_key(key_file)
    plain_text = open(in_file, 'r').read()
    cipher = key.encrypt(plain_text, 32)
    cipher_file = open('cipher.txt', 'w')
    cipher_file.write(str(cipher))
    cipher_file.close()
    return "Cipher file for given plain file is successfully created"

def decrypt(key_file, cipher_file):
    key = import_key(key_file)
    cipher_text = open(cipher_file, 'r').read()
    cipher = literal_eval(cipher_text)
    plain_text = key.decrypt(cipher)

    plain_file = open('plain.txt', 'w')
    plain_file.write(plain_text)
    plain_file.close()
    return "Plain file for given cipher file is successfully created"

def enc_des3(secret, in_file):
    if len(secret) > 16:
        return "Error: Secret length should be less than 16 char"

    if len(secret) < 16:
        secret += ' '*(16-len(secret))

    plain_text = open(in_file, 'r').read()

    if len(plain_text) % 8 != 0:
        plain_text += ' '*(8 - (len(plain_text) % 8))

    # iv = Random.new().read(DES3.block_size) #DES3.block_size==8
    iv = 'aaaaaaaa'
    key = DES3.new(secret, DES3.MODE_OFB, iv)

    cipher = key.encrypt(plain_text)
    cipher_file = open('cipher.txt', 'w')
    cipher_file.write(str(cipher))
    cipher_file.close()
    return "Cipher file for given plain file is successfully created"

def dec_des3(secret, cipher_file):
    if len(secret) > 16:
        return "Error: Secret length should be less than 16 char"

    if len(secret) < 16:
        secret += ' '*(16-len(secret))

    cipher_text = open(cipher_file, 'r').read()

    iv = 'aaaaaaaa'
    key = DES3.new(secret, DES3.MODE_OFB, iv)

    plain_text = key.decrypt(cipher_text)
    plain_text = plain_text.rstrip() + '\n'
    plain_file = open('plain.txt', 'w')
    plain_file.write(str(plain_text))
    plain_file.close()
    return "Plain file for given cipher file is successfully created"
