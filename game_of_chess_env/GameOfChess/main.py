from chessman import chessman
from constants import constants

if __name__ == "__main__":
    rook = chessman(constants.ROOK, constants.BLACK, "A", "1")
    print(rook.state)
    