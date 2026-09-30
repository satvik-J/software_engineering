# Traffic Escape

Cross 8 lanes of oncoming traffic to reach the other side (Frogger-style).

## Setup

```bash
pip install -r requirements.txt
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| A/D or Left/Right | Change lane |
| W / UP | Move forward |
| S / DOWN | Move back |
| R | Restart |

## Tasks to Complete

### Task 1: Lives System

I am working on the Traffic Escape Python game in this repository.

Read the existing code carefully before making changes.

Implement Task 1 from the README: Lives System.

Requirements:
- The player should start with exactly 3 lives.
- Whenever the player gets hit by a car, reduce the lives by 1.
- Display the current number of lives clearly on the game screen.
- When lives reach 0, show a Game Over state.
- The player should not immediately lose multiple lives from a single collision.
- Allow the player to restart the game using the existing R key behavior.
- Preserve all existing gameplay and controls.
- Do not remove or break any existing functionality.
- Make the smallest clean changes necessary.
- After making the changes, explain which files were modified and how the implementation works.



### Task 2: Moving Log/Raft Lane
Now implement Task 2 from the README.

Add a safe water lane where the player must use a moving log/raft to cross.

Requirements:
- Add a dedicated safe/water lane.
- Add one or more logs/rafts that move horizontally across this lane.
- The player should be able to stand on the moving log.
- When the player is standing on the log, the player should move along with it.
- If the player enters the water without being on a log, treat it as a failed crossing/collision and apply the game's life-loss behavior.
- The log should continuously move and wrap/reappear when it leaves the screen.
- Keep the existing traffic lanes and controls working.
- Integrate this cleanly with the existing game architecture.
- Do not remove the lives system we just implemented.
- Make only the necessary changes.
- Explain the files and logic you changed after implementing it.



### Task 3: High Score Table
> Track and display the top 5 scores across sessions (save to JSON).
Now implement Task 3 from the README.

Add a persistent Top 5 High Score system.

Requirements:
- Track the player's score during gameplay.
- Display the current score on screen.
- When a game ends, allow the score to be considered for the leaderboard.
- Store the top 5 scores persistently in a JSON file.
- The scores must remain available after closing and reopening the game.
- Sort the scores from highest to lowest.
- Keep only the best 5 scores.
- Display the Top 5 leaderboard clearly in the game.
- If the JSON file does not exist, create it automatically.
- Handle invalid or missing JSON data safely.
- Do not break the existing lives, raft, traffic, controls, or game-over behavior.
- Make the implementation consistent with the existing project structure.


### Task 4: Day/Night Cycle
> Every 30 seconds switch between day and night. At night, cars have headlights visible further ahead.
Now implement Task 4 from the README.

Add a day/night cycle.

Requirements:
- The game should automatically switch between day and night every 30 seconds.
- The transition should continue throughout gameplay.
- Make the visual appearance clearly different between day and night.
- During night mode, car headlights should be visible and illuminate farther ahead.
- Headlights should be visually noticeable but should not interfere with collision detection.
- Display a small indicator showing whether the game is currently in DAY or NIGHT mode.
- Keep all existing functionality working, including lives, moving raft, scoring, leaderboard, traffic, controls, and restart.
- Use the existing game architecture rather than rewriting the entire project.
- Avoid unnecessary changes.
- Explain exactly how the 30-second timer and night headlights work.

## Folder Structure

```
traffic-escape/
├── main.py
├── requirements.txt
├── game/
│   ├── __init__.py
│   ├── game_engine.py
│   ├── player.py
│   └── traffic.py
└── README.md
```

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history

