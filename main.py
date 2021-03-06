from curses import wrapper
import curses
from util import Display, eprint
from time import sleep
from board import Board, Stone


def main(screen):
    # Create the display object. This is found in util.py
    x=3
    y=3
    display = Display(screen)
    message = ''
    board = Board(5, 5)
    turn = Stone.BLACK

    while True:
        # See util.py for where these methods are defined
        display.set_cursor((x,y))
        display.print_board(board.get_stone_at)
        display.display_message(message)
        display.refresh()

        board.is_alive(x-1,y-1)        

        input_char = display.get_input()

        if input_char == curses.KEY_RIGHT and x<5:
            x=x+1
        elif input_char == curses.KEY_DOWN and y<5:
            y=y+1
        elif input_char == curses.KEY_UP and y>1:
            y=y-1
        elif input_char == curses.KEY_LEFT and x > 1:
            x=x-1
        elif input_char == 32:
            turn = board.set_stone_at(x, y, turn)

        display.set_cursor((x,y))
        # These may help you figure out what is going on

        #
        ######################################################
    
if __name__ == "__main__":
    wrapper(main)
    
