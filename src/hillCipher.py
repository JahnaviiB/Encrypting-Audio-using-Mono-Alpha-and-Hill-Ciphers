# Below libraries are imported
from sympy.crypto.crypto import encipher_hill, decipher_hill
from sympy import Matrix
# defining a function for hill cipher
def hill():
    with open("./src/example.wav", "rb") as f:
        x = f.read().hex()

    key = Matrix([[1, 1, 1, 2], [0, 1, 1, 0],
                  [2, 2, 3, 4], [1, 1, 0, 1]])

    # This is the process for Encryption
    print("Process for Encryption has started")
    cipher_text = ""
    for i in x:
        if i.isalpha():
            cipher_text+=encipher_hill(i,key)
        else:
            cipher_text+=i
    print("Encryption has been completed")
    with open("enc_hill.wav.crypt", "w") as f:
        f.write(cipher_text)

    print("Completed file encryption ")
    print("Process for Decryption has started")
    # This is the process for Decryption
    point_1 = ""
    for i in cipher_text:
        if i.isalpha():
            point_1+=decipher_hill(i,key)
        else:
            point_1+=i

    with open("dec_hill.wav", "wb") as f:
        f.write(bytes().fromhex(point_1))
    print("Decryption has been completed")
    
hill()