import re

def criar_hashtag(frase):

    frase_apenas = re.sub(r"[^\w\s]", "", frase)

    palavras = frase_apenas.split()

    palavras_filtrada = [palavra for palavra in palavras if palavra.lower() != "não"]

    hashtag = "".join(palavra.capitalize() for palavra in palavras_filtrada)

    return f"#{hashtag}"


user = input("Digite uma frase qualquer: ")

print(f"hashtag gerada -> {criar_hashtag(user)}")