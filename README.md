# Monster Fighter

This is my first personal project for boot.dev.
This is a turn based monster fighting game similar to pokemon.

I believe this took about 20 to 30 hours to make over the course of a week, although I wasn't timing myself.
I got to add most of the features I was planning on adding in that time. At the time of writing, I want to add more attacks, include passive abilities, and improve the printing layout a bit.
I wasn't too concerned with balancing the stats of the monsters and abilities I for the sake of time, and the damage calculation was also kept simple.

## How to play
activate virtual environment in terminal before playing:
source venv/bin/activate

Run main.py to start playing:
python3 main.py

After that, follow the prompts to choose your team and begin fighting!
The enemy will pick a random team, and pick their attacks randomly, good luck!

## Monsters 
### List of Monsters
The different monsters I intend on adding with a short description:
- Dragon (poweful monster, but slow with long cooldowns)
- Golem (Great physical defence and endurance, but slow with lackluster offense)
- Unicorn (Mythical beast with healing and buff abilities. Fast, but not too durable)
- Automaton (All-round attacker with an overdrive mode)
- Slime (Doesn't hit hard, but its large health pool regenerates)
- Phoenix (Fast and strong fire attacks. Fragile, but can revive once)

### About Stats
- HP: When a monster runs out, they die.
- Durability: Reduces damage taken from physical attacks.
- Spirit: Reduces damage taken from magic attacks.
- Speed: The monster with higher speed acts first. If speed if tied, turn order is randomized.

### About Skills
Power: The amout of damage the attack will do. Will be reduced based off the defending monster's stats.
Cooldown: The amount of turns until you can use a move again.
Pyhsical/Magic: Determines if the attack will have it's damage reduced by durability or spirit.