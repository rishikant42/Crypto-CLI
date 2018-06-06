import argparse
from sys import argv
from Crypto.Hash import SHA256

def create_hash(text):
    digest = SHA256.new(text).hexdigest()
    return digest

def verify_hash(text, digest):
    text_digest = SHA256.new(text).hexdigest()
    if text_digest == digest:
        return True
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', nargs='?', default='create_hash', choices=['create_hash', 'verify_hash'])
    parser.add_argument("-t", "--text", help="pass string")
    parser.add_argument("-d", "--digest", help="pass string")
    args = parser.parse_args()
    if args.cmd == 'create_hash':
        return create_hash(str(args.text))

    elif args.cmd == 'verify_hash':
        return verify_hash(str(args.text), str(args.digest))

    else:
        return "Unknown action"

print main()
