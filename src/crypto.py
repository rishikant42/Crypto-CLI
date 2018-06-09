#!/usr/bin/python2.7

import argparse
from sys import argv

from hash_handler import generate_hash, verify_hash
from keys_handler import generate_key_pairs, import_key
from encrypt_decrypt_handler import encrypt, decrypt, enc_des3, dec_des3

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
