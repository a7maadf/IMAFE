import shutil

def DupImg(iname):
    try:
        global NewImgName
        NewImgName = 'imafed - ' + iname
        shutil.copyfile(iname, str(NewImgName)) # Duplicating the image.
    except FileNotFoundError: # Handling image not being found
        print("File Not Found....")
        main()

def TheMerge(fname):
    try:
        SecMsg = open(str(fname), "r", encoding='utf-8', errors="ignore") # Opening the secret message
        f = open(str(NewImgName), "a", errors="ignore") # Opening the duplicated image for appending 
        f.write('\n' + SecMsg.read())
    except FileNotFoundError: # Handling secret file not being found
        print("File Not Found")
        main()



def main():
    DupImg(input("Please input the name of the image along with the extension ex. 'image.jpg' "))
    TheMerge(input("Please input the name of the file which has the secret messagealong with the extension ex. 'msg.txt' "))
    
try:
    main()
except Exception:
    print("Error")
    quit()

