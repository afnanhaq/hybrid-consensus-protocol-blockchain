from hashlib import sha256
from random import randint, choices

def create_hash(data):
    """
    Creates a SHA-256 hash of data
    :param string: data
    """
    sha_signature = sha256(data.encode()).hexdigest()
    return sha_signature

def proof_of_work_algo(last_hash, sha_signature):
        """
        Simple Proof of Work Algorithm:

         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof
        """

        proof = 0
        while valid_proof(last_hash, str(proof), sha_signature) is False:
            proof += 1
        
        return proof
    
def valid_proof(last_hash, proof, sha_signature):
        """
        Validates the Proof
        :return: <bool> True if correct, False if not.
        """

        guess = (last_hash + proof + sha_signature).encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
