import argparse
from sys import argv
from Crypto.Hash import SHA256

def generate_hash(msg):
    digest = SHA256.new(msg).hexdigest()
    return digest

def verify_hash(msg, input_digest):
    msg_digest = SHA256.new(msg).hexdigest()
    if msg_digest == input_digest:
        return True
    return False

def main():
    parser = argparse.ArgumentParser("A CLI to perform cryptographic operations")
    subparsers = parser.add_subparsers()

    parser_generate_hash = subparsers.add_parser('generate_hash')
    parser_generate_hash.add_argument("-m", "--msg", nargs="?")

    parser_verify_hash = subparsers.add_parser('verify_hash')
    parser_verify_hash.add_argument("-m", "--msg", nargs="?")
    parser_verify_hash.add_argument("-d", "--digest", nargs="?")

    args = parser.parse_args()

    subcommand = argv[1]
    if subcommand == 'generate_hash':
        return generate_hash(args.msg)

    elif subcommand == 'verify_hash':
        return verify_hash(args.msg, args.digest)

print main()
