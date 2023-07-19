from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import PIL

def generate_random_key():
    key = os.urandom(16)
    return key.hex()

def encrypt_message(key, message):
    backend = default_backend()

    iv = os.urandom(16)

    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()

    return iv + ciphertext

def decrypt_message(key, encrypted_message):
    backend = default_backend()

    iv = encrypted_message[:16]
    ciphertext = encrypted_message[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()

    return message.decode()

def encrypt_image(image_path, key, output_path):
    backend = default_backend()

    with open(image_path, "rb") as file:
        image_data = file.read()

    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    padded_data = padder.update(image_data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_image = iv + encrypted_data

    with open(output_path, "wb") as file:
        file.write(encrypted_image)

    return encrypted_image, output_path


def decrypt_image(encrypted_image_path, key, output_path):
    backend = default_backend()

    with open(encrypted_image_path, "rb") as file:
        encrypted_image_data = file.read()

    iv = encrypted_image_data[:16]
    encrypted_data = encrypted_image_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Save decrypted image
    with open(output_path, "wb") as file:
        file.write(unpadded_data)

    return unpadded_data


def main():
    key = bytes.fromhex("b402870f761608b2464145dd52fa3fb9")
    decrypt_image("aux_enc.png", key, "decrypted_image.png")
    #image_path = "img_cu_ms_cript.png"
    # encrypted_image = encrypt_image(image_path, key)
    #
    #
    # with open("imagine_cript_output.png", "wb") as file:
    #     file.write(encrypted_image)

    #decrypt_image("imagine_cript_output.png", key, "imagine_decriptata_out.png")

    # key = generate_random_key()
    # print(f"Key = {key}")
    # # Input message from user
    # message = input("Enter a message to encrypt: ")
    #
    # # Encrypt the message
    # encrypted = encrypt_message(bytes(key), message)
    # print("Encrypted message:", encrypted.hex())
    #
    # # Decrypt the message
    # decrypted = decrypt_message(key, encrypted)
    # print("Decrypted message:", decrypted)

    # key = b'\xe3\x05\xc3&`b\xfe\x87\xcf\xfd\xd1/X\x13N\x1f'
    # print(f"tip = {type(key)}, cheie = {key}")
    # hex_key = key.hex()
    # print(f"tip = {type(hex_key)}, cheie = {hex_key}")
    # print(bytes.fromhex(hex_key))
    # enc = bytes.fromhex("d721757ee4a42fc40d74a5016e27eef87c91e1e9504c6971aa7e8977fade6087")
    #
    #
    # decr = decrypt_message(bytes.fromhex(hex_key), enc)
    # print(decr)

if __name__ == "__main__":
    main()
