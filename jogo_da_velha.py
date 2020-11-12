tabuleiro = [' '] * 10


def imprimir_tabuleiro():
    print(f'   {tabuleiro[7]}   |', f'   {tabuleiro[8]}   |    {tabuleiro[9]}    ')
    print('_' * 6, '|', '_' * 6, '|', '_' * 6)
    print(f'   {tabuleiro[4]}   |', f'   {tabuleiro[5]}   |    {tabuleiro[6]}    ')
    print('_' * 6, '|', '_' * 6, '|', '_' * 6)
    print(f'   {tabuleiro[1]}   |', f'   {tabuleiro[2]}   |    {tabuleiro[3]}    ')
    print('       |', '       |     ')


def receber_dados(jogador):
    posicao = int(input('Digite a posição '))
    if tabuleiro[posicao] == ' ':
        if posicao == 0:
            return False
        tabuleiro[posicao] = jogador
        return True
    else:
        print('Campo Preenchido')
        return False


def verificar_tabuleiro():
    vazios = 0
    for a in range(0, 10):
        if tabuleiro[a] == ' ':
            vazios += 1
    if vazios == 1:
        print('-' * 25)
        print('EMPATE')
        print('-' * 25)
        return False
    else:
        return True


def verificar_vencedor(j):
    return ((tabuleiro[7] == j and tabuleiro[8] == j and tabuleiro[9] == j) or
            (tabuleiro[4] == j and tabuleiro[5] == j and tabuleiro[6] == j) or
            (tabuleiro[1] == j and tabuleiro[2] == j and tabuleiro[3] == j) or
            (tabuleiro[7] == j and tabuleiro[4] == j and tabuleiro[1] == j) or
            (tabuleiro[8] == j and tabuleiro[5] == j and tabuleiro[2] == j) or
            (tabuleiro[9] == j and tabuleiro[6] == j and tabuleiro[3] == j) or
            (tabuleiro[7] == j and tabuleiro[5] == j and tabuleiro[3] == j) or
            (tabuleiro[9] == j and tabuleiro[5] == j and tabuleiro[1] == j))


def jogar_novamente():
    jn = input('Deseja Jogar Novamente? [S/N]').strip().upper()[0]
    while jn not in 'SN':
        jn = input('Digite somente S para Sim e N para Não. Deseja Jogar Novamente? [S/N]').strip().upper()[0]
        if jn == 'N':
            return False
        return True

def jogo():
    imprimir_tabuleiro()
    Jon = True
    Jogador = 'Jogador 1'
    while Jon:
        if Jogador == 'Jogador 1':
            j = 'X'
        else:
            j = 'O'
        print('_'*25)
        print(Jogador)
        inputados = receber_dados(j)
        print('_' * 25)
        print()
        tab = verificar_tabuleiro()
        imprimir_tabuleiro()
        win = verificar_vencedor(j)
        if win:
            print('-'*25)
            print(f'{Jogador} Venceu!'.center(25))
            print('-' * 25)
            Jon = False
        if not tab:
            Jon = False
        if inputados:
            if Jogador == 'Jogador 1':
                Jogador = 'Jogador 2'
            else:
                Jogador = 'Jogador 1'
    jogar_mais = jogar_novamente()
    if jogar_mais:
        global tabuleiro
        tabuleiro = [' '] * 10
        jogo()


jogo()