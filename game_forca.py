# -*- coding: utf-8 -*-

import random
dir(random)

#criando uma lista com as posições do boneco
forca = ['''

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
        if letra in self.palavra and letra not in self.certa:
            self.certa.append(letra)
        elif letra not in self.palavra and letra not in self.errada:
            self.errada.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def gameover(self):
       if self.vencedor() or (len(self.errada)==6):
           return True


    # Método para verificar se o jogador venceu
    def vencedor(self):
        if '_' not in self.encondeLetra():
            return True
        return False

    # Método para não mostrar a letra no board

    def encondeLetra(self):
        ident = " "
        for letra in self.palavra:
            if letra not in self.certa:
                ident = ident + "_"
            else:
                ident = ident + letra
            return ident


    # Método para checar o status do game e imprimir o board na tela
    def statusJogo(self):
        print(forca[len(self.errada)])
        print('\nPalavra: ', self.encondeLetra)
        print('\nLetras erradas: ', )
        for letra in self.errada:
            print(letra)
        print()
        print('Letras corretas: ', )
        for letra in self.certa:
            print(letra)
        print()


# Função para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto

    game = Boneco(palavra_aleatoria())

    while not game.gameover():
        game.statusJogo()
        letra_digitada = input("\nDigite uma letra")
        game.advinhaLetra(letra_digitada)

    game.statusJogo()


    if game.vencedor():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ', game.palavra)


# Executa o programa
if __name__ == "__main__":
    main()


