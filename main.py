# -*- coding: utf-8 -*-

import random
dir(random)

#criando uma lista com as posições do boneco
boneco = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Boneco:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra=palavra
        self.errada = []
        self.certa = []
        print("Bora jogar!")

    # Método para adivinhar a letra
    def advinhaLetra(self, letra):
        letra = input.print("Digite uma letra: ")
            if letra in self.palavra and letra not in self.certa:
                self.certa.append(letra)
                print("Tem essa letra: %s", letra)
            else:
                print("Não tem essa letra. Perdeu ponto! ")


    # Método para verificar se o jogo terminou
    def gameover(self):
        if boneco[7]:
            ("Fim de jogo")

    # Método para verificar se o jogador venceu
    def venceu(self):
        if boneco[0-6]:
            print("Voce ganhou!")

    # Método para não mostrar a letra no board
    def encondeLetra(self):
        for l in palavra_aleatoria():


    # Método para checar o status do game e imprimir o board na tela
    def statusJogo(self):


# Função para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Boneco(advinhaLetra())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    # Verifica o status do jogo

        # Objeto
        game = Hangman(rand_word())

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()


