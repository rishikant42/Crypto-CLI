from Crypto.Hash import SHA256, SHA512, MD5

def generate_hash(msg, algo='sha256'):
    if algo == 'sha256':
        digest = SHA256.new(msg).hexdigest()

    elif algo == 'sha512':
        digest = SHA512.new(msg).hexdigest()

    elif algo == 'md5':
        digest = MD5.new(msg).hexdigest()

    else:
        digest = "Unknown algorithm"

    return digest

def verify_hash(msg, input_digest, algo='sha256'):
    if algo == 'sha256':
        msg_digest = SHA256.new(msg).hexdigest()

    elif algo == 'sha512':
        msg_digest = SHA512.new(msg).hexdigest()

    elif algo == 'md5':
        msg_digest = MD5.new(msg).hexdigest()

    else:
        msg_digest = "Unknow Algorithm"

    if msg_digest == input_digest:
        return True

    return False

