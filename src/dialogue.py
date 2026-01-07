import random
import datetime
import time

def get_dialogue(goblin):
    mood = goblin.mood
    name = goblin.name
    user = goblin.username
    now = datetime.datetime.now()
    
    # Priority: Dead
    if mood == "dead":
        dead_dialogues = [
            "...",
            "System offline.",
            "Rest in pieces.",
            f"{name} is gone. You're alone now."
        ]
        return random.choice(dead_dialogues)

    dialogues = []
    
    # Time based
    if now.hour < 5:
        dialogues.append(f"It's late, {user}. Why are we still awake?")
    elif now.hour < 12:
        dialogues.append(f"Morning, {user}. I hope you've had coffee.")
    elif now.hour > 20:
        dialogues.append(f"Getting late. Don't forget to push your code.")

    # Last command based
    if goblin.last_command:
        if "git" in goblin.last_command:
            dialogues.append(f"You always run {goblin.last_command} when you're stressed.")
        elif "rm" in goblin.last_command:
            dialogues.append(f"Careful with that {goblin.last_command}. I live here too!")
        else:
            dialogues.append(f"I saw you run '{goblin.last_command}'. Interesting choice.")

    # Care based
    if goblin.care_score > 50:
        dialogues.append(f"You're actually pretty nice, {user}. For a human.")
    elif goblin.care_score < -10:
        dialogues.append(f"I'm starting to think you're trying to see how long I can last without food.")

    # Neglect based (Passive-aggressive)
    if goblin.hunger > 70 or goblin.health < 50:
        passive_aggressive = [
            "Oh, don't mind me. I'm just starving to death in this directory.",
            "I'd ask for food, but I know how 'busy' you are with your git status.",
            "Is this how you treat all your processes? Or just the ones that care?",
            "I've been calculating the heat death of the universe while waiting for you.",
            "Maybe if I was a VS Code extension you'd pay more attention to me."
        ]
        if random.random() < 0.6:
            return random.choice(passive_aggressive)

    # Prioritize reactive dialogues if they exist
    if dialogues and random.random() < 0.7:
        return random.choice(dialogues)

    # Mood based
    mood_dialogues = {
        "happy": [
            "I'm just watching the cursor blink. It's hypnotic.",
            "You're doing great. I think."
        ],
        "bored": [
            "*yawn* Is there anything interesting happening?",
            "I was almost asleep."
        ],
        "anxious": [
            "Are we okay? You seem to be typing fast.",
            "I'm watching you. Just so you know."
        ],
        "feral": [
            "FEED ME OR I EAT THE BASH HISTORY.",
            "*hisses at the prompt*"
        ],
        "sick": [
            "I don't feel so good...",
            "*coughs in binary*"
        ]
    }
        
    return random.choice(mood_dialogues.get(mood, ["..."]))
