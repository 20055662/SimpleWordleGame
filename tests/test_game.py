import pytest
from src.game import score_guess

def test_score_guess_correct():
    assert score_guess("apple", "apple") == True

def test_score_guess_incorrect():
    assert score_guess("apple", "ample") == False
