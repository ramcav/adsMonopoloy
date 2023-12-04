import pytest
from board import Board

def test_board_initialization():
    board_size = 4
    board = Board(board_size)
    assert board.board_size == board_size
    assert len(board.tiles_list) == board_size**2

def test_str_format():
    board = Board()
    formatted_str = board.str_format("Test", 2, "Ricardo")
    assert "Test" in formatted_str
    assert "(RR)" in formatted_str
    

    


if __name__ == '__main__':
    pytest.main(['-v', __file__])