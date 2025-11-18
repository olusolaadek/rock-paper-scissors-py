"""Simple Rock-Paper-Scissors game.

Features:
- Input validation (accepts full words or first letter: r/p/s)
- Replay loop with scoreboard
- Graceful exit via 'q' or 'exit'
"""

from __future__ import annotations

import random
from typing import Literal, Optional

Choice = Literal["rock", "paper", "scissors"]

VALID_CHOICES: tuple[Choice, ...] = ("rock", "paper", "scissors")
ALIASES: dict[str, Choice] = {
    "r": "rock",
    "p": "paper",
    "s": "scissors",
}


def get_player_choice() -> Optional[Choice]:
    """Prompt the user for a choice.

    Returns a normalized choice or None if the user wants to quit.
    """
    while True:
        raw = (
            input("Enter your choice (rock/paper/scissors) or (q to quit): ")
            .strip()
            .lower()
        )
        if raw in {"q", "quit", "exit"}:
            return None
        if raw in ALIASES:
            return ALIASES[raw]
        if raw in VALID_CHOICES:
            return raw  # type: ignore[return-value]
        print("Invalid input. Try again (rock, paper, scissors, or q to quit).")


def get_computer_choice() -> Choice:
    return random.choice(VALID_CHOICES)


def decide_winner(player: Choice, computer: Choice) -> Literal["win", "lose", "draw"]:
    if player == computer:
        return "draw"
    winning_pairs = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }
    return "win" if (player, computer) in winning_pairs else "lose"


def format_result(player: Choice, computer: Choice, outcome: str) -> str:
    if outcome == "draw":
        return f"Both chose {player}. It's a draw!"

    phrases: dict[tuple[Choice, Choice], str] = {
        ("rock", "scissors"): "Rock crushes scissors",
        ("paper", "rock"): "Paper covers rock",
        ("scissors", "paper"): "Scissors cut paper",
    }

    # Resolve an action phrase regardless of order, with safe fallback
    action = phrases.get((player, computer)) or phrases.get((computer, player))
    if action is None:
        action = f"{player.title()} vs {computer.title()}"

    if outcome == "win":
        prefix = "You win!"
    else:  # outcome == "lose"
        prefix = "You lose!"

    return f"{prefix} {action}. (You: {player} | Computer: {computer})"


def main() -> None:
    wins = losses = draws = 0
    round_num = 1
    while True:
        print(f"-- Round {round_num} --")
        player_choice = get_player_choice()
        if player_choice is None:
            break
        computer_choice = get_computer_choice()
        outcome = decide_winner(player_choice, computer_choice)
        if outcome == "win":
            wins += 1
        elif outcome == "lose":
            losses += 1
        else:
            draws += 1
        print(format_result(player_choice, computer_choice, outcome))
        print(f"Score => Wins: {wins} | Losses: {losses} | Draws: {draws}\n")
        round_num += 1

    print("Thanks for playing! Goodbye. 👋")


if __name__ == "__main__":  # pragma: no cover
    main()
