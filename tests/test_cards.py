import pytest
from entity import Card, CardStack
from entity import Player
from unittest.mock import patch, MagicMock
from board import StreetTile


def test_card_invoke_lottery():
    player = Player("TestPlayer", 0)
    card = Card(0)  
    
    with patch('builtins.print') as mock_print:
        card.invoke(player)
        assert player.money == 1100
        mock_print.assert_called_with("You've won the lottery! $100 have been added to your account!")

def test_card_invoke_penalty():
    player = Player("TestPlayer", 200)
    card = Card(1)  # Penalty card
    with patch('builtins.print') as mock_print:
        card.invoke(player)
        assert player.money == 900
        mock_print.assert_called_with("Oops! You forgot to pay your mortgage in time! 100 dollars have been subtracted from your account.")

def test_card_invoke_inheritance():
    player = Player("TestPlayer", 0)
    tile = StreetTile("Washington")
    tile.houses = 2
    player.houses = {tile: 2} 
    card = Card(2) 
    card.invoke(player)
    assert player.houses[tile] == 3
    
def test_card_stack_take():
    player = Player("TestPlayer", 0)
    card_stack = CardStack(5)
    
    with patch('random.randint', return_value=0):
        card_stack.take(player)
        assert len(card_stack.stack) == 4
    
def test_card_stack_take_money():
    player = Player("TestPlayer", 0)
    tile = StreetTile("Washington")
    tile.houses = 2
    player.houses = {tile: 3} 
    card = Card(2) 
    card.invoke(player)
    assert player.money == 1050

def test_empty_card_stack():
    player = Player("TestPlayer", 0)
    card_stack = CardStack(0)
    card_stack.removed = [Card(0), Card(1), Card(2)]

    # The stack should be empty
    # and the removed should have 3 cards
    assert len(card_stack.stack) == 0
    assert len(card_stack.removed) == 3

    with patch('random.randint', return_value=0):
        card_stack.take(player)

    # Cards should have been removed from removed and added to stack
    # and removed should now have one card
    assert len(card_stack.stack) == 2
    assert len(card_stack.removed) == 1
    
    # Player should have won 100$
    assert player.money == 1100


if __name__ == "__main__":
    pytest.main(["-v", __file__])