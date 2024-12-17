The following is required for a riichi mahjong game state:

### Individual Player State:

1. **Hand Information:**

   - **Hand tiles (13-14 tiles):** Correct. Note that the hand should always have 13 tiles, and drawing a 14th tile is part of the game flow.
   - **Last drawn tile:** Useful for determining the winning tile or for the latest action.
   - **Exposed tiles (from chi, pon, kan calls):** Important for tracking melds.
   - **Open/closed status:** Indicates whether the player has exposed any tiles.
   - **Tenpai status:** Crucial for determining if the player is ready to win.
   - **Discarded tiles:** Needed for tracking the discard history.
   - **Latest discard:** Useful for recent actions.

2. **Player Status:**
   - **Score:** Essential for tracking the game's progress.
   - **Seat wind position:** Important for scoring and hand values.
   - **Riichi status:** Indicates if the player has declared riichi.
   - **Ippatsu eligibility:** Should be tied to the riichi declaration.
   - **Dealing status (current dealer?):** Needed for round progression.
   - **Furiten status:** Crucial for determining if a player is in a furiten state.

### Shared Game State:

1. **Wall Information:**

   - **Remaining tiles in wall:** Important for determining the game's progression.
   - **Dead wall count:** Needed for dora indicators and other game mechanics.
   - **Number of kans declared:** Influences the game's flow and scoring.

2. **Round Information:**

   - **Round wind:** Essential for scoring and hand values.
   - **Dealer position:** Needed for round progression.
   - **Current turn (whose turn is it):** Important for game flow.
   - **Current hand number in round:** Useful for tracking the progression within the round.

3. **Dora Information:**

   - **Dora indicators (visible):** Crucial for scoring.
   - **Ura dora indicators (hidden until riichi win):** Also important for scoring.
   - **Kan dora indicators:** Should be considered if kans affect dora.

4. **Table Stakes:**

   - **Riichi sticks count:** Needed for scoring.
   - **Tsumi sticks count:** Should be clarified; typically, tsumi refers to penalties, but in riichi, it might not be standard.

5. **Abort Conditions:**

   - **Four-wind call count in first round:** Important for game progression.
   - **Riichi declaration count:** Useful for aborting the game under certain conditions.
   - **Kan declaration count:** Influences game flow and potential aborts.
   - **Sacred discard rules in effect:** Needed for specific game mechanics.

6. **Game Progress:**
   - **All-last status:** Crucial for scoring and game progression.
   - **Current hand number overall:** Useful for tracking the overall game progress.
   - **Number of honba:** Important for scoring and hand values.

### Additional Considerations:

- **Tile Ownership:** It might be useful to track which tiles belong to which player, especially for exposed melds.
- **Riichi Declaration Timing:** You might want to track when a player declared riichi, as it affects the game's flow and scoring.
- **Winning Hand Information:** When a player wins, you need to track the winning hand's composition, yaku (patterns), and han (value) for scoring purposes.
- **Player Order:** The seating order and wind positions are essential for scoring and game progression.
- **Game Mode:** If you're implementing different game modes or rule variations, you might need to include game mode settings.
- **Penalties and Bonuses:** Some game mechanics might involve penalties or bonuses that need to be tracked.

### Potential Redundancies:

- **Discarded Tiles vs. Latest Discard:** If you track the history of discarded tiles, the latest discard can be derived from it. However, having a separate field for the latest discard can optimize access.
- **Riichi Sticks vs. Tsumi Sticks:** Ensure that these are necessary for your implementation, as they might not be standard in all riichi mahjong rule sets.

### Conclusion:

Your structure is quite comprehensive, but you might need to add some details related to scoring, game progression, and specific game mechanics. Additionally, ensure that you're not tracking redundant information and that your data structures are optimized for performance, especially if you plan to use this for an AI player.

By carefully considering these aspects, you can create a robust and efficient game state representation for your riichi mahjong AI.
