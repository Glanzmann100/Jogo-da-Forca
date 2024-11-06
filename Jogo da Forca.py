import random

print("Bem Vindo ao Jogo da forca")

#Indica quais palavras podem ser selecionadas, o número de tentativas e o vetor das letras
arq = open("palavras.txt")
linhas = arq.readlines()
arq.close()
Palavra_Secreta = random.choice(linhas)
Letras_Corretas = []
Tentativas = 5

#Impõe o loop que será executado
while True:
    print(f"Você possui {Tentativas} tentativas")
    Tentativa = input("Digite uma letra: ")

#Estabelece as opções de respostas
    if Tentativas <= 0:
        print("Você perdeu")
        break

    elif Tentativa in Letras_Corretas:
        print("Você já escolheu essa letra ")
    elif Tentativa in Palavra_Secreta:
        Letras_Corretas.append(Tentativa)
        print("Parabéns você acertou uma letra ")
    else:
        Tentativas -= 1
        print("Infelizmente você errou ")

#Define a lista de letras que serão preenchidas
    Lista_Palavra = ''
    for Letra in Palavra_Secreta:
        if Letra in Letras_Corretas:
            Lista_Palavra = Lista_Palavra + Letra
        else:
            Lista_Palavra += '*'

#Finaliza o jogo           
    if Lista_Palavra == Palavra_Secreta:
        print(f"Fim de jogo! A palavra era: {Palavra_Secreta}")
        break
    else:
        print(f"{Lista_Palavra}")
        print("_"*20)