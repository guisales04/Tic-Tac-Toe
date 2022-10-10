from os import system

posicoes = {x: str(x) for x in range(1, 10)}

vitoria = [
    [1, 2, 3],
    [1, 4, 7],
    [4, 5, 6],
    [7, 8, 9],
    [3, 6, 9],
    [2, 5, 8],
    [1, 5, 9],
    [7, 5, 3]
]


def verify_win(jogadas: list) -> bool:
    for list in vitoria:
        sets = set(list) & set(jogadas)
        if len(sets) == 3:
            return True
    return False


def verify_velha(jogadas_x: list, jogadas_o: list) -> str:
    x = verify_win(jogadas_x)
    o = verify_win(jogadas_o)
    match x, o:
        case True, False:
            return 'xwin'
        case False, True:
            return 'owin'
        case False, False:
            for pos in posicoes:
                pos_str = str(posicoes[pos])
                if pos_str.isdigit():
                    return 'None'
    return 'velha'


def time_player(jogador: int) -> str:
    return 'O' if jogador % 2 == 0 else 'X'


def validation_position(position) -> bool:
    if position.isdigit():
        if int(position) in posicoes.keys():
            if posicoes[int(position)].isdigit():
                return True
    return False


def sync_table() -> str:
    velha = '''1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
'''
    for pkey, pvalue in posicoes.items():
        velha = velha.replace(str(pkey), pvalue)
    return velha


def movimento(player: str) -> int:
    jogada = input(f"Selecione a posição para colocar o {player}: ")

    while not validation_position(jogada):
        print('\nSelecione uma posição válida!')
        jogada = input(f"Selecione a posição para colocar o {player}: ")
    movimento = int(jogada)
    posicoes[movimento] = player
    return movimento


def start():
    jogador_atual = 1
    jogadas_x = []
    jogadas_o = []

    while True:
        system("cls")
        print(sync_table())

        win = verify_velha(jogadas_x, jogadas_o)
        match win:
            case 'velha':
                return velha()
            case 'xwin':
                return end_game('X')
            case 'owin':
                return end_game('O')

        player = time_player(jogador_atual)
        jogada = movimento(player)

        match player:
            case 'X':
                jogadas_x.append(jogada)
            case 'O':
                jogadas_o.append(jogada)

        jogador_atual += 1


def velha():
    system('cls')
    print('Meer, deu velha, que paia!')


def end_game(winner: str):
    system('cls')
    print(f'Parabéns, o vencedor foi o representante de {winner}')


start()
