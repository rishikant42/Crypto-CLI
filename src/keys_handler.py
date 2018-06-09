from Crypto import Random
from Crypto.PublicKey import RSA

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
