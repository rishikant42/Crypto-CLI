from ast import literal_eval

from Crypto.Hash import SHA256

from keys_handler import import_key

def sign(key_file, in_file):
    key = import_key(key_file)
    if not key.has_private():
        return "Error: Pass private key to sign"
    text = open(in_file, 'r').read()
    hash_text = SHA256.new(text).digest()
    signature = key.sign(hash_text, '')

    sign_file = open('sign.txt', 'w')
    sign_file.write(str(signature))
    sign_file.close()
    return "Signature file 'sign.txt' is successfully created"


def sign_verify(key_file, sign_file, in_file):
    key = import_key(key_file)
    sign_text = open(sign_file, 'r').read()
    signature = literal_eval(sign_text)

    text = open(in_file, 'r').read()
    hash_text = SHA256.new(text).digest()

    if key.verify(hash_text, signature):
        return True

    return False
