import random

import numpy as np

BOARD_SIZE = 3

board = np.arange(1, BOARD_SIZE**2 + 1).astype(str)

victories = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]
)

moves = [num for num in range(1, (BOARD_SIZE**2) + 1)]
random.shuffle(moves)


def display_board(BOARD_SIZE: int, board: np.ndarray) -> None:
    """
    Display the current state of the game board.

    Args:
        BOARD_SIZE: The size of the game board (e.g., 3 for a 3x3 board).
        board: The current game board state.
    """
    print()
    for i, num in enumerate(board):
        print(num, end="  ")
        if (i + 1) % BOARD_SIZE == 0:
            print()
    print()


def apply_move(
    player: str,
    symbol: str,
    move: int,
    board: np.ndarray,
) -> None:
    """
    Update the game board with the player's move.

    Args:
        player: The current player's name.
        symbol: The player's symbol (e.g., "O" or "X").
        move: The position chosen by the player.
        board: The current game board state.
    """
    print(f"{player}({symbol})가 선택한 수 : {move}")
    board[(move - 1)] = symbol


def check_for_victory(board: np.ndarray, victories: np.ndarray) -> bool:
    """
    Determine if any win condition is satisfied.

    Args:
        board: The current game board state.
        victories: Possible win conditions.
    Return:
        True if a condition is satisfied, otherwise False.
    """
    for victory in victories:
        if np.all(board[victory - 1] == board[victory - 1][0]):
            return True
    return False


def play_game(
    BOARD_SIZE: int,
    moves: list[int],
    board: np.ndarray,
    victories: np.ndarray,
) -> None:
    """
    Run a Tic Tac Toe game.

    Args:
        BOARD_SIZE: The size of the game board (e.g., 3 for a 3x3 board).
        moves: Shuffled board positions.
        board: The current game board state.
        victories: Possible win conditions.
    """
    display_board(BOARD_SIZE, board)
    for idx, move in enumerate(moves):
        if idx % 2 == 0:
            player_name = "첫 번째 플레이어"
            symbol = "O"
            apply_move(player_name, symbol, move, board)
        else:
            player_name = "두 번째 플레이어"
            symbol = "X"
            apply_move(player_name, symbol, move, board)

        display_board(BOARD_SIZE, board)

        if check_for_victory(board, victories):
            print(f"{player_name} 승리!")
            break
    else:
        print("비겼습니다.")


if __name__ == "__main__":
    play_game(BOARD_SIZE, moves, board, victories)
