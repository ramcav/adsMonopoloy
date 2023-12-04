import pytest
from board import Go, Prison, Train, StreetTile
from entity import Player
from unittest.mock import patch


def test_go_tile():
    player = Player("TestPlayer", 0)
    go_tile = Go()
    go_tile.when_walked(player, 4)

def test_prison_tile():
    player = Player("TestPlayer", 0) 
    prison_tile = Prison()
    prison_tile.when_walked(player, 4)
    assert player.pos == 9

def test_train_tile():
    player = Player("TestPlayer", 0)
    train_tile = Train()
    train_tile.when_walked(player, 4)
    assert player.pos == 3

def test_handle_tile_purchase_performed():
    player = Player("TestPlayer", 0)
    street_tile = StreetTile("Washington")

    with patch('builtins.input', return_value='y'):
        street_tile.handle_tile_purchase(player)
        assert street_tile.owner == player
        assert player.money == 1000 - 100

def test_handle_tile_purchase_not_performed():
    player = Player("TestPlayer", 0) 
    street_tile = StreetTile("Washington")
    
    with patch('builtins.input', return_value='n'):
        street_tile.handle_tile_purchase(player)
        assert street_tile.owner != player
        assert player.money == 1000


if __name__ == "__main__":
    pytest.main(["-v", __file__])