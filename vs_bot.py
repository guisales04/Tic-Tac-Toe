from os import system
from time import sleep as sp
from random import randint

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


def verify_velha(jogadas: list, jogadas_bot: list) -> str:
    player = verify_win(jogadas)
    bot = verify_win(jogadas_bot)
    match player, bot:
        case True, False:
            return 'player'
        case False, True:
            return 'bot'
    for pos in posicoes.values():
        if pos.isdigit():
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


def validation_bot(position) -> bool:
    if not posicoes[position].isdigit():
        return False
    return True


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


def get_positions() -> list:
    possibilities = []
    for pos in posicoes.values():
        possibilities.append(int(pos)) if pos.isdigit() else None
    return possibilities


def movimento_ai(bot: str, bot_plays: list, jogadas_player: list):
    positions = get_positions()

    for pos in positions:
        bot_plays.append(pos)
        bot_win = verify_win(bot_plays)
        if bot_win:
            del bot_plays[-1]
            posicoes[pos] = bot
            return pos
        del bot_plays[-1]

    for pos in positions:
        jogadas_player.append(pos)
        player_win = verify_win(jogadas_player)
        if player_win:
            del jogadas_player[-1]
            posicoes[pos] = bot
            return pos
        del jogadas_player[-1]
    bot_play = randint(1, 9)

    while not validation_bot(bot_play):
        bot_play = randint(1, 9)
    posicoes[bot_play] = bot
    return bot_play


def movimento(player: str):
    jogada = input(f"Selecione a posição para colocar o {player}: ")

    while not validation_position(jogada):
        print('\nSelecione uma posição válida!')
        jogada = input(f"Selecione a posição para colocar o {player}: ")
    movimento = int(jogada)
    posicoes[movimento] = player
    return movimento


def start():
    jogador_atual = 1
    jogadas = []
    jogadas_bot = []
    bot = ''
    player = input('Deseja jogar como X ou O: ').upper()

    while player not in ['X', 'O']:
        print('\n Selecione uma opção válida!')
        player = input('Deseja jogar como X ou O: ').upper()

    match player:
        case 'X':
            bot = 'O'
        case 'O':
            bot = 'X'

    while True:
        system("cls")
        print(sync_table())

        win = verify_velha(jogadas, jogadas_bot)
        match win:
            case 'velha':
                sp(2)
                return velha()
            case 'player':
                sp(2)
                return end_game('Jogador')
            case 'bot':
                sp(2)
                return end_game('Bot')

        if time_player(jogador_atual) == player:
            jogada = movimento(player)
            jogadas.append(jogada)
        else:
            print('Bot está jogando...')
            sp(2)
            bot_play = movimento_ai(bot, jogadas_bot, jogadas)
            jogadas_bot.append(bot_play)

        jogador_atual += 1


def velha():
    system('cls')
    print('Meer, deu velha, que paia!')


def end_game(winner: str):
    system('cls')
    match winner:
        case 'Jogador':
            print('Parabéns você venceu!')
        case 'Bot':
            print('Errr, você perdeu, HORRIVEL!')


start()
