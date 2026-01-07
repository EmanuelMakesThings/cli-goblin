# 🔧 Developer Mode Guide

This document outlines the hidden Developer Mode for `cliGoblin`, used for testing states, debugging animations, and manipulating time.

## 🔑 Access
**Command:** `cligoblin dev`
**Password:** `GobbyDev`

## 🛠 Commands

You can combine flags.

| Flag | Description |
| :--- | :--- |
| `--set-hunger [0-100]` | Set hunger level. >80 triggers Feral/Health decay. |
| `--set-health [0-100]` | Set health level. <30 is Sick, <10 is Corrupted. |
| `--set-energy [0-100]` | Set energy level. <20 prevents playing. |
| `--set-bond [int]` | Set the raw bond counter. |
| `--set-care [float]` | Set the Care Score (affects dialogue). |
| `--time-travel [hours]` | Advance time forward (positive) or backward (negative). |

Alternatively, use the interactive menu:
`cligoblin menu` -> **Developer Mode** -> Enter Password.
Inside the menu, you now have options to:
*   **Set Stats** (Hunger, Health, Energy)
*   **Time Travel**
*   **Kill Gobby** (Sets Health to 0)
*   **Reset/Revive Gobby** (Resets all stats to default)

## 🧪 Examples

**Make the goblin sick instantly:**
```bash
cligoblin dev --set-health 20 --set-hunger 0
```

**Simulate 24 hours of neglect:**
```bash
cligoblin dev --time-travel 24
```
*Note: Run `cligoblin status` afterwards to see the calculated decay from the time jump.*

**Reset to perfect condition:**
```bash
cligoblin dev --set-hunger 0 --set-health 100 --set-energy 100 --set-mood happy
```
