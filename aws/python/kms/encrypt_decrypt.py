import boto3
session = boto3.Session(region_name='us-east-1', profile_name='default')
kms = session.client('kms')

def encrypt(plaintext):
    ciphertext = kms.encrypt(KeyId='alias/mykey', Plaintext=plaintext)
    encoded_ciphertext = base64.b64encode(ciphertext["CiphertextBlob"])
    return encoded_ciphertext.decode('utf-8')
  
def decrypt(encoded_ciphertext):
    decoded_ciphertext = base64.b64decode(encoded_ciphertext)
    plaintext = kms.decrypt(CiphertextBlob=bytes(decoded_ciphertext))
    return plaintext['Plaintext'].decode('utf-8')

"""
>>> a = encrypt('hello')
>>> a
'AQICAHgQYMmngPUi9lcJeng2A12tVdu[shortened]2XY1wT3t1zreJg2KEF8vZmYykJBc8g=='

>>> b = decrypt(a)
>>> b
'hello'
"""
