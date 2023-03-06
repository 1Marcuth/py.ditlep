from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
import base64
import json

def decrypt_data(encrypted_data):
    iv = bytes.fromhex("e84ad660c4721ae0e84ad660c4721ae0")
    password = "ZGl0bGVwLWRyYWdvbi1jaXR5".encode()
    salt = "ZGl0bGVwLWRyYWdvbi1jaXR5LXNhbHQ=".encode()

    key = PBKDF2(
        password,
        salt,
        dkLen=16,
        count=1000
    )

    cipher = AES.new(
        key,
        AES.MODE_CBC,
        iv
    )

    decrypted_data = unpad(
        cipher.decrypt(
            base64.b64decode(encrypted_data)
        ),
        AES.block_size
    )

    return json.loads(decrypted_data.decode())

__all__ = [ decrypt_data ]