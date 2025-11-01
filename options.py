from __future__ import annotations

from dataclasses import dataclass
from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.

    - Cups: Beat all cups
    - Races: Beat all races
    - Time Trials: Beat all time trials
    - Puzzle Piece Hunt: Collect puzzle pieces
    """
    display_name = "Goal"
    default = 0
    option_cups = 0
    option_races = 1
    option_time_trials = 2
    option_puzzle_piece_hunt = 3

class PuzzlePieceCount(Range):
    """
    Sets the number of Puzzle Pieces required for the Puzzle Piece Hunt goal.

    If the goal is not Puzzle Piece Hunt, this option does nothing.
    """
    display_name = "Puzzle Piece Count"
    range_start = 1
    range_end = 48
    default = 48

class ProgressiveCups(Toggle):
    """
    Starts the game with the first cup onlocked, then unlocks them in order
    every time a "Cup Unlock" item is found.
    Turning this off unlocks cups in random order with their specific items.
    """
    display_name = "Progressive Cups"


@dataclass
class GarfKartOptions(PerGameCommonOptions):
    goal: Goal
    puzzle_piece_count: PuzzlePieceCount
    progressive_cups: ProgressiveCups


option_groups = [
    OptionGroup(
        "Goal Options",
        [Goal, PuzzlePieceCount],
    ),
    OptionGroup(
        "Randomizer Options",
        [ProgressiveCups],
    ),
]