import pytest
from player import Player, FightResult, RunAwayResult
from enemy import Enemy, EnemyType

"""
Equivalence Classes for fight Method:
Player's Health vs. Enemy's Strength:
Equivalence Class 1: Player's health > Enemy's strength (Expect WIN)
Equivalence Class 2: Player's health <= Enemy's strength (Expect LOSE)
"""

def test_fight_win():
    # Test the fight method with player's health greater than enemy's strength
    player = Player(1, "Alice", "Female", "Human", "Sword")
    player.increase_health(5)
    enemy = Enemy(EnemyType.GIANT_SPIDER, 6, 6)  # Choose an enemy for testing
    assert player.fight(enemy) == FightResult.WIN

def test_fight_lose():
    # Test the fight method with player's health less than enemy's strength
    player = Player(1, "Alice", "Female", "Human", "Sword")
    enemy = Enemy(EnemyType.DRAGON, 20, 20)  # Choose an enemy for testing
    assert player.fight(enemy) == FightResult.LOSE

"""
Equivalence Classes for run_away Method:
Player's Stamina:
Equivalence Class 1: Player's stamina > 3 (Expect SUCCESS)
Equivalence Class 2: Player's stamina <= 3 (Expect FAILURE)
"""

def test_run_away_success():
    # Test the run_away method with player's stamina greater than 3
    player = Player(1, "Alice", "Female", "Human", "Sword")
    enemy = Enemy(EnemyType.GOBLIN, 4, 5)  # Choose an enemy for testing
    assert player.run_away(enemy) == RunAwayResult.SUCCESS

def test_run_away_failure():
    # Test the run_away method with player's stamina less than or equal to 3
    player = Player(1, "Alice", "Female", "Human", "Sword")
    enemy = Enemy(EnemyType.DRAGON, 8, 8)  # Choose an enemy for testing
    # First run is succesfull
    player.run_away(enemy)
    # Second is failure
    assert player.run_away(enemy) == RunAwayResult.FAILURE 


