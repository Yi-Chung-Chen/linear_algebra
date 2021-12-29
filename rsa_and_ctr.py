from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util import Counterrsa and ctr
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import base64
import hashlib

#aes加密
plaintext ='ThisIsMyHomeWork'
AES_key = get_random_bytes(16)
with open("AES_key", 'wb+') as f:
    f.write(AES_key)
cipherAES_enc = AES.new(AES_key,AES.MODE_CTR,counter=Counter.new(128))
AES_ciphertext = cipherAES_enc.encrypt(plaintext.encode('utf-8'))

#rsa
random_generator = Random.new().read
rsa = RSA.generate(2048, random_generator)
 
private_key = rsa.exportKey()
with open("private_a.rsa", 'wb') as f:
    f.write(private_key)
 
public_key = rsa.publickey().exportKey()
with open("public_a.rsa", 'wb') as f:
    f.write(public_key)
 
# 公鑰加密
with open('public_a.rsa') as f:
    key = f.read()
    change = str(AES_key)
    pub_key = RSA.importKey(str(key))
    cipher = PKCS1_cipher.new(pub_key)
    rsa_text = base64.b64encode(cipher.encrypt(change.encode('utf-8')))

 
# 私鑰解密
with open('private_a.rsa') as f:
    key = f.read()
    pri_key = RSA.importKey(key)
    cipher = PKCS1_cipher.new(pri_key)
    back_text = cipher.decrypt(base64.b64decode(rsa_text),"fail")
    print("-------------------------------------two--------------------------------------------")
    print(back_text.decode('utf-8'))
    print(AES_key)



#AES_CTR解密
cipherAES_dec = AES.new(back_text.decode('utf-8'),AES.MODE_CTR,counter=Counter.new(128))
AES_plaintext = cipherAES_dec.decrypt(AES_ciphertext)
print("這是AES_CTR解密後的明文:")
print(AES_plaintext)
