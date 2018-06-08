import argparse
from ast import literal_eval
from sys import argv

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import DES3
from Crypto import Random

from hash_handler import generate_hash, verify_hash

def generate_key_pairs():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    pvt_key = key.exportKey()
    pub_key = key.publickey().exportKey()

    pvt_key_file = open('pvtkey.pem', 'w')
    pvt_key_file.write(pvt_key)
    pvt_key_file.close()

    pub_key_file = open('pubkey.pem', 'w')
    pub_key_file.write(pub_key)
    pub_key_file.close()
    return "Private-Public key pairs are successfully created"

def import_key(file_name):
    key = open(file_name, 'r').read()
    key_object = RSA.importKey(key)
    return key_object

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

def main():
    parser = argparse.ArgumentParser("A CLI to perform cryptographic operations")
    subparsers = parser.add_subparsers()

    parser_generate_hash = subparsers.add_parser('generate_hash')
    parser_generate_hash.add_argument("-m", "--msg", nargs="?")
    parser_generate_hash.add_argument("-a", "--algo", nargs="?", default='sha256', choices=['md5', 'sha256', 'sha512'])

    parser_verify_hash = subparsers.add_parser('verify_hash')
    parser_verify_hash.add_argument("-m", "--msg", nargs="?")
    parser_verify_hash.add_argument("-d", "--digest", nargs="?")
    parser_verify_hash.add_argument("-a", "--algo", nargs="?", default='sha256', choices=['md5', 'sha256', 'sha512'])

    parser_generate_key_pairs = subparsers.add_parser('generate_key_pairs')

    parser_encrypt = subparsers.add_parser('encrypt')
    parser_encrypt.add_argument("-p", "--pubkey", nargs="?")
    parser_encrypt.add_argument("-i", "--infile", nargs="?")

    parser_decrypt = subparsers.add_parser('decrypt')
    parser_decrypt.add_argument("-p", "--pvtkey", nargs="?")
    parser_decrypt.add_argument("-i", "--infile", nargs="?")

    parser_enc_des3 = subparsers.add_parser('enc_des3')
    parser_enc_des3.add_argument("-s", "--secret", nargs="?")
    parser_enc_des3.add_argument("-i", "--infile", nargs="?")

    parser_dec_des3 = subparsers.add_parser('dec_des3')
    parser_dec_des3.add_argument("-s", "--secret", nargs="?")
    parser_dec_des3.add_argument("-i", "--infile", nargs="?")

    args = parser.parse_args()

    subcommand = argv[1]
    if subcommand == 'generate_hash':
        return generate_hash(args.msg, args.algo)

    elif subcommand == 'verify_hash':
        return verify_hash(args.msg, args.digest, args.algo)

    elif subcommand == 'generate_key_pairs':
        return generate_key_pairs()

    elif subcommand == 'encrypt':
        return encrypt(args.pubkey, args.infile)

    elif subcommand == 'decrypt':
        return decrypt(args.pvtkey, args.infile)

    elif subcommand == 'enc_des3':
        return enc_des3(args.secret, args.infile)

    elif subcommand == 'dec_des3':
        return dec_des3(args.secret, args.infile)

print main()
# print generate_key_pairs()

# print encrypt(argv[1], argv[2])
# print decrypt(argv[1], argv[2])
