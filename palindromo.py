

def palindromo(frase):
    lista=[]
    frase = frase.split(" ")
    for palavra in (frase):
        remove = ["(", ")",",",".","!",'"',"'"]
        for especial in remove:
            palavra = palavra.replace(especial, "")
        palavrainvert = palavra[::-1]
        if (palavra == palavrainvert and len(palavra)>1):
            lista.append(palavra)
    return (lista)


while (True):
    try:
        frase = input("Digite a frase a ser testada: ")
        if frase == "":
            raise
        break
    except:
        print("Digite uma frase corretamente")
print (palindromo(frase))
