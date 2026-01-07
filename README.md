# 👹 cliGoblin v1.0.1

> "Oh. You again. Took you long enough."

**cliGoblin** is a persistent "living" terminal pet. It runs as a CLI tool but maintains its own internal state (hunger, mood, health) that evolves over time, even when you aren't running it.

### 🆕 What's New in v1.0.1
*   **Art Fix:** The "Rust Crab" has been correctly identified as a **Rust Bunny**.
*   **Full Release:** Stability improvements and documentation updates.

## 📦 Installation

1. **Clone or Download** this repository.
2. **Setup Environment**:
   Modern Linux systems often prevent global pip installs. Use a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install the Package**:
   ```bash
   pip install -e .
   ```
   *Note: If you don't want to use a virtual environment, you can use `pip install . --break-system-packages` (not recommended).*

4. **Verify Installation**:
   ```bash
   cligoblin --help
   ```

## 🚀 Quick Start

1. **Birth your Goblin**:
   ```bash
   cligoblin init
   ```
2. **Check Status**:
   ```bash
   cligoblin status
   ```
3. **Interactive Watch Mode** (Live animations):
   ```bash
   cligoblin watch
   ```

## 🥣 Care & Commands

| Command | Description |
| :--- | :--- |
| `cligoblin status` | Shows current stats, ASCII art, and dialogue. |
| `cligoblin feed` | Decreases hunger, increases bond. |
| `cligoblin play` | Increases mood, consumes energy, increases bond. |
| `cligoblin watch` | Enters a live loop where the goblin animates on screen. |
| `cligoblin menu` | Opens interactive settings menu (Rename, Minimal Mode, Dev). |

### 🧠 Shell Integration

To make your goblin react to your commands, you can alias it or use the `--last` flag.

**Bash/Zsh Alias:**
Add this to your `.bashrc` or `.zshrc`:
```bash
alias critter='/path/to/cliGoblin/venv/bin/cligoblin'
```

**Command Watching:**
You can tell the goblin what you just did, and it might comment on it:
```bash
critter status --last "git push --force"
```

## 🏗 Project Structure

*   `src/goblin.py`: Core logic for stats and time decay.
*   `src/cli.py`: Command-line interface and dialogue engine.
*   `src/art.py`: ASCII art assets.
*   `src/state_manager.py`: Handles saving/loading JSON state to `~/.cligoblin/`.

## 📜 License
MIT
