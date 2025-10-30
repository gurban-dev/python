class Fish:
  # Class variable: shared by all fish
  # It describes general characteristics of each species
  species_data = {
    "Goldfish": {"aggressiveness": 1, "survival_rate": 0.95},
    "Betta": {"aggressiveness": 8, "survival_rate": 0.85},
    "Guppy": {"aggressiveness": 2, "survival_rate": 0.9},
    "Angelfish": {"aggressiveness": 5, "survival_rate": 0.88},
    "Tetra": {"aggressiveness": 3, "survival_rate": 0.92},
  }

  def __init__(self, name, species, age):
    # Instance variables: unique to each fish
    self.name = name
    self.species = species
    self.age = age

  def can_live_with(self, other_fish):
    """
    Determines whether two fish can live together.
    Rule:
    - If both have aggressiveness ≤ 4 → compatible
    - Otherwise, not compatible
    """
    my_aggr = Fish.species_data[self.species]["aggressiveness"]
    other_aggr = Fish.species_data[other_fish.species]["aggressiveness"]

    if my_aggr <= 4 and other_aggr <= 4:
        return True
    return False

  def compatibility_score(self, other_fish):
    """
    Returns a number between 0 and 1 representing compatibility.
    A higher score means more likely to live together.
    """
    my_aggr = Fish.species_data[self.species]["aggressiveness"]
    other_aggr = Fish.species_data[other_fish.species]["aggressiveness"]

    # Compatibility decreases as aggressiveness difference increases
    difference = abs(my_aggr - other_aggr)

    # simple linear scale
    return max(0, 1 - (difference / 10))

  @classmethod
  def show_available_species(cls):
    """Displays all fish species stored in the class variable."""
    print("Available fish species:")
    for species, data in cls.species_data.items():
      print(f" - {species}: aggressiveness={data['aggressiveness']}, survival={data['survival_rate']}")

  def __str__(self):
    """Readable string for printing each fish."""
    return f"{self.name} ({self.species}, age {self.age})"

# Show available fish
Fish.show_available_species()
print("\n")

# Create individual fish (instance variables)
f1 = Fish("Sunny", "Goldfish", 1)
f2 = Fish("Blue", "Betta", 2)
f3 = Fish("Flash", "Guppy", 1)
f4 = Fish("Angel", "Angelfish", 3)
f5 = Fish("Tiny", "Tetra", 2)

# Group all peaceful fish (aggressiveness <= 4)
peaceful_fish = []
aggressive_fish = []

# Create a list of all your fish
fish_list = [f1, f2, f3, f4, f5]

for fish in fish_list:
  aggr = Fish.species_data[fish.species]["aggressiveness"]

  if aggr <= 4:
    peaceful_fish.append(fish)
  else:
    aggressive_fish.append(fish)

print("🐟 Peaceful Fish (Can live together):")
for f in peaceful_fish:
  print(f" - {f.name} ({f.species}, aggressiveness={Fish.species_data[f.species]['aggressiveness']})")

print("\n🐠 Aggressive Fish (Separate tank recommended):")
for f in aggressive_fish:
  print(f" - {f.name} ({f.species}, aggressiveness={Fish.species_data[f.species]['aggressiveness']})")