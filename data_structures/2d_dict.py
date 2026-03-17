# Nested dictionary (2D dictionary).
species_data = {
  "Goldfish": {"aggressiveness": 1, "survival_rate": 0.95},
  "Betta": {"aggressiveness": 8, "survival_rate": 0.85},
  "Guppy": {"aggressiveness": 2, "survival_rate": 0.9},
  "Angelfish": {"aggressiveness": 5, "survival_rate": 0.88},
  "Tetra": {"aggressiveness": 3, "survival_rate": 0.92}
}

print('species_data["Goldfish"]:', species_data["Goldfish"])

# Notice that whenever you access a key in a dictionary, you
# must put square brackets around it.
print('\nspecies_data["Goldfish"]["aggressiveness"]:',
      species_data['Goldfish']['aggressiveness'])

goldfish_dict = species_data["Goldfish"]

print('\ngoldfish_dict:', goldfish_dict)

print('\ngoldfish_dict[\'aggressiveness\']:',
      goldfish_dict['aggressiveness'])

# The .items() method returns each key-value pair in the dictionary.
for key, value in species_data.items():
  print(f"\nSpecies: {key}")

  # 'value' is itself a dictionary, e.g.,
  # {"aggressiveness": 1, "survival_rate": 0.95}

  # Iterate over its key-value pairs.
  for key, value in value.items():
      print(f" - {key}: {value}")