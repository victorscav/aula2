def forca():

    palavra_secreta = "senac"
    letras_certas = ''
    tentativas = 0

    while True:
        letra_digitada = input("Digite uma letra: ")

        palavra_formada = ''
        if letra_digitada in palavra_secreta:
            letras_certas += letra_digitada
            

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_certas:
                palavra_formada += letra_secreta

            else:
                palavra_formada += '*'

        print(f"Palavra formada: {palavra_formada}")

        if palavra_formada == palavra_secreta:
            print("Fim de jogo")

forca()
