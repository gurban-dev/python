import requests

# A pure function is one whose output will always be the
# same when given the same input.

# It just accepts data and return the data.

# This means that the function doesnt't:
# Modify global variables.
# Write to files.
# Call APIs
# Affect the external state.

def normalise_ip(ip):
    return ip.strip().lower()

# If the normalise_ip() function is invoked 1 000 times,
# it'll always return "8.8.8.8". Nothing else occurs.
print('normalise_ip(\" 8.8.8.8 \"):', normalise_ip(" 8.8.8.8 "))

# A side-effect function has side-effects if it changes
# something outside of itself.

# Examples:
# API calls
# Writing to a database
# Logging
# Changing global state

# The following is not a pure functon because:
# Network state can change
# API responses change
# It depends on external systems

# The same input doesn't always guarantee the same output.
def query_virustotal(ip):
    response = requests.get(f"https://api.ipify.org?format=json&ip={ip}")

    return response.json()

print('\nquery_virustotal(\"8.8.8.8\"):', query_virustotal("8.8.8.8"))

'''
For an IOC tool, the architecture should look like:
Pure Layer (Core logic)
IOC parsing
Validation

Side Effect Layer (Edges of the System)
API calls
File storage
Database writes
'''