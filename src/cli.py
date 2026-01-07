import argparse
import sys
import getpass
import time
from .state_manager import load_state, save_state
from .goblin import Goblin
from .art import get_art
from .dialogue import get_dialogue
from .ui import run_menu, live_watch

def main():
    parser = argparse.ArgumentParser(description="CLI Goblin - Your terminal pet")
    parser.add_argument("command", nargs="?", choices=["status", "feed", "play", "init", "watch", "dev", "menu", "hunt", "collection", "dex"], default="status")
    parser.add_argument("--last", help="The last command you ran (to let the goblin watch)")
    
    # Dev mode arguments
    parser.add_argument("--set-hunger", type=float, help="[Dev] Set hunger level (0-100)")
    parser.add_argument("--set-health", type=float, help="[Dev] Set health level (0-100)")
    parser.add_argument("--set-energy", type=float, help="[Dev] Set energy level (0-100)")
    parser.add_argument("--set-bond", type=int, help="[Dev] Set bond level")
    parser.add_argument("--set-care", type=float, help="[Dev] Set care score")
    parser.add_argument("--time-travel", type=float, help="[Dev] Advance time by N hours (can be negative)")
    
    args = parser.parse_args()
    
    state = load_state()
    
    if args.command == "init" or state is None:
        if state is None:
            print("A new goblin egg has appeared in your terminal!")
            name = input("What will you name it? ")
            user = getpass.getuser()
            goblin = Goblin(name=name)
            goblin.username = user
            save_state(goblin.to_dict())
            print(f"{name} has hatched!")
        else:
            print("You already have a goblin!")
        return

    goblin = Goblin(state=state)
    
    if args.command == "dev":
        pwd = getpass.getpass("Enter Developer Password: ")
        if pwd != "GobbyDev":
            print("Access Denied. The goblin bites your finger.")
            return
        
        print(f"🔧 Developer Mode Accessed for {goblin.name}")
        changes_made = False
        
        if args.set_hunger is not None:
            goblin.hunger = max(0, min(100, args.set_hunger))
            print(f"Set Hunger to {goblin.hunger}")
            changes_made = True
            
        if args.set_health is not None:
            goblin.health = max(0, min(100, args.set_health))
            print(f"Set Health to {goblin.health}")
            changes_made = True
            
        if args.set_energy is not None:
            goblin.energy = max(0, min(100, args.set_energy))
            print(f"Set Energy to {goblin.energy}")
            changes_made = True
            
        if args.set_bond is not None:
            goblin.bond = args.set_bond
            print(f"Set Bond to {goblin.bond}")
            changes_made = True

        if args.set_care is not None:
            goblin.care_score = args.set_care
            print(f"Set Care Score to {goblin.care_score}")
            changes_made = True
            
        if args.time_travel is not None:
            # Adjust last_update to simulate time passing
            seconds = args.time_travel * 3600
            goblin.last_update -= seconds
            print(f"Time traveled {args.time_travel} hours.")
            changes_made = True
            
        if not changes_made:
            print("No changes specified. Use --set-hunger, --time-travel, etc.")
        else:
            goblin.update_mood_string() # Refresh mood based on new stats
            save_state(goblin.to_dict())
            print("State updated successfully.")
        return
        
    if args.command == "watch":
        live_watch(goblin)
        return

    if args.command == "menu":
        run_menu(goblin)
        return

    # Calculate dialogue BEFORE update so we can use old state for "last interaction"
    elapsed = time.time() - goblin.last_update
    dialogue = get_dialogue(goblin)
    if elapsed > 86400 and goblin.mood != "dead":
        dialogue = f"Oh. You again. Took you long enough. (Last seen: {int(elapsed/3600)} hours ago)"

    goblin.update(command_watched=args.last)
    
    if args.command == "status":
        if not goblin.settings.get("minimal_mode"):
            print(get_art(goblin.mood))
        print(f"--- {goblin.name} ---")
        print(f"Mood: {goblin.mood}")
        print(f"Hunger: {goblin.hunger:.1f}%")
        print(f"Energy: {goblin.energy:.1f}%")
        print(f"Health: {goblin.health:.1f}%")
        print(f"Bond: {goblin.bond}")
        print(f"\n{goblin.name}: \"{dialogue}\"")
    
    elif args.command == "feed":
        print(goblin.feed())
        
    elif args.command == "play":
        print(goblin.play())

    elif args.command == "hunt":
        creature, msg = goblin.hunt()
        print(msg)
        if creature:
            print(creature['art'])
            print(f"Name: {creature['name']}")
            print(f"Rarity: {creature['rarity']}")
            print(f"Desc: {creature['desc']}")
            
    elif args.command in ["collection", "dex"]:
        if not goblin.collection:
            print(f"{goblin.name} hasn't caught anything yet. Try 'hunt'!")
        else:
            print(f"--- 📦 {goblin.name}'s Collection ({len(goblin.collection)}) ---")
            for c in goblin.collection:
                print(f"[{c['rarity']}] {c['name']} - {c['desc']}")
    
    save_state(goblin.to_dict())

if __name__ == "__main__":
    main()