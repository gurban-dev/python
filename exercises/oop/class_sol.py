class Fish:
  # Class variable: shared by all fish
  # It describes general characteristics of each species
  species_data = {
    "Goldfish": {"aggressiveness": 1, "survival_rate": 0.95},
    "Betta": {"aggressiveness": 8, "survival_rate": 0.85},
    "Guppy": {"aggressiveness": 2, "survival_rate": 0.9},
    "Angelfish": {"aggressiveness": 5, "survival_rate": 0.88},
    "Tetra": {"aggressiveness": 3, "survival_rate": 0.92}
  }

  def __init__(self, name, species, age):
    # Instance variables: unique to each fish
    self.name: str = name
    self.species: str = species
    self.age: int = age
  
  # Selector/getter because it simply returns an
  # instance variable that belongs to some instance
  # of this class.
  def get_fish_name(self):
    return self.name

  def get_fish_species(self):
    return self.species

  def can_live_with(self, other_fish):
    """
    Determines whether two fish can live together.
    Rule:
    - If both have aggressiveness <= 4 → compatible
    - Otherwise, not compatible

    E.g.
    goldfish = Fish("Sunny", "Goldfish", 1)
    betta = Fish("Blue", "Betta", 2)

    goldfish.can_live_with(betta)

    self.species in this example, will be "Goldfish".
    """
    my_aggr: int = Fish.species_data[self.species]["aggressiveness"]

    other_aggr: int = Fish.species_data[other_fish.species]["aggressiveness"]

    # The "and" keyword is a logical operator that returns
    # True only if conditions on both its sides are True.
    if my_aggr <= 4 and other_aggr <= 4:
      return True
    else:
      return False

  def compatibility_score(self, other_fish) -> float:
    """
    Returns a number between 0 and 1 representing compatibility.
    A higher score means more likely to live together.
    """
    my_aggr: int = Fish.species_data[self.species]["aggressiveness"]
    other_aggr: int = Fish.species_data[other_fish.species]["aggressiveness"]

    # Compatibility decreases as aggressiveness difference increases
    difference: int = abs(my_aggr - other_aggr)

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

# Show the available fish species.
Fish.show_available_species()

# Create objects/instances of the Fish class.
goldfish: Fish = Fish("Sunny", "Goldfish", 1)
betta: Fish = Fish("Blue", "Betta", 2)
guppy: Fish = Fish("Flash", "Guppy", 1)
angel_fish: Fish = Fish("Angel", "Angelfish", 3)
tetra: Fish = Fish("Tiny", "Tetra", 2)

# Create a list of all your fish.
fish_list: list[Fish] = [goldfish, betta, guppy, angel_fish, tetra]

print('\ngoldfish.can_live_with(betta):', goldfish.can_live_with(betta))

# Group all peaceful fish together (aggressiveness <= 4).
peaceful_fish: Fish = []
aggressive_fish: Fish = []

for fish in fish_list:
  # Obtain the aggressiveness of each fish.
  aggr: int = Fish.species_data[fish.species]["aggressiveness"]

  if aggr <= 4:
    peaceful_fish.append(fish)
  else:
    aggressive_fish.append(fish)

# Print the names of the peaceful fish.
for index, fish in enumerate(peaceful_fish):
  if index != len(peaceful_fish) - 1:
    print(fish.get_fish_name(), end=", ")
  else:
    print(fish.get_fish_name(), end='\n\n')

print("🐟 Peaceful Fish (Can live together):")
for fish in peaceful_fish:
  # peaceful_fish references a list of Fish objects.

  print(f" - {fish.get_fish_name()} ({fish.get_fish_species()}, "
        f"aggressiveness="
        f"{Fish.species_data[fish.get_fish_species()]['aggressiveness']})")

print("\n🐠 Aggressive Fish (Separate tank recommended):")
for fish in aggressive_fish:
  print(f" - {fish.name} ({fish.species}, "
        f"aggressiveness="
        f"{Fish.species_data[fish.get_fish_species()]['aggressiveness']})")