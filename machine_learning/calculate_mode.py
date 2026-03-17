# "scipy" is the name of module/library.
# The sub-package named "stats" is being
# imported from the "scipy" library.
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

mode_of_speed = stats.mode(speed)

print(mode_of_speed)