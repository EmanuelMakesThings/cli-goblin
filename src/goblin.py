import time
import random
from .creatures import get_random_creature

class Goblin:
    def __init__(self, name="Gobby", state=None):
        self.name = name
        if state:
            self.hunger = state.get("hunger", 50)
            self.mood = state.get("mood", "happy")
            self.mood_value = state.get("mood_value", 100)
            self.energy = state.get("energy", 100)
            self.health = state.get("health", 100)
            self.bond = state.get("bond", 0)
            self.last_update = state.get("last_update", time.time())
            self.username = state.get("username", "User")
            self.birth_date = state.get("birth_date", time.time())
            self.last_command = state.get("last_command", None)
            self.interaction_count = state.get("interaction_count", 0)
            self.care_score = state.get("care_score", 0)
            self.settings = state.get("settings", {"minimal_mode": False})
            self.collection = state.get("collection", [])
        else:
            self.hunger = 50
            self.mood = "happy"
            self.mood_value = 100
            self.energy = 100
            self.health = 100
            self.bond = 0
            self.last_update = time.time()
            self.username = "User"
            self.birth_date = time.time()
            self.last_command = None
            self.interaction_count = 0
            self.care_score = 0
            self.settings = {"minimal_mode": False}
            self.collection = []

    def update(self, command_watched=None):
        if self.health <= 0:
            self.mood = "dead"
            return # No decay for the dead
            
        now = time.time()
        elapsed = now - self.last_update
        self.interaction_count += 1
        if command_watched:
            self.last_command = command_watched
        
        # Decay rates (per hour)
        hunger_decay = 10
        mood_decay = 5
        energy_decay = 2
        
        hours_passed = elapsed / 3600
        
        self.hunger = min(100, self.hunger + (hunger_decay * hours_passed))
        self.mood_value = max(0, self.mood_value - (mood_decay * hours_passed))
        
        # If hunger is high, health drops
        if self.hunger > 80:
            health_drop = (self.hunger - 80) * 0.5 * hours_passed
            self.health = max(0, self.health - health_drop)
            self.care_score -= 1 * hours_passed
        
        self.update_mood_string()
        self.last_update = now

    def update_mood_string(self):
        if self.health <= 0:
            self.mood = "dead"
        elif self.health < 10:
            self.mood = "corrupted"
        elif self.health < 40:
            self.mood = "sick"
        elif self.hunger > 80:
            self.mood = "feral"
        elif self.mood_value < 30:
            self.mood = "bored"
        elif self.mood_value < 60:
            self.mood = "anxious"
        else:
            self.mood = "happy"

    def feed(self):
        amount = random.randint(20, 40)
        self.hunger = max(0, self.hunger - amount)
        self.bond += 1
        self.care_score += 5
        self.mood_value = min(100, self.mood_value + 5)
        return f"You fed {self.name}. It looks a bit less hungry."

    def play(self):
        if self.energy < 20:
            return f"{self.name} is too tired to play."
        self.energy -= 20
        self.mood_value = min(100, self.mood_value + 30)
        self.bond += 2
        self.care_score += 10
        return f"You played with {self.name}! It's happier now."

    def hunt(self):
        if self.energy < 30:
            return None, f"{self.name} is too tired to hunt. (Needs 30 Energy)"
        
        self.energy -= 30
        self.hunger = min(100, self.hunger + 10) # Hunting makes you hungry
        
        if random.random() < 0.3: # 30% chance to fail
            return None, f"{self.name} sniffed around but found nothing."
            
        creature = get_random_creature()
        
        # Check if already caught
        if any(c['name'] == creature['name'] for c in self.collection):
            return creature, f"{self.name} found another {creature['name']}! (Already in collection)"
        
        self.collection.append(creature)
        return creature, f"{self.name} caught a {creature['name']}! ({creature['rarity']})"

    def to_dict(self):
        return {
            "name": self.name,
            "hunger": self.hunger,
            "mood": self.mood,
            "mood_value": self.mood_value,
            "energy": self.energy,
            "health": self.health,
            "bond": self.bond,
            "last_update": self.last_update,
            "username": self.username,
            "birth_date": self.birth_date,
            "last_command": self.last_command,
            "interaction_count": self.interaction_count,
            "care_score": self.care_score,
            "settings": self.settings,
            "collection": self.collection
        }
