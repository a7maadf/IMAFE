def DeMafer(fname):
    IMAFED_f = open(str(fname), "r", encoding='utf-8', errors="ignore")
    lines = IMAFED_f.readlines()
    for line in lines:
        if line.find('-----BEGIN IMAFED DATA-----') != -1:
            DeMafed_N = lines[lines.index(line) + 1]
            DeMafed = open(str(DeMafed_N).rstrip(), "w", encoding='utf-8', errors="ignore")
            sLine = lines.index(line) + 2
            for item in lines[sLine:]:
                if item != "-----END IMAFED DATA-----":
                    DeMafed.write(item)
            quit()

DeMafer('imafed - image.jpg')
