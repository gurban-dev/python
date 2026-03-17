# Shell utilities
import shutil as su

# Copy the philosophers.txt file.
source_file = './philosophers.txt'
destination = './philosophers_copy.txt'

su.copy(source_file, destination)

print(source_file, 'file copied successfully.')