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


def randomize_moves(board: np.ndarray) -> np.ndarray:
    """
    Generate a randomized sequence of moves.

    Arg:
        board: The current game board state.

    Return:
        moves: Shuffled board positions.
    """
    moves = np.random.permutation(board)
    return moves


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


def apply_move(
    player: str,
    symbol_mapping: dict[int, str],
    symbol_value: int,
    move: int,
    board: np.ndarray,
) -> None:
    """
    Apply the player's move to the game board.

    Args:
        player: The current player's name.
        symbol_mapping: Numeric-symbol pairs.
        symbol_value: Numeric value of the player's symbol.
        move: The position chosen by the player.
        board: The current game board state.
    """
    print(f"{player}({symbol_mapping[symbol_value]})가 선택한 수 : {move}")
    board[(move - 1)] = symbol_value


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
    moves: np.ndarray,
    victory_rules: list[list[int]],
) -> None:
    """
    Play a single round of the Tic Tac Toe game.

    Args:
        board_size: The size of the game board (e.g., 3 for a 3x3 board).
        board: The current game board state.
        symbol_mapping: Numeric-symbol pairs.
        moves: Shuffled board positions.
        victory_rules: Possible win conditions.
    """
    display_board(board_size, board, symbol_mapping)

    for idx, move in enumerate(moves):
        if idx % 2 == 0:
            player_name = "첫 번째 플레이어"
            symbol_value = 0
        else:
            player_name = "두 번째 플레이어"
            symbol_value = -1

        apply_move(player_name, symbol_mapping, symbol_value, move, board)
        display_board(board_size, board, symbol_mapping)

        if check_for_victory(board, victory_rules):
            print(f"{player_name} 승리!")
            break
    else:
        print("비겼습니다.")


def main() -> None:
    """Execute the Tic Tac Toe game."""
    victory_rules = setup_victory_rules()

    while True:
        board_size, board, symbol_mapping = initialize_board()
        moves = randomize_moves(board)

        play_one_round(board_size, board, symbol_mapping, moves, victory_rules)

        if prompt_restart():
            print("게임을 재시작합니다.")
        else:
            print("게임을 종료합니다.")
            break


if __name__ == "__main__":
    main()
