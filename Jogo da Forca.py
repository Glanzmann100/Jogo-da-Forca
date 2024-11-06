import random

print("Bem Vindo ao Jogo da forca")

Palavras = ['python', 'programacao', 'algoritmo', 'desenvolvimento', 'tecnologia']
Palavra_Secreta = random.choice(Palavras)
Letras_Corretas = []
Tentativas = 5

while True:
    print(f"Você possui {Tentativas} tentativas")
    Tentativa = input("Digite uma letra: ")

    if Tentativas < 1:
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

    Lista_Palavra = ''
    for Letra in Palavra_Secreta:
        if Letra in Letras_Corretas:
            Lista_Palavra = Lista_Palavra + Letra
        else:
            Lista_Palavra += '*'
            
    if Lista_Palavra == Palavra_Secreta:
        print(f"Fim de jogo! A palavra era: {Palavra_Secreta}")
        break
    else:
        print(f"{Lista_Palavra}")