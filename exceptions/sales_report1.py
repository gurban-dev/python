# This program displays the total of the amounts in
# the sales_data.txt file.

# Objective:
# When a Python program encounters an error, rather
# than crashing the entire program, it should handle
# the error gracefully. This is done with exception
# handling with try and except blocks.

def main():
	# Initialise an accumulator.
	total = 0

	'''
	Any source code that may generate an exception should be
	put in the try block. This way, it is caught rather than
	crashing the entire program.'''
	try:
		'''
		Open the sales_data.txt file.
		If the file that the program is attempting to open
		is not found, the program will jump to the IOError
		except clause.

		The sales_data.txt file was opened for reading and
		a file object was returned.

		./ tells Python to search for the file in the current
		directory.

		'r' passed as the second argument indicates that the
		file is being opened for reading.'''
		file_obj = open('./sales_data.txt', 'r')

		# If the sale_data.txt file was one directory
		# level above.
		# file_obj = open('./../sales_data.txt', 'r')

		# If the sale_data.txt file was one directory
		# level below.
		# file_obj = open('./sub_directory_name/sales_data.txt', 'r')

		# Read the values from each line in the file and accumulate
		# them.
		for line in file_obj:
			# The data type of "line" will be a string.

			# Remove the newline character from the end of the line.
			# The .strip() method removes any leading and trailing
			# whitespace character (spaces, newlines) from a string.
			line = line.strip()

			print(f'type({line}): {type(line)}\n')

			'''
			If the value being casted as a float, is not
			actually a numeric value, the program jumps
			from total += float(line) to the ValueError
			except clause.'''

			# If the current line doesn't exclusively contains numerals
			# skip to the next iteration in the for loop.
			# if not line.isdigit():
			# 	continue

			# total = total + float(line)
			total += float(line)

			'''
			If the program were to cast '50.00' as an integer, '50.00'
			would have to be cast as a float first before being cast
			as an integer.'''
			# total += int(float(line))

		# Close the file.
		file_obj.close()

		# Print the total.
		# Notice that "total" is a float because
		# the numeric values were casted as floats
		# above with the float() function.
		# print('\n', format(total, ',.2f'))

		# To see the following print() statement executed, remove
		# the last line from the sales_data.txt file that triggers
		# a ValueError exception.
		print('\nInside try block\ntotal:', total)
	except IOError:
		print('An error occured trying to read the file.')
	except ValueError:
		# A ValueError exception is raised when an invalid
		# value is included in a some kind of operation.
		print('Non-numeric data found in the file.')

		# "line" is possibly unbound means:
		# Python can't guarantee that line was assigned a value
		# before you try to use it.

		# 'line' might still reference the last value in the file
		# that was successfully processed so printing it out may
		# not help in debugging. 
		# print(line)
	except:
		print('An error occured.')

	# Once an exception is raised, the program will cease to
	# continue executing the remaining code in the try block.

	# Notice how the fourth line in the sales_data.txt file
	# never processed.
	print('\nOutside try block\ntotal:', total)

main()

# It's good practice to use try catch whenever data may not
# be appropriate for an operation being performed.
# E.g. Reading from a file, user input, network connections, etc.