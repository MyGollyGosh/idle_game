## AI powered Idle Game (Pygame)

A small top-down idle/interaction game built with Pygame. Explore the overworld and a bustling town as our fated hero.

Idle games are all the rage now. This game takes the idea of what if we could use AI to dynamically create a new story for us each time based on how long we had been idle? 

Speak to to the wisp to hear your completely unique tale.

### Features
- **AI powered story telling** with interaction based on the time you have been idle
- **Overworld and House maps** with transition tiles between scenes
- **Animated player sprite** with directional movement
- **Obstacle and collision system** including invisible blockers
- **Dialogue system** with paginated text for the wisp
- **60 FPS loop** with delta-time based movement
- **1280×720 window** with simple UI prompts

## Getting Started

**.env** file is needed with a Groq key. This can be generated for free with an account here https://groq.com/

### Prerequisites
- **Python 3.9+**
- pip

### Setup
```bash
# Clone the repo
git clone <https://github.com/MyGollyGosh/idle_game>
cd idle_game

# (Recommended) Create and activate a virtual environment
python3 -m venv idle_game_venv
source idle_game_venv/bin/activate  # macOS/Linux
# .\\idle_game_venv\\Scripts\\activate  # Windows PowerShell

# Install dependencies
pip install -r requirements.txt
```

### Run
```bash
python3 app.py
```

## Controls
- **W/A/S/D**: Move
- **SPACE**: Interact/advance dialogue (when near the wisp)

## Project Structure
```text
idle_game/
  app.py                   # Main game loop and state machine
  requirements.txt         # Python dependencies (pygame)
  assets/                  # Sprites and backgrounds (map, floor, characters)
  lib/
    player.py              # Player sprite, animation, movement, collisions
    house.py               # House sprite/group wrapper
    generate_text.py       # Text utilities (if used by dialogue)
    tiles/                 # Tile sprites (tree, water, wisp, transitions, etc.)
    tile_maps/             # Map layouts (overworld, house)
  stories.db               # SQLite story data
  sqlite_story_script.py   # Script to manage story database
```

## How It Works
- `app.py` initializes the game, loads the current map, and manages states: `starting`, `in overworld`, `talking`, `in house`.
- Map generation uses 16×16 tiles from `lib/tile_maps/overworld.py` and `lib/tile_maps/house.py`.
- Collision uses a dedicated `hitbox` and checks against both visible and invisible obstacles.
- Dialogue with the wisp is paginated; SPACE advances chunks of text.

## Assets and Attribution
- Tiles: `free_art/Cute_Fantasy_Free` (Cute Fantasy Free tiles)
- Sprites: in `assets/` (e.g., `adventurer.png`, `wisp.png`, `map.png`, `floor.png`)

Please include proper attribution per the asset license if required by the source.

## Troubleshooting
- **ModuleNotFoundError: pygame**  
  Activate your venv and install deps:
  ```bash
  source idle_game_venv/bin/activate
  pip install -r requirements.txt
  ```
- **Black window or no input**  
  Ensure the `assets/` paths exist and you’re running from the project root.

## Things I'd like to change
- Many rough edges with hit boxes. Would like to smooth them out.
- Would like to add open door animation to smooth our entering a house
- Have player spawn at house they just exited when they exit
- Add functionality to view previous stories
- Add stats system that would change and upgrade based on the story generated and help shape further stories
- Add collectable daily chest to bottom of cliff edge
-- many more honestly but right now I just wanted to get the core functionality working of having a game where when you jump on a personalised story is created based on the time you have been away.