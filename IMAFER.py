import shutil, os, pyperclip
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)

def DupImg(iname):
    try:
        global NewImgName
        NewImgName = 'imafed - ' + iname
        shutil.copyfile(iname, str(NewImgName))  # Duplicating the image.
    except FileNotFoundError:  # Handling image not being found
        print("File Not Found....")
        main()


def TheMerge(fname):
    try:
        '''
            Begin encryption part
        '''
        SecMsg = open(fname, "rb").read()  # Opening the secret message
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(SecMsg)


        file_out = open(str(NewImgName), "a", errors="ignore")  # Opening the duplicated image for appending
        file_out.write('\n' + "-----BEGIN IMAFED DATA-----" + "\n" + 'DeMafed - ' + fname + '\n')
        file_out.close()
        file_out = open(str(NewImgName), "ab")
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
        file_out.close()
        file_out = open(str(NewImgName), "a", errors="ignore")
        # file_out.write('\n' + "-----END IMAFED DATA-----")
        print("Merged successfully")
        # pyperclip.copy(str(key))
        print("Password has been copied to your clipboard, store it in a safe place.")
        Show = input("In case you have problem accessing your keyboard, write 'save' then hit enter; this will save the password in file named 'pass.txt'\n>> ")
        if Show.lower() == "save":
            print("Your password (without the quotes) is '" + str(key) + "'", "Store it in a safe place since you won't have access to it again")
            awf = open('pass.txt', 'w')
            awf.write(str(key))
            awf.close()
        '''
                    End encryption part
        '''
    except FileNotFoundError:  # Handling secret file not being found
        print("File Not Found")
        main()



def main():
    Tk().withdraw()
    AllowedFiletypes = (("Image files", "*.jpg *.jpeg *.png"),)
    input("Hit enter to chose the image you want to encrypt the data in")
    DupImg(os.path.basename(askopenfilename(title="Select an image file", filetypes=AllowedFiletypes)))
    # DupImg(input("Please input the name of the image along with the extension ex. 'image.jpg' "))
    print("Imported image name is", DupImg, "\nPlease hit enter to proceed with the file you want to encrypt")
    input()
    TheMerge(os.path.basename(askopenfilename(title="Select the file you want to Encrypt")))
    # TheMerge(
    #     input("Please input the name of the file which has the secret messagealong with the extension ex. 'msg.txt' "))



try:
    main()
except Exception:
    print("Error")
    quit()

