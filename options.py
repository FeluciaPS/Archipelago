from __future__ import annotations

from dataclasses import dataclass
from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, Visibility

##
# Goal Options
##
class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.

    - Grand Prix: Get first place in every grand prix cup
    - Races: Get first place in every race
    - Time Trials: Gain medals in all time trials (DOES NOT WORK)
    - Puzzle Piece Hunt: Collect puzzle pieces
    """
    display_name = "Goal"

    default = 0
    option_grand_prix = 0
    option_races = 1
    option_time_trials = 2
    option_puzzle_piece_hunt = 3

class CCRequirement(Choice):
    """
    Sets the CC requirement for the Grand Prix and Races goals.

    If the goal is not one of those, this option does nothing.
    """
    visibility = Visibility.none # Not implemented

    display_name = "CC Requirement"

    default = 0
    option_any = 0
    option_50cc = 1
    option_100cc = 2
    option_150cc = 3

class PuzzlePieceCount(Range):
    """
    Sets the number of the 48 Puzzle Pieces required for the Puzzle Piece Hunt goal.

    If the goal is not Puzzle Piece Hunt, this option does nothing.
    """
    visibility = Visibility.none # Not implemented

    display_name = "Puzzle Piece Count"

    range_start = 1
    range_end = 48
    default = 48

class TimeTrialGoalGrade(Choice):
    """
    Sets the minimum medal grade required for the Time Trials goal
    !!!IMPORTANT!!! Platinum medals require certain car combinations to be 
    reasonably achievable. These aren't implemented in logic yet, so randomizing
    cart loadouts may lead to impossible games.

    If the goal is not Time Trials, this option does nothing.
    """
    visibility = Visibility.none # Not implemented

    display_name = "Time Trials Goal Grade"

    default = 0
    option_any = 0
    option_bronze = 1
    option_silver = 2
    option_gold = 3
    option_platinum = 4

##
# Randomizer Options
##
class RandomizeRaces(Choice):
    """
    Sets whether to shuffle race unlocks into the item pool

    - Cups: Grand Prix cup unlocks are shuffled into the item pool, races unlock when you unlock their cup
    - Races: Race unlocks are shuffled into the item pool, cups unlock when you've unlocked all races in the cup
    - Cups and Races: Race and cup unlocks are shuffled into the item pool, playing a cup requires all 4 races and the cup item
    """
    display_name = "Randomize Races"
    default = 0

    option_off = 0
    option_cups = 1
    option_races = 2
    option_cups_and_races = 3

class ProgressiveCups(Toggle):
    """
    Starts the game with the first cup onlocked, then unlocks them in order
    every time a "Cup Unlock" item is found.
    Turning this off unlocks cups in random order with their specific items.

    This option does nothing if cups aren't randomized
    """
    display_name = "Progressive Cups"

class RandomizeHats(Choice):
    """
    Adds hats to the item pool

    - Off: Hats are unlocked in their vanilla locations
    - Progressive: Always unlock bronze hats first, then silver, then gold
    - Gold Only: Only gold tier hats are added to the item pool
    - On: All tiers of all hats are added to the item pool

    !!!IMPORTANT!! only gold-only will be implemented in early versions
    """
    visibility = Visibility.none # Not implemented

    display_name = "Randomize Hats"
    default = 0

    option_off = 0
    option_progressive = 1
    option_gold_only = 2
    option_on = 3

class RandomizeSpoilers(Choice):
    """
    Adds spoilers to the item pool

    - Off: Spoilers are unlocked in their vanilla locations
    - Progressive: Always unlock bronze spoilers first, then silver, then gold
    - Combine Tiers: Unlocking a spoiler instantly unlocks bronze, silver, and gold
    - On: All tiers of all spoilers are added to the item pool

    !!!IMPORTANT!! only gold-only will be implemented in early versions
    """
    visibility = Visibility.none # Not implemented

    display_name = "Randomize Spoilers"
    default = 0

    option_off = 0
    option_progressive = 1
    option_combine_tiers = 2
    option_on = 3

class RandomizePuzzlePieces(Toggle):
    """
    Adds puzzle pieces to the item pool.
    
    Always on when the goal is Puzzle Piece Hunt
    """
    display_name = "Randomize Puzzle Pieces"


@dataclass
class GarfKartOptions(PerGameCommonOptions):
    # Goal Options
    goal: Goal
    cc_requirement: CCRequirement
    puzzle_piece_count: PuzzlePieceCount
    time_trial_goal_grade: TimeTrialGoalGrade

    # Randomizer Options
    randomize_races: RandomizeRaces
    progressive_cups: ProgressiveCups
    randomize_hats: RandomizeHats
    randomize_spoilers: RandomizeSpoilers
    randomize_puzzle_pieces: RandomizePuzzlePieces


option_groups = [
    OptionGroup(
        "Goal Options",
        [Goal, CCRequirement, PuzzlePieceCount, TimeTrialGoalGrade],
    ),
    OptionGroup(
        "Randomizer Options",
        [RandomizeRaces, ProgressiveCups, RandomizeSpoilers, RandomizeHats, RandomizePuzzlePieces],
    ),
]