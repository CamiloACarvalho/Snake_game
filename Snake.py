#Este projeto é uma forma que encontrei de estudar e treinar Python

import random #Estamos importando essa biblioteca para gerar a camida da cobrinha aleatoriamente pela tela
import curses #Essa biblioteca para poder mover a cobrinha, então serve como entrada para os comandos do teclado. Lembrando que, essa biblioteca não é padrão do Python

altura, largura = curses.initscr().getmaxyx() #Definindo a largura e altura da tela do jogo
janela = curses.newmain(altura, largura, 0,0) #Aqui criamos a tela da janela. o campo da batalha.