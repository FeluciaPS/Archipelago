from __future__ import annotations

from dataclasses import dataclass
from Options import Choice

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..world import GarfKartWorld


class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.

    - Grand Prix: Get first place in every grand prix cup
    - Races: Get first place in every race
    - Time Trials: Gain medals in all time trials (READ BELOW)
    - Puzzle Piece Hunt: Collect puzzle pieces

    Note on time trials: Although the game generates, please check for mod support
    before enabling this option, and beware that not all time trials may be
    beatable with the current logic and you could get stuck.
    """
    display_name = "Goal"

    default = 0
    option_grand_prix = 0
    option_races = 1
    option_time_trials = 2
    option_puzzle_piece_hunt = 3

class CCRequirement(Choice):
    """
    Sets the CC requirement for the Grand Prix and Races goals. Other ccs may still 
    give checks depending on other options.

    If the goal is not Grand Prix or Races, this option does nothing.
    """
    display_name = "CC Requirement"

    default = 0
    option_any = 0
    option_50cc = 1
    option_100cc = 2
    option_150cc = 3

class TimeTrialGoalGrade(Choice):
    """
    Sets the minimum medal grade required for the Time Trials goal
    !!!IMPORTANT!!! Platinum medals require certain kart combinations to be 
    reasonably achievable. These aren't implemented in logic yet, so randomizing
    kart loadouts may lead to impossible games.

    If the goal is not Time Trials, this option does nothing.
    """
    display_name = "Time Trials Goal Grade"

    default = 2
    option_bronze = 0
    option_silver = 1
    option_gold = 2
    option_platinum = 3