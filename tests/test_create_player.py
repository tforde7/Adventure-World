
import pytest
from create_player import PlayerCreator
from create_player import CharacterLengthExceeded

@pytest.fixture
def mock_input(monkeypatch):
    # Mock input function to simulate user input
    user_inputs = []

    def mock_input_func(_):
        if user_inputs:
            return user_inputs.pop(0)
        return ""

    monkeypatch.setattr('builtins.input', mock_input_func)

    return user_inputs

"""
input_name()
---
Equivalence Classes
---
EC1: name length is less than 20 charcters - valid input
EC2: name length is greter than 20 charcters - invalid input

Boundary Values
---
length = 19
length = 20
length = 21

"""

def test_input_name_valid(mock_input):
    mock_input.append("John")
    player_creator = PlayerCreator()
    assert player_creator.input_name() == "John"

    
def test_input_name_invalid(mock_input):
    mock_input.append("X" * 25)
    player_creator = PlayerCreator()
    with pytest.raises(CharacterLengthExceeded) as exception:
        player_creator.input_name()
    
    assert str(exception.value) == "Maximun 20 characters"


def test_input_name_boundary(mock_input):
    player_creator = PlayerCreator()

    # Test input name length of 19 characters
    mock_input.append("A" * 19)
    assert player_creator.input_name() == "A" * 19

    # Test input name length of 20 characters
    mock_input.append("B" * 20)
    assert player_creator.input_name() == "B" * 20

    # Test input name length of 21 characters
    mock_input.append("C" * 21)
    with pytest.raises(CharacterLengthExceeded) as exception:
        player_creator.input_name()

    assert str(exception.value) == "Maximun 20 characters"

    



