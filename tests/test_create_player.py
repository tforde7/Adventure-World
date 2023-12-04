
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
EC1: name length is less than or equal to 20 characters - valid input
EC2: name length is greter than 20 characters - invalid input

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
    
    assert str(exception.value) == "Maximum 20 characters"


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

    assert str(exception.value) == "Maximum 20 characters"


"""
input_gender()
---
Equivalence Classes
---
EC1: gender length is less than or equal to 10 characters - valid input
EC2: gender length is greter than 10 characters - invalid input

Boundary Values
---
length = 9
length = 10
length = 11

"""

def test_input_gender_valid(mock_input):
    mock_input.append("male")
    player_creator = PlayerCreator()
    assert player_creator.input_gender() == "male"

    
def test_input_gender_invalid(mock_input):
    mock_input.append("X" * 15)
    player_creator = PlayerCreator()
    with pytest.raises(CharacterLengthExceeded) as exception:
        player_creator.input_gender()
    
    assert str(exception.value) == "Maximum 10 characters"


def test_input_name_boundary(mock_input):
    player_creator = PlayerCreator()

    # Test input gender length of 9 characters
    mock_input.append("A" * 9)
    assert player_creator.input_gender() == "A" * 9

    # Test input gender length of 10 characters
    mock_input.append("B" * 10)
    assert player_creator.input_gender() == "B" * 10

    # Test input gender length of 11 characters
    mock_input.append("C" * 11)
    with pytest.raises(CharacterLengthExceeded) as exception:
        player_creator.input_gender()

    assert str(exception.value) == "Maximum 10 characters"

"""
input_race()
---
Equivalence Classes
---
EC1: race length is less than or equal to 12 characters - valid input
EC2: race length is greter than 12 characters - invalid input

Boundary Values
---
length = 11
length = 12
length = 13

"""

def test_input_race_valid(mock_input):
    mock_input.append("Elf")
    player_creator = PlayerCreator()
    assert player_creator.input_race() == "Elf"

    
def test_input_race_invalid(mock_input):
    mock_input.append("X" * 15)
    player_creator = PlayerCreator()
    with pytest.raises(CharacterLengthExceeded) as exception:
        player_creator.input_race()
    
    assert str(exception.value) == "Maximum 12 characters"


def test_input_race_boundary(mock_input):
    player_creator = PlayerCreator()

    # Test input race length of 11 characters
    mock_input.append("A" * 11)
    assert player_creator.input_race() == "A" * 11

    # Test input race length of 12 characters
    mock_input.append("B" * 12)
    assert player_creator.input_race() == "B" * 12

    # Test input race length of 13 characters
    mock_input.append("C" * 13)
    with pytest.raises(CharacterLengthExceeded) as exception:
        player_creator.input_race()

    assert str(exception.value) == "Maximum 12 characters"

"""
input_weapon()
---
Equivalence Classes
---
EC1: weapon length is less than or equal to 15 characters - valid input
EC2: weapon length is greter than 15 characters - invalid input

Boundary Values
---
length = 14
length = 15
length = 16

"""

def test_input_weapon_valid(mock_input):
    mock_input.append("Sword")
    player_creator = PlayerCreator()
    assert player_creator.input_weapon() == "Sword"

    
def test_input_weapon_invalid(mock_input):
    mock_input.append("X" * 18)
    player_creator = PlayerCreator()
    with pytest.raises(CharacterLengthExceeded) as exception:
        player_creator.input_weapon()
    
    assert str(exception.value) == "Maximum 15 characters"


def test_input_weapon_boundary(mock_input):
    player_creator = PlayerCreator()

    # Test input weapon length of 14 characters
    mock_input.append("A" * 14)
    assert player_creator.input_weapon() == "A" * 14

    # Test input weapon length of 15 characters
    mock_input.append("B" * 15)
    assert player_creator.input_weapon() == "B" * 15

    # Test input weapon length of 16 characters
    mock_input.append("C" * 16)
    with pytest.raises(CharacterLengthExceeded) as exception:
        player_creator.input_weapon()

    assert str(exception.value) == "Maximum 15 characters"

    



