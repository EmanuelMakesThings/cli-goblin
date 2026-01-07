import os
import time
import getpass
from .state_manager import save_state
from .art import IDLE, EXCITED, SLEEPING, ANGRY, WATCHING

def run_inventory(goblin):
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"--- 📦 {goblin.name}'s Inventory 📦 ---")
        if not goblin.collection:
            print("\n(Empty. Go 'hunt' to find creatures!)")
            input("\nPress Enter to go back...")
            return

        for idx, creature in enumerate(goblin.collection):
            print(f"{idx + 1}. [{creature['rarity']}] {creature['name']}")
        
        print(f"{len(goblin.collection) + 1}. Back")
        
        choice = input("\nSelect a creature to manage: ")
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(goblin.collection):
                selected = goblin.collection[idx]
                while True:
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print(selected['art'])
                    print(f"Name:   {selected['name']}")
                    print(f"Rarity: {selected['rarity']}")
                    print(f"Desc:   {selected['desc']}")
                    print("\n1. Rename")
                    print("2. Back")
                    
                    sub_choice = input("\nAction: ")
                    if sub_choice == "1":
                        new_name = input(f"Rename {selected['name']} to: ")
                        if new_name:
                            selected['name'] = new_name
                            save_state(goblin.to_dict())
                            print("Renamed!")
                            time.sleep(1)
                    elif sub_choice == "2":
                        break
            elif idx == len(goblin.collection):
                break

def run_menu(goblin):
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"--- ⚙️  {goblin.name}'s Settings Menu ⚙️  ---")
        print("1. Inventory / Collection 📦")
        print("2. Rename Goblin")
        print(f"3. Toggle Minimalist Mode (Current: {'ON' if goblin.settings.get('minimal_mode') else 'OFF'})")
        print("4. Developer Mode 🔒")
        print("5. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            run_inventory(goblin)
        
        elif choice == "2":
            new_name = input("Enter new name: ")
            if new_name:
                goblin.name = new_name
                print(f"Renamed to {new_name}!")
                save_state(goblin.to_dict())
                time.sleep(1)
                
        elif choice == "3":
            goblin.settings['minimal_mode'] = not goblin.settings.get('minimal_mode', False)
            print(f"Minimalist Mode set to: {goblin.settings['minimal_mode']}")
            save_state(goblin.to_dict())
            time.sleep(1)
            
        elif choice == "4":
            pwd = getpass.getpass("Enter Developer Password: ")
            if pwd == "GobbyDev":
                while True:
                    print("\n--- 🔧 Developer Submenu ---")
                    print("1. Set Hunger")
                    print("2. Set Health")
                    print("3. Set Energy")
                    print("4. Time Travel")
                    print("5. Kill Gobby 💀")
                    print("6. Reset Gobby (Revive) 🩹")
                    print("7. Back")
                    
                    dev_choice = input("Dev Action: ")
                    if dev_choice == "1":
                        try:
                            val = float(input("New Hunger (0-100): "))
                            goblin.hunger = max(0, min(100, val))
                            print("Updated.")
                        except ValueError: print("Invalid number.")
                    elif dev_choice == "2":
                        try:
                            val = float(input("New Health (0-100): "))
                            goblin.health = max(0, min(100, val))
                            print("Updated.")
                        except ValueError: print("Invalid number.")
                    elif dev_choice == "3":
                        try:
                            val = float(input("New Energy (0-100): "))
                            goblin.energy = max(0, min(100, val))
                            print("Updated.")
                        except ValueError: print("Invalid number.")
                    elif dev_choice == "4":
                        try:
                            val = float(input("Hours to jump (can be negative): "))
                            goblin.last_update -= (val * 3600)
                            print(f"Traveled {val} hours.")
                        except ValueError: print("Invalid number.")
                    elif dev_choice == "5":
                        confirm = input(f"Are you sure you want to kill {goblin.name}? (y/N): ")
                        if confirm.lower() == 'y':
                            goblin.health = 0
                            goblin.hunger = 100
                            goblin.energy = 0
                            goblin.update_mood_string() # This will set mood to "dead"
                            print(f"{goblin.name} has perished.")
                    elif dev_choice == "6":
                        confirm = input(f"Are you sure you want to reset {goblin.name}? (y/N): ")
                        if confirm.lower() == 'y':
                            goblin.hunger = 50
                            goblin.mood = "happy"
                            goblin.mood_value = 100
                            goblin.energy = 100
                            goblin.health = 100
                            goblin.bond = 0
                            goblin.last_update = time.time()
                            goblin.care_score = 0
                            print(f"{goblin.name} has been revived and reset!")
                    elif dev_choice == "7":
                        break
                    
                    goblin.update_mood_string()
                    save_state(goblin.to_dict())
            else:
                print("Access Denied.")
                time.sleep(1)
                
        elif choice == "5":
            break

def live_watch(goblin):
    try:
        frames = [IDLE, EXCITED, IDLE, WATCHING]
        if goblin.mood == "feral":
            frames = [ANGRY, IDLE, ANGRY]
        elif goblin.mood == "bored":
            frames = [SLEEPING, SLEEPING, IDLE]
            
        while True:
            for frame in frames:
                os.system('clear' if os.name == 'posix' else 'cls')
                print(frame)
                print(f"--- {goblin.name} is watching ---")
                print("Press Ctrl+C to stop watching.")
                time.sleep(1)
                goblin.update()
                save_state(goblin.to_dict())
    except KeyboardInterrupt:
        print("\nStopping watch mode...")
