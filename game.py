from graphics import *


def board_create():
    game_board = GraphWin('Game Board', 300, 300) # creates a board
    game_board.setCoords(0, 0, 150, 150)

    # making the grid
    left_line = Line(Point(50, 125), Point(50, 35))
    left_line.setWidth(2)
    left_line.draw(game_board)

    center_line = Line(Point(80, 125), Point(80, 35))
    center_line.setWidth(2)
    center_line.draw(game_board)

    right_line = Line(Point(110, 125), Point(110, 35))
    right_line.setWidth(2)
    right_line.draw(game_board)

    bottom_line = Line(Point(140, 65), Point(20, 65))
    bottom_line.setWidth(2)
    bottom_line.draw(game_board)

    top_line = Line(Point(140, 95), Point(20, 95))
    top_line.setWidth(2)
    top_line.draw(game_board)

    message = Text(Point(game_board.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(game_board)
    
    game_board.getMouse()
    game_board.close()


def noughts_crosses():
    board_dic = {
        'top_l':'',
        'top_m':'',
        'top_r':'',
        'mid_l':'',
        'mid_m':'',
        'mid_r':'',
        'bottom_l':'',
        'bottom_m':'',
        'bottom_r':''
    }

    options = [1,2,3,4,5,6,7,8,9]


