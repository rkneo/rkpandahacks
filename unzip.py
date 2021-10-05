import pyzipper
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

secret_password = b'lost art of keeping a secret'

with pyzipper.AESZipFile('new_test.zip',
                         'w',
                         compression=pyzipper.ZIP_LZMA,
                         encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(secret_password)
    zf.writestr('test.txt', "What ever you do, don't tell anyone!")

with pyzipper.AESZipFile('new_test.zip') as zf:
    zf.setpassword(secret_password)
    my_secrets = zf.read('test.txt')


while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
         pass


cipher = DES3.new(key, DES3.MODE_CFB)
plaintext = b'We are no longer the knights who say ni!'
msg = cipher.iv + cipher.encrypt(plaintext)
print(msg)