import random

import numpy as np


def initialize_board() -> tuple[int, np.ndarray, dict[int, str]]:
    """
    Initialize the game board.

    Returns:
        board_size: The size of the game board (e.g., 3 for a 3x3 board).
        board: The initial game board state.
        symbol_mapping: Numeric-symbol pairs.
    """
    board_size = 3
    board = np.arange(1, board_size**2 + 1)
    symbol_mapping = {0: "O", -1: "X"}
    return board_size, board, symbol_mapping


def setup_victory_rules() -> list[list[int]]:
    """
    Define the win conditions for the game.

    Return:
        victory_rules: Possible win conditions.
    """
    victory_rules = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    return victory_rules


def setup_players() -> tuple[str, str]:
    """
    Sets up the players with a random order.

    Return:
        players: The player names in random order.
    """
    players = ("Computer", "Player")
    random.sample(players, 2)
    return players


def display_board(
    board_size: int, board: np.ndarray, symbol_mapping: dict[int, str]
) -> None:
    """
    Display the current state of the game board.

    Args:
        board_size: The size of the game board (e.g., 3 for a 3x3 board).
        board: The current game board state.
        symbol_mapping: Numeric-symbol pairs.
    """

    print()
    for i, num in enumerate(board):
        if board[i] == 0:
            print(symbol_mapping[0], end="  ")
        elif board[i] == -1:
            print(symbol_mapping[-1], end="  ")
        else:
            print(num, end="  ")
        if (i + 1) % board_size == 0:
            print()
    print()


def display_scoreboard(scoreboard: dict[str, int]) -> None:
    """
    Display the current game scoreboard.

    Arg:
        scoreboard: The current scores.
    """
    print(f"    현재 스코어    ")
    print(
        f"< Player >  {scoreboard['Player']} : {scoreboard['Computer']}  < Computer >\n"
    )


def get_player_move(available_moves: list[int]) -> int:
    """
    Prompt the player to input a valid move.

    Arg:
        available_moves: Positions available for selection.

    Return:
        move: The position chosen by the human player.
    """
    while True:
        try:
            move = int(input("수를 입력하세요. : "))
        except ValueError as e:
            print(f"정수를 입력하세요.")
        else:
            if move < 1 or move > 9:
                print("1 ~ 9 사이의 수를 입력하세요.")
            if move in available_moves:
                return move
            else:
                print("이미 놓인 수입니다. 다시 선택해 주세요.")


def choose_random_move(available_moves: list[int]) -> int:
    """
    Select a random move from the available moves.

    Arg:
        available_moves: Positions available for selection.

    Return:
        move: The position randomly chosen by the computer.
    """
    move = random.choice(available_moves)
    return move


def check_for_victory(board: np.ndarray, victory_rules: list[list[int]]) -> bool:
    """
    Determine if any win condition is satisfied.

    Args:
        board: The current game board state.
        victory_rules: Possible win conditions.

    Return:
        True if a condition is satisfied, otherwise False.
    """
    for victory in victory_rules:
        if np.all(board[victory] == board[victory][0]):
            return True
    return False


def prompt_restart() -> bool:
    """
    Prompt the user to restart game.

    Return:
        bool: True for restart, otherwise False.
    """

    while True:
        restart = (
            input("게임을 다시 시작하려면 'y', 종료하려면 'n'을 입력하세요. : ")
            .strip()
            .lower()
        )
        if restart in ["y", "n"]:
            return restart == "y"
        else:
            print("잘못 입력하셨습니다. 다시 입력해 주세요.")


def play_one_round(
    board_size: int,
    board: np.ndarray,
    symbol_mapping: dict[int, str],
    victory_rules: list[list[int]],
    available_moves: list[int],
    first_player: str,
    second_player: str,
    scoreboard: dict[str, int],
) -> None:
    """
    Play a single round of the Tic Tac Toe game.

    Args:
        board_size: The size of the game board (e.g., 3 for a 3x3 board).
        board: The current game board state.
        symbol_mapping: Numeric-symbol pairs.
        victory_rules: Possible win conditions.
        available_moves: Positions available for selection.
        first_player: The player who moves first.
        second_player: The player who moves second.
        scoreboard: The current scores.
    """
    display_board(board_size, board, symbol_mapping)

    while available_moves:
        if len(available_moves) % 2:
            player_name = first_player
            symbol_value = 0
        else:
            player_name = second_player
            symbol_value = -1

        if player_name == "Computer":
            move = choose_random_move(available_moves)
        else:
            move = get_player_move(available_moves)

        print(f"{player_name}({symbol_mapping[symbol_value]})가 선택한 수 : {move}")

        available_moves.remove(move)
        board[(move - 1)] = symbol_value

        display_board(board_size, board, symbol_mapping)

        if check_for_victory(board, victory_rules):
            scoreboard[player_name] += 1
            print(f"{player_name} 승리!")
            break
    else:
        print("비겼습니다.")


def main() -> None:
    """Execute the Tic Tac Toe game."""
    victory_rules = setup_victory_rules()
    first_player, second_player = setup_players()
    scoreboard = {"Player": 0, "Computer": 0}
    round = 1

    while True:
        board_size, board, symbol_mapping = initialize_board()
        available_moves = list(board)

        print(f"Round {round}\n")
        display_scoreboard(scoreboard)
        print(f"{first_player}가 선입니다.")

        play_one_round(
            board_size,
            board,
            symbol_mapping,
            victory_rules,
            available_moves,
            first_player,
            second_player,
            scoreboard,
        )

        if prompt_restart():
            round += 1
            first_player, second_player = second_player, first_player
            print("게임을 재시작합니다.\n")
        else:
            print("게임을 종료합니다.")
            break


if __name__ == "__main__":
    main()
