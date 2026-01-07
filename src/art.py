IDLE = r"""
   (o_o)
   <) )>
    / \
"""

SLEEPING = r"""
   (-_-) zZ
   <) )>
    / \
"""

EXCITED = r"""
   \(^o^)/
    (   )
    /   \
"""

ANGRY = r"""
   (>_<)
   <) )>
    / \
"""

SICK = r"""
   (x_x)
   <) )>
    / \
"""

WATCHING = r"""
   ( @ @ )
    ( - )
    /   \
"""

CORRUPTED = r"""
   (?.?)
   <| |>
    / \
"""

DEAD = r"""
   (x_x)
   --|--
    / \
   [DEAD]
"""

def get_art(mood):
    if mood == "dead":
        return DEAD
    elif mood == "happy":
        return IDLE
    elif mood == "bored":
        return SLEEPING
    elif mood == "anxious":
        return WATCHING
    elif mood == "feral":
        return ANGRY
    elif mood == "sick":
        return SICK
    else:
        return CORRUPTED
