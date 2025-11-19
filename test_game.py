"""Unit tests for Rock-Paper-Scissors game."""

import unittest
from unittest.mock import patch
from game import (
    get_player_choice,
    get_computer_choice,
    decide_winner,
    format_result,
    VALID_CHOICES,
)


class TestRockPaperScissors(unittest.TestCase):
    def test_get_computer_choice(self):
        """Test that computer choice is always valid."""
        for _ in range(100):  # Test multiple times due to randomness
            choice = get_computer_choice()
            self.assertIn(choice, VALID_CHOICES)

    @patch("builtins.input", side_effect=["rock"])
    def test_get_player_choice_valid_full(self, mock_input):
        """Test valid full word input."""
        choice = get_player_choice()
        self.assertEqual(choice, "rock")

    @patch("builtins.input", side_effect=["r"])
    def test_get_player_choice_valid_alias(self, mock_input):
        """Test valid alias input."""
        choice = get_player_choice()
        self.assertEqual(choice, "rock")

    @patch("builtins.input", side_effect=["q"])
    def test_get_player_choice_quit(self, mock_input):
        """Test quit input."""
        choice = get_player_choice()
        self.assertIsNone(choice)

    @patch("builtins.input", side_effect=["invalid", "paper"])
    def test_get_player_choice_invalid_then_valid(self, mock_input):
        """Test invalid input followed by valid."""
        choice = get_player_choice()
        self.assertEqual(choice, "paper")

    def test_decide_winner_draw(self):
        """Test draw outcome."""
        self.assertEqual(decide_winner("rock", "rock"), "draw")

    def test_decide_winner_win(self):
        """Test win outcomes."""
        self.assertEqual(decide_winner("rock", "scissors"), "win")
        self.assertEqual(decide_winner("paper", "rock"), "win")
        self.assertEqual(decide_winner("scissors", "paper"), "win")

    def test_decide_winner_lose(self):
        """Test lose outcomes."""
        self.assertEqual(decide_winner("rock", "paper"), "lose")
        self.assertEqual(decide_winner("paper", "scissors"), "lose")
        self.assertEqual(decide_winner("scissors", "rock"), "lose")

    def test_format_result_draw(self):
        """Test draw result formatting."""
        result = format_result("rock", "rock", "draw")
        self.assertIn("draw", result.lower())

    def test_format_result_win(self):
        """Test win result formatting."""
        result = format_result("rock", "scissors", "win")
        self.assertIn("you win", result.lower())
        self.assertIn("rock crushes scissors", result.lower())

    def test_format_result_lose(self):
        """Test lose result formatting."""
        result = format_result("rock", "paper", "lose")
        self.assertIn("you lose", result.lower())
        self.assertIn("paper covers rock", result.lower())


if __name__ == "__main__":
    unittest.main()
