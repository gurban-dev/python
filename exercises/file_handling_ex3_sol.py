# Declare dictionaries to store counts.
page_visits = {}
user_visits = {}
unique_users = set()

# Read the log file.
with open("access.log", "r") as f:
	for line in f:
		# Remove leading and trailing whitespace characters.
		line = line.strip()

		if not line:
			# Skip empty lines
			continue
		
		timestamp, user_id, page = line.split(",")
		
		# Track unique users
		unique_users.add(user_id)
		
		# Count page visits
		if page not in page_visits:
			page_visits[page] = 0

		page_visits[page] += 1
		
		# Count user activity
		if user_id not in user_visits:
			user_visits[user_id] = 0

		user_visits[user_id] += 1

# Find the maximum visits for most active user(s)
max_visits = max(user_visits.values(), default=0)

most_active_users = [
    user for user, visits in user_visits.items() if visits == max_visits
]

# Print summary
print(f"Unique users: {len(unique_users)}")

print("Page visits:")
for page, count in page_visits.items():
  	print(f"  {page}: {count}")

print("Most active user(s):", ", ".join(most_active_users))