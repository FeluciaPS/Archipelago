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

class PuzzlePieceCount(Range):
    """
    Sets the amount of puzzle pieces added to the item pool. If the goal is Puzzle Piece Hunt, 
    this is the amount of puzzle pieces required to beat the game. 

    If puzzle pieces aren't randomized, this option does nothing.
    """

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
    display_name = "Time Trials Goal Grade"

    default = 2
    option_bronze = 0
    option_silver = 1
    option_gold = 2
    option_platinum = 3

##
# Randomizer Options
##
class RandomizeRaces(Choice):
    """
    Sets how to shuffle race unlocks into the item pool

    - Cups: Grand Prix cup unlocks are shuffled into the item pool, races unlock when you unlock their cup
    - Races: Race unlocks are shuffled into the item pool, cups unlock when you've unlocked all races in the cup
    - Cups and Races: Race and cup unlocks are shuffled into the item pool, playing a cup requires all 4 races and the cup item
    """
    display_name = "Randomize Races"
    default = 0

    option_cups = 0
    option_races = 1
    option_cups_and_races = 2

class ProgressiveCups(Toggle):
    """
    Starts the game with the first cup onlocked, then unlocks them in order
    every time a "Cup Unlock" item is found.
    Turning this off unlocks cups in random order with their specific items.

    This option does nothing if cups aren't randomized
    """
    display_name = "Progressive Cups"

class RandomizePuzzlePieces(Toggle):
    """
    Adds puzzle pieces to the item pool.
    
    Always on when the goal is Puzzle Piece Hunt
    """
    display_name = "Randomize Puzzle Pieces"

class RandomizeCharacters(Toggle):
    """
    Adds characters to the item pool, and adds a location for winning a race as each character.
    """
    visibility = Visibility.none

    display_name = "Randomize Characters"

class RandomizeCars(Toggle):
    """
    Adds cars to the item pool, and adds a location for winning a race with each car.
    """
    visibility = Visibility.none

    display_name = "Randomize Cars"

class RandomizeHats(Choice):
    """
    Adds hats to the item pool

    - Off: Hats are unlocked in their vanilla locations
    - Progressive: Always unlock bronze hats first, then silver, then gold
    - Combine Tiers: Unlocking a hat instantly unlocks bronze, silver, and gold
    """
    display_name = "Randomize Hats"
    default = 0

    option_off = 0
    option_progressive = 1
    option_combine_tiers = 2

class RandomizeSpoilers(Choice):
    """
    Adds spoilers to the item pool

    - Off: Spoilers are unlocked in their vanilla locations
    - Progressive: Always unlock bronze spoilers first, then silver, then gold
    - Combine Tiers: Unlocking a spoiler instantly unlocks bronze, silver, and gold
    """
    display_name = "Randomize Spoilers"
    default = 0

    option_off = 0
    option_progressive = 1
    option_combine_tiers = 2

class LapCount(Range):
    """
    Modifies the amount of laps in a race 
    """
    display_name = "Lap Count"
    default = 3

    range_start = 1
    range_end = 10

class DisableCPUItems(Toggle):
    """
    Prevents CPUs from using items for a less chaotic experience.
    """
    display_name = "Disable CPU Items"

class SpringsOnly(Toggle):
    """
    Item boxes can only give springs. This makes puzzle piece hunting a lot easier.

    If Randomize Items is enabled, you start without springs unlocked and item boxes
    do nothing.
    """
    display_name = "Springs Only"

class RandomizeItems(Toggle):
    """
    Randomizes the items that can be received from item boxes and adds locations for
    acquiring each item from an item box for the first time. 
    Always starts with one item unlocked, unless Springs Only is enabled.
    """
    display_name = "Randomize Items"

class TrapPercentage(Range):
    visibility = Visibility.none

    display_name = "Trap Percentage"
    
    range_start = 0
    range_end = 100
    default = 0

class DeathLink(Toggle):
    """
    Enables Death Link.
    """
    visibility = Visibility.none # I don't even know if we're adding this

    display_name = "Death Link"


@dataclass
class GarfKartOptions(PerGameCommonOptions):
    # Goal Options
    goal: Goal
    cc_requirement: CCRequirement
    time_trial_goal_grade: TimeTrialGoalGrade

    # Race Randomizer Options
    randomize_races: RandomizeRaces
    progressive_cups: ProgressiveCups

    # Puzzle Piece Options
    randomize_puzzle_pieces: RandomizePuzzlePieces
    puzzle_piece_count: PuzzlePieceCount

    # Character Options
    randomize_characters: RandomizeCharacters
    randomize_cars: RandomizeCars
    randomize_hats: RandomizeHats
    randomize_spoilers: RandomizeSpoilers

    # Game Options
    lap_count: LapCount
    disable_cpu_items: DisableCPUItems
    springs_only: SpringsOnly
    """
    Other game option ideas:
    - cpu_scaling (scales CPU car speed up/down by a percentage)
    - rubber_banding (scales CPU rubber banding settings to speed them up when they're significantly behind and
        slow them down when they're significantly ahead)
    - no_cpu (disable CPUs entirely)
    """


    # Other Randomizer Options
    randomize_items: RandomizeItems
    trap_percentage: TrapPercentage
    death_link: DeathLink


option_groups = [
    OptionGroup(
        "Goal Options",
        [Goal, CCRequirement, TimeTrialGoalGrade],
    ),
    OptionGroup(
        "Race Randomizer Options",
        [RandomizeRaces, ProgressiveCups],
    ),
    OptionGroup(
        "Puzzle Piece Options",
        [RandomizePuzzlePieces, PuzzlePieceCount]
    ),
    OptionGroup(
        "Character Options",
        [RandomizeCharacters, RandomizeCars, RandomizeHats, RandomizeSpoilers]
    ),
    OptionGroup(
        "Game Options",
        [LapCount, DisableCPUItems, SpringsOnly],
    ),
    OptionGroup(
        "Other Randomizer Options",
        [RandomizeItems, TrapPercentage, DeathLink],
    ),
]