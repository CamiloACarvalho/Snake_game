#Este projeto é uma forma que encontrei de estudar e treinar Python

import random #Estamos importando essa biblioteca para gerar a camida da cobrinha aleatoriamente pela tela
import curses #Essa biblioteca para poder mover a cobrinha, então serve como entrada para os comandos do teclado. Lembrando que, essa biblioteca não é padrão do Python

altura, largura = curses.initscr().getmaxyx() #Definindo a largura e altura da tela do jogo
janela = curses.newwin(altura, largura, 0,0) #Aqui criamos a tela da janela. o campo da batalha.

#Algumas configurações para o jogo

curses.curs_set(False) #Para não aparecer o cursos do mouse dentro da janela
janela.keypad(True) #Para utilizar o teclado para movimentar a cobrinha
janela.nodelay(True) #Para não ter delay na tela do jogo

#Iniciando o jogo

#Criando limites para cobrinha se movimentar
for pos in range (0, largura -1):

    janela.addch (0, pos,'#') # o '#' será o corpo da cobrinha. To pensando em mudar. Vamos ver como vai ser depois do jogo pronto
    janela.addch (altura -1, pos, '#')

for pos in range (0, altura -1):

    janela.addch (pos, 0, '#')
    janela.addch (pos, largura -1, '#')

#Criando a cobrinha

cobra = [[2,4],[2,3],[2,2]] # Sempre [Linha, Coluna]. Estamos utilizando essa estrutura bidimensional

#Adicionando a cobrinha no campo de jogo

for pos in range (0, len(cobra)):

    janela.addch (cobra[pos][0], cobra[pos][1], '#') #Declaramos cobra duas vezes porque como é posição bidimensional, no primeiro se refere a linha e o segundo a coluna

#Criando variável para controlar a cobra. E também para saber se ela tocará na maçã ou nas extremidades

posicao_cabeca = [2,4]
comida = [5,5] #Note que tanto a linha quanto a coluna estão no mesmo lugar, pois a comida representará apenas um pixel

#Adicionando a comida na tela

janela.addch(comida[0], comida[1], '*') # o '*' representará a maçã no jogo

#Declarando as variáveis

tecla = -1
tecla_nova = curses.KEY_RIGHT #Está dando o comando para a cobra começar o seu movimento para a direita
ultima_posicao = 'r' #Esse 'r' é de right, ou seja, direita
pontuacao = 0
velocidade_movimento = 50

#Começando o jogo

while True:

    tecla_nova = janela.getch() #Pesquisar essa função*****
    tecla = tecla if tecla_nova == -1 else tecla_nova #Aqui vamos dar um comando pra ela, ou seja apertar uma tecla. Se a gente apertar uma outra tecla, ela assume esse controle, se não mantém a direção

    #Aqui vamos estabelecer uma regra que é a seguinte. Se ela estiver indo pra direita e tu der o comando pra ir pra esquerda, não poderá mudar o mesmo vale se tiver indo pra cima e mandar ela ir para baixo.

    if tecla == curses.KEY_DOWN and ultima_posicao != 'u': ultima_posicao = 'd' #aqui diz o seguinte: Se ela estiver indo para baixo e vc der o comando para ela subir, ela vai continuar indo para baixo
    elif tecla == curses.KEY_UP and ultima_posicao != 'd': ultima_posicao = 'u' #aqui diz o seguinte: Se ela estiver indo para cima e vc der o comando para ela descer, ela vai continuar sbindo
    elif tecla == curses.kEY_LEFT and ultima_posicao != 'r': ultima_posicao = 'l' #aqui diz o seguinte: Se ela estiver indo para esquerda e vc der o comando para ela ir para direita, ela vai continuar indo para esquerda
    if tecla == curses.KEY_RIGHT and ultima_posicao != 'l': ultima_posicao = 'r' #aqui diz o seguinte: Se ela estiver indo para direita e vc der o comando para ela ir para esquerda, ela vai continuar indo para direita
    
    #Aqui vamos fazer a cobrinha se deslocar incrementando ou decrementando sua posição

    if ultima_posicao == 'r': posicao_cabeca[1] += 1
    elif ultima_posicao == 'l': posicao_cabeca[1] -= 1
    if ultima_posicao == 'u': posicao_cabeca[0] -= 1
    if ultima_posicao == 'd': posicao_cabeca[0] += 1

    #Agora vamos configurar o movimento para se a cabeça da cobra estiver na mesma direção da maçã

    if posicao_cabeca == comida:

        pontuacao += 1 #quer dizer que ela comeu a maçã, logo vai incrementar a pontuação
        comida = [random.randint(1, altura -2), random.randint(1, largura -2)] #Depois de ter comido a maçã, gerando outra maçã aleatoriamente.
        janela.addch(comida[0], comida[1], '*') #Coloando a maçã na tela de novo
        velocidade_movimento = velocidade_movimento -10 if velocidade_movimento -10 > 5 else velocidade_movimento #Aumentando a velocidade da cobrinha a medida que ela vai comendo uma maçã
    elif (posicao_cabeca [0] == altura -1 or posicao_cabeca [0] == 0) or (posicao_cabeca [1] == largura -1 or posicao_cabeca [1] == 0): break #Aqui é para parar o jogo, caso a cobra bata, encerra o loop

    #Se ela não bater, não comer a maçã, será o movimento da cobra. Então vamos elaborar esses movimentos

    else:

        #Para ela movimentar a cauda tem que andar, deslocar

        cauda = cobra.pop() #Pesquisar essas funções depois
        janela.addch(cauda[0],cauda[1], '') #Aqui estamos elaborando o movimento dela, ou seja, quando ela andar, a cauda vai sumir '' aspas vazia

    #Quando ela come, temos que aumentar o tamanho da cobrinha, logo

    cobra.insert(0, list(posicao_cabeca))
    janela.addch (posicao_cabeca[0], posicao_cabeca[1], '#') #Pronto, a cabeça está atualizada. Agora quando comer a maçã, a cobra vai ficar maior

    #Agora temos um novo problema, que é quando a cabeça bate na cauda

    if cobra[0] in cobra [1:]: break

    #Determinar a velocidade da cobra

    curses.napms(velocidade_movimento)
    janela.refresh() #Atualiza a tela, porque a cobra vai aumentar a velocidade

#Exibir a pontuação caso game-over

janela.addstr (int(altura/2), int(largura/2.5), "PONTUAÇÃO:  "+ str(pontuacao))
janela.refresh() #Atualiza a tela
curses.napms(2000)
curses.endwin() #Termina o jogo





