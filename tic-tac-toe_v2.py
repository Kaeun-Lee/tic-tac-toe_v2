import random

BOARD_SIZE = 3

board = [num for num in range(1, (BOARD_SIZE**2) + 1)]

victories = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]

moves = [num for num in range(1, (BOARD_SIZE**2) + 1)]
random.shuffle(moves)


def current_state() -> None:
    """Display the current state of the game board."""
    print()
    for i, num in enumerate(board):
        print(num, end="  ")
        if (i + 1) % BOARD_SIZE == 0:
            print()
    print()


def is_matched(victories: list[list[int]]) -> bool:
    """
    Check if any victory condition is satisfied.

    Args:
        victories: Possible winning conditions.
    Return:
        True if a condition is satisfied, otherwise False.
    """
    for victory in victories:
        if victory.count(0) == 3:
            return True
        elif victory.count(-1) == 3:
            return True
    else:
        return False


def game() -> None:
    """play a Tic Tac Toe game"""
    current_state()
    for idx, move in enumerate(moves):
        if idx % 2 == 0:
            print(f"첫 번째 플레이어(O)가 선택한 수 : {move}")

            board[move - 1] = "O"
            for victory in victories:
                if move in victory:
                    move_idx = victory.index(move)
                    victory[move_idx] = 0
            current_state()

            if is_matched(victories):
                print("첫 번째 플레이어 승리!")
                break
        else:
            print(f"두 번째 플레이어(X)가 선택한 수 : {move}")

            board[move - 1] = "X"
            for victory in victories:
                if move in victory:
                    move_idx = victory.index(move)
                    victory[move_idx] = -1
            current_state()

            if is_matched(victories):
                print("두 번째 플레이어 승리!")
                break
    else:
        print("비겼습니다.")


if __name__ == "__main__":
    game()
