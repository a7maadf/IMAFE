import random, os, string, time
from Cryptodome.Cipher import AES
from tkinter import Tk
from tkinter.filedialog import askopenfilename
def DeMafer():
    Tk().withdraw()
    AllowedFiletypes = (("Image files", "*.jpg *.jpeg *.png"),)
    # fname = input("Please enter the file name (include the extension)")
    fname = os.path.basename(askopenfilename(title="Select an image file", filetypes=AllowedFiletypes))
    try:
        IMAFED_f = open(str(fname), "rb")
    except FileNotFoundError:
        print("File not found")
    lines = IMAFED_f.readlines()
    for line in lines:
        if line.find(b'-----BEGIN IMAFED DATA-----') != -1:
            DeMafed_N = lines[lines.index(line) + 1]
            sLine = lines.index(line) + 2
            letters = string.ascii_lowercase
            tempFName = ''.join(random.choice(letters) for i in range(5)) + 'rnd.txt'
            file_in = open(tempFName, 'ab')
            for item in lines[sLine:]:
                if b'\r\n-----END IMAFED DATA-----' not in item:
                    file_in.write(item)
            file_in.close()

    # Decryption
    file_in = open(tempFName, "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    while True:
        try:
            passKey = eval(input("Please input the passkey: "))
            cipher = AES.new(passKey, AES.MODE_EAX, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            print("File decrypted successfully")
            break
        except Exception:
            print("Error, probably wrong password")
            time.sleep(0.5)
    file_in.close()
    os.remove(tempFName)
    open((DeMafed_N).decode().rstrip(), "wb").write(data)

DeMafer()
