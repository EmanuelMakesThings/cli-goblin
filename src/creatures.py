import random

# Rarity tiers
COMMON = "Common"
UNCOMMON = "Uncommon"
RARE = "Rare"
LEGENDARY = "Legendary"

CREATURES = [
    {
        "name": "Glitch Bug",
        "rarity": COMMON,
        "desc": "A tiny, harmless software error.",
        "art": r"""
    ,   ,
   (o_o)
   ( " )
  """
    },
    {
        "name": "Bash Worm",
        "rarity": COMMON,
        "desc": "It lives in your shell history.",
        "art": r"""
    ~o~
   ( _ )~
  """
    },
    {
        "name": "PySnake",
        "rarity": UNCOMMON,
        "desc": "It loves indentation.",
        "art": r"""
     __
    <oo>_
     \ \
      \_\_>
  """
    },
    {
        "name": "Lil' Daemon",
        "rarity": UNCOMMON,
        "desc": "Runs in the background.",
        "art": r"""
     , ,
    (>.<)
    /| |\
  """
    },
    {
        "name": "Rust Bunny",
        "rarity": RARE,
        "desc": "Fast and memory safe. Hoist the colors!",
        "art": r"""
    (\_/)
   (o.o)
   (> <)
  """
    },
    {
        "name": "Root Penguin",
        "rarity": LEGENDARY,
        "desc": "The king of the kernel.",
        "art": r"""
     ___
    ( o)>
    //\
    V_/_ 
  """
    }
]

def get_random_creature():
    roll = random.random()
    if roll < 0.5: # 50% Common
        tier = COMMON
    elif roll < 0.8: # 30% Uncommon
        tier = UNCOMMON
    elif roll < 0.95: # 15% Rare
        tier = RARE
    else: # 5% Legendary
        tier = LEGENDARY
        
    candidates = [c for c in CREATURES if c['rarity'] == tier]
    return random.choice(candidates)