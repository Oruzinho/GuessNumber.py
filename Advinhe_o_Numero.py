import random

def jogar():
    print("*" * 45)
    print("*" + " " * 43 + "*")
    print("*     Bem-vindo ao Jogo de Advinhação!      *")
    print("*   Tente advinhar qual o número secreto!   *")
    print("* O Número Secreto é um valor entre 1 e 100 *")
    print("*                Boa Sorte!                 *")
    print("*" + " " * 43 + "*")
    print("*" * 45, end="\n\n\n")

    print("Em qual nível de dificuldade você quer jogar?")
    print("Isto vai determinar o seu número de tentativas", end=("\n\n"))
    print("(1) Fácil", "(2) Médio", "(3) Difícil", sep=("\n"), end=("\n\n"))

    tentativas = 0
    while(tentativas == 0):
        dificuldade = int(input("Escolha a dificuldade: "))

        if dificuldade == 1:
            print("Você escolheu a dificuldade FÁCIL", end="\n\n")
            tentativas = 15
        elif dificuldade == 2:
            print("Você escolheu a dificuldade MÉDIO", end="\n\n")
            tentativas = 10
        elif dificuldade == 3:
            print("Você escolheu a dificuldade DIFÍCIL", end="\n\n")
            tentativas = 5
        else:
            print("Valor inválido!", end="\n\n")
            continue

    numero_secreto = random.randrange(1, 101)

    while tentativas > 0:
        print("Você têm {} tentativas!".format(tentativas))
        chute = int(input("Digite o seu número: "))

        if chute < 1 or chute > 100:
            print("Você deve digitar um valor entre 1 e 100!", end="\n\n")
            continue

        acertou = numero_secreto == chute
        chute_maior = chute > numero_secreto

        if acertou:
            print("VOCÊ ACERTOU!", end="\n\n")
            break
        else:
            print("Esse não era o número correto!", end="\n\n")
            if chute_maior:
                print("O Número Secreto é MENOR que o seu chute", end="\n\n")
            else:
                print("O Número Secreto é MAIOR que o seu chute", end="\n\n")

        tentativas -= 1

    print("Fim do Jogo!")

if __name__ == "__main__":
    jogar()
