import pytest
from hangman import Hangman

@pytest.fixture
def basic_game():
    game = Hangman('basic')
    game.puzzle = 'python'
    game.masked = '______'
    return game

def test_initialization_basic():
    game = Hangman('basic')
    assert game.puzzle != ''
    assert len(game.masked) == len(game.puzzle)
    assert game.lives == 6

def test_initialization_intermediate():
    game = Hangman('intermediate')
    assert ' ' in game.puzzle
    assert ' ' in game.masked

def test_correct_guess(basic_game):
    updated = basic_game.guess('p')
    assert updated == 'p_____'
    assert basic_game.lives == 6

def test_incorrect_guess(basic_game):
    updated = basic_game.guess('z')
    assert updated == '______'
    assert basic_game.lives == 5

def test_multiple_occurrences():
    game = Hangman('basic')
    game.puzzle = 'testing'
    game.masked = '_______'
    updated = game.guess('t')
    assert updated == 't__t___'

def test_is_won(basic_game):
    basic_game.masked = 'python'
    assert basic_game.is_won() == True
    basic_game.masked = 'p_thon'
    assert basic_game.is_won() == False

def test_is_lost(basic_game):
    basic_game.lives = 0
    assert basic_game.is_lost() == True
    basic_game.lives = 1
    assert basic_game.is_lost() == False