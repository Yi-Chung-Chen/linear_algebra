from Crypto import Cipher
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from Crypto.Cipher import AES,PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64



#aes encrypt
plaintext = 'sendmedown'
aes_key = get_random_bytes(16)
ctr = Counter.new(128)
aes_cipher = AES.new(aes_key,AES.MODE_CTR,counter = ctr)
aes_ciphertext = aes_cipher.encrypt(plaintext.encode('utf-8'))
with open('aes_ciphertext','wb') as f:
    f.write(aes_ciphertext)

#rsa private and public key generate

random_generator = Random.new().read
rsa = RSA.generate(1024,random_generator)

private_key = rsa.exportKey()
with open('private_key.pem','wb') as i :
    i.write(private_key)


public_key = rsa.publickey().exportKey()
with open('public_key.pem','wb') as j :
    j.write(public_key)

#encrypt aes key
with open('public_key.pem') as f :
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    aes_key_encrypt = base64.b64encode(cipher.encrypt(aes_key))
with open ('aes_key_encrpyt','wb') as f :
    f.write(aes_key_encrypt)

#decrypt aes key
with open('private_key.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    aes_key_decrypt = cipher.decrypt(base64.b64decode(aes_key_encrypt), random_generator)

#aes decrypt
cipherAES_decrypt = AES.new(aes_key_decrypt,AES.MODE_CTR,counter=ctr)
AES_plaintext = cipherAES_decrypt.decrypt(aes_ciphertext)
print("這是原文：",plaintext)
print("----------------------------------------")
print("這是隨機產生的aes_key：",aes_key)
print("----------------------------------------")
print("這是rsa加密後的aes_key：",aes_key_encrypt)
print("----------------------------------------")
print("這是公鑰：",public_key)
print("----------------------------------------")
print("這是私鑰：",private_key)
print("----------------------------------------")
print("這是rsa解密後的aes_key：",aes_key_decrypt)
print("----------------------------------------")
print("這是解完密後的plaintext",str(AES_plaintext))