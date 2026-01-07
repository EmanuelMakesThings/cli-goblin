# 📖 The Goblin Care Guide

So, you've hatched a cliGoblin. Unlike standard scripts, this process simulates "life." If you leave it alone for a week, you might come back to a very angry (or very dead) text file.

## 📊 Vital Statistics

Your goblin tracks 5 core stats. All of them decay or change based on **real-world time**.

### 1. Hunger 🍖
*   **Increases:** ~10% per hour.
*   **Effect:** If Hunger > 80%, **Health** starts dropping and the goblin becomes **Feral**.
*   **Fix:** `cligoblin feed`

### 2. Energy ⚡
*   **Decreases:** When you `play`.
*   **Recharges:** Slowly over time (2% per hour).
*   **Effect:** If Energy is too low (< 20%), the goblin will refuse to play.

### 3. Mood 🎭
Determines the ASCII art and dialogue.
*   **Happy:** High Health, Low Hunger, High Mood Value.
*   **Bored:** Ignored for a while, Mood Value drops.
*   **Anxious:** Mood Value fluctuates, often triggered by neglect.
*   **Feral:** Hunger > 80%. It will hiss at you.
*   **Sick:** Health < 30%.
*   **Corrupted:** Health < 10%. (Art becomes glitchy).

### 4. Health ❤️
*   **Impact:** Only drops if the goblin is starving (Hunger > 80%).
*   **Recovery:** Slowly recovers if Hunger is low.

### 5. Bond / Care Score 🤝
*   **Grows:** When you `feed` or `play`.
*   **Decays:** When you starve the goblin.
*   **Effect:** Changes the tone of the dialogue.
    *   *High Bond:* "You're actually pretty nice, for a human."
    *   *Low Bond:* "I'm starting to think you're trying to see how long I can last without food."

### 6. Creature Collection 🦋
Gobby isn't the only thing living in your terminal.
*   **Command:** `cligoblin hunt`
*   **Cost:** 30 Energy.
*   **Effect:** Gobby explores the system and might find a creature to add to your collection.
*   **Rarity:**
    *   Common (50%): Glitch Bugs, Bash Worms
    *   Uncommon (30%): PySnakes, Lil' Daemons
    *   Rare (15%): Rust Crabs
    *   Legendary (5%): Root Penguins
*   **View Collection:** `cligoblin collection` (or `dex`)
*   **Manage Collection:** Open `cligoblin menu` and select "Inventory". Here you can view details, see the art, and **rename** your creatures.

---

## 🗣️ Reactive Personality

Your goblin is watching (sometimes).

### Time of Day
*   **Late Night:** It might ask why you're still awake.
*   **Morning:** It expects coffee.

### Neglect
If you haven't run `cligoblin` in over 24 hours, expect passive-aggressive comments:
> "Oh. You again. Took you long enough."

### Command Awareness
If you use the `--last` flag (or build a wrapper script), the goblin reacts to specific keywords:
*   `git`: It knows you are stressed.
*   `rm`: It gets nervous about deletion.

---

## 🚑 Emergency Recovery

**"My goblin is Feral/Sick! What do I do?"**

1.  **Feed it immediately.** You might need to run `cligoblin feed` multiple times to get Hunger under 80%.
2.  **Wait.** Health regenerates slowly once it's not starving.
3.  **Play.** Once it's healthy, play with it to restore the Bond score.

**"My goblin died/state is broken."**

The state is stored in `~/.cligoblin/state.json`.
*   **Hard Reset:** Delete that file to hatch a new egg.
