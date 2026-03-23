import random

# A dictionary of all 195 UN-recognized countries and their
# capitals.
COUNTRIES = {
	"Afghanistan": "Kabul",
	"Albania": "Tirana",
	"Algeria": "Algiers",
	"Andorra": "Andorra la Vella",
	"Angola": "Luanda",
	"Antigua and Barbuda": "Saint John's",
	"Argentina": "Buenos Aires",
	"Armenia": "Yerevan",
	"Australia": "Canberra",
	"Austria": "Vienna",
	"Azerbaijan": "Baku",
	"Bahamas": "Nassau",
	"Bahrain": "Manama",
	"Bangladesh": "Dhaka",
	"Barbados": "Bridgetown",
	"Belarus": "Minsk",
	"Belgium": "Brussels",
	"Belize": "Belmopan",
	"Benin": "Porto-Novo",
	"Bhutan": "Thimphu",
	"Bolivia": "Sucre",
	"Bosnia and Herzegovina": "Sarajevo",
	"Botswana": "Gaborone",
	"Brazil": "Brasília",
	"Brunei": "Bandar Seri Begawan",
	"Bulgaria": "Sofia",
	"Burkina Faso": "Ouagadougou",
	"Burundi": "Gitega",
	"Cabo Verde": "Praia",
	"Cambodia": "Phnom Penh",
	"Cameroon": "Yaoundé",
	"Canada": "Ottawa",
	"Central African Republic": "Bangui",
	"Chad": "N'Djamena",
	"Chile": "Santiago",
	"China": "Beijing",
	"Colombia": "Bogotá",
	"Comoros": "Moroni",
	"Republic of the Congo": "Brazzaville",
	"Costa Rica": "San José",
	"Croatia": "Zagreb",
	"Cuba": "Havana",
	"Cyprus": "Nicosia",
	"Czechia": "Prague",
	"Democratic Republic of the Congo": "Kinshasa",
	"Denmark": "Copenhagen",
	"Djibouti": "Djibouti",
	"Dominica": "Roseau",
	"Dominican Republic": "Santo Domingo",
	"Ecuador": "Quito",
	"Egypt": "Cairo",
	"El Salvador": "San Salvador",
	"Equatorial Guinea": "Malabo",
	"Eritrea": "Asmara",
	"Estonia": "Tallinn",
	"Eswatini": "Mbabane",
	"Ethiopia": "Addis Ababa",
	"Fiji": "Suva",
	"Finland": "Helsinki",
	"France": "Paris",
	"Gabon": "Libreville",
	"Gambia": "Banjul",
	"Georgia": "Tbilisi",
	"Germany": "Berlin",
	"Ghana": "Accra",
	"Greece": "Athens",
	"Grenada": "Saint George's",
	"Guatemala": "Guatemala City",
	"Guinea": "Conakry",
	"Guinea-Bissau": "Bissau",
	"Guyana": "Georgetown",
	"Haiti": "Port-au-Prince",
	"Honduras": "Tegucigalpa",
	"Hungary": "Budapest",
	"Iceland": "Reykjavik",
	"India": "New Delhi",
	"Indonesia": "Jakarta",
	"Iran": "Tehran",
	"Iraq": "Baghdad",
	"Ireland": "Dublin",
	"Israel": "Jerusalem",
	"Italy": "Rome",
	"Jamaica": "Kingston",
	"Japan": "Tokyo",
	"Jordan": "Amman",
	"Kazakhstan": "Astana",
	"Kenya": "Nairobi",
	"Kiribati": "Tarawa",
	"Kuwait": "Kuwait City",
	"Kyrgyzstan": "Bishkek",
	"Laos": "Vientiane",
	"Latvia": "Riga",
	"Lebanon": "Beirut",
	"Lesotho": "Maseru",
	"Liberia": "Monrovia",
	"Libya": "Tripoli",
	"Liechtenstein": "Vaduz",
	"Lithuania": "Vilnius",
	"Luxembourg": "Luxembourg",
	"Madagascar": "Antananarivo",
	"Malawi": "Lilongwe",
	"Malaysia": "Kuala Lumpur",
	"Maldives": "Malé",
	"Mali": "Bamako",
	"Malta": "Valletta",
	"Marshall Islands": "Majuro",
	"Mauritania": "Nouakchott",
	"Mauritius": "Port Louis",
	"Mexico": "Mexico City",
	"Micronesia": "Palikir",
	"Moldova": "Chișinău",
	"Monaco": "Monaco",
	"Mongolia": "Ulaanbaatar",
	"Montenegro": "Podgorica",
	"Morocco": "Rabat",
	"Mozambique": "Maputo",
	"Myanmar": "Naypyidaw",
	"Namibia": "Windhoek",
	"Nauru": "Yaren",
	"Nepal": "Kathmandu",
	"Netherlands": "Amsterdam",
	"New Zealand": "Wellington",
	"Nicaragua": "Managua",
	"Niger": "Niamey",
	"Nigeria": "Abuja",
	"North Korea": "Pyongyang",
	"North Macedonia": "Skopje",
	"Norway": "Oslo",
	"Oman": "Muscat",
	"Pakistan": "Islamabad",
	"Palau": "Ngerulmud",
	"Palestine": "Ramallah",
	"Panama": "Panama City",
	"Papua New Guinea": "Port Moresby",
	"Paraguay": "Asunción",
	"Peru": "Lima",
	"Philippines": "Manila",
	"Poland": "Warsaw",
	"Portugal": "Lisbon",
	"Qatar": "Doha",
	"Romania": "Bucharest",
	"Russia": "Moscow",
	"Rwanda": "Kigali",
	"Saint Kitts and Nevis": "Basseterre",
	"Saint Lucia": "Castries",
	"Saint Vincent and the Grenadines": "Kingstown",
	"Samoa": "Apia",
	"San Marino": "San Marino",
	"Sao Tome and Principe": "São Tomé",
	"Saudi Arabia": "Riyadh",
	"Senegal": "Dakar",
	"Serbia": "Belgrade",
	"Seychelles": "Victoria",
	"Sierra Leone": "Freetown",
	"Singapore": "Singapore",
	"Slovakia": "Bratislava",
	"Slovenia": "Ljubljana",
	"Solomon Islands": "Honiara",
	"Somalia": "Mogadishu",
	"South Africa": "Pretoria",
	"South Korea": "Seoul",
	"South Sudan": "Juba",
	"Spain": "Madrid",
	"Sri Lanka": "Sri Jayawardenepura Kotte",
	"Sudan": "Khartoum",
	"Suriname": "Paramaribo",
	"Sweden": "Stockholm",
	"Switzerland": "Bern",
	"Syria": "Damascus",
	"Tajikistan": "Dushanbe",
	"Tanzania": "Dodoma",
	"Thailand": "Bangkok",
	"Timor-Leste": "Dili",
	"Togo": "Lomé",
	"Tonga": "Nuku'alofa",
	"Trinidad and Tobago": "Port of Spain",
	"Tunisia": "Tunis",
	"Turkey": "Ankara",
	"Turkmenistan": "Ashgabat",
	"Tuvalu": "Funafuti",
	"Uganda": "Kampala",
	"Ukraine": "Kyiv",
	"United Arab Emirates": "Abu Dhabi",
	"United Kingdom": "London",
	"United States": "Washington, D.C.",
	"Uruguay": "Montevideo",
	"Uzbekistan": "Tashkent",
	"Vanuatu": "Port Vila",
	"Vatican City": "Vatican City",
	"Venezuela": "Caracas",
	"Vietnam": "Hanoi",
	"Yemen": "Sana'a",
	"Zambia": "Lusaka",
	"Zimbabwe": "Harare"
}

print('COUNTRIES["Tunisia"]', COUNTRIES["Tunisia"])

def normalize_answer(answer):
	"""Normalize answer for comparison"""
	return answer.lower().strip().replace("'", "'")

def run_quiz():
	"""Main quiz function"""
	print("=" * 60)
	print("WORLD CAPITALS QUIZ - 195 UN Member States")
	print("=" * 60)
	print("\nTest your knowledge of world capitals!")
	print("Type 'quit' at any time to exit.\n")
  
	# Get quiz mode
	while True:
		print("Choose quiz mode:")
		print("1. All countries (195 questions)")
		print("2. Random sample (specify number)")

		mode = input("\nEnter your choice (1 or 2): ").strip()
		
		if mode == "1":
			countries_list = list(COUNTRIES.items())
			break
		elif mode == "2":
			try:
				num = int(input("How many questions? (1-195): "))

				if 1 <= num <= 195:
					countries_list = random.sample(list(COUNTRIES.items()), num)
					break
				else:
					print("Please enter a number between 1 and 195.")
			except ValueError:
				print("Invalid input. Please enter a number.")
		else:
			print("Invalid choice. Please enter 1 or 2.")
	
	# Shuffle questions
	random.shuffle(countries_list)
	
	score = 0
	total = len(countries_list)
	
	print(f"\n{'=' * 60}")
	print(f"Starting quiz with {total} questions!")
	print(f"{'=' * 60}\n")

	for i, (country, capital) in enumerate(countries_list, 1):
		print(f"Question {i}/{total}")
		print(f"What is the capital of {country}?")

		user_answer = input("Your answer: ").strip()
		
		if user_answer.lower() == 'quit':
			print(f"\nQuiz ended early. Final score: {score}/{i-1}")
			return
		
		if normalize_answer(user_answer) == normalize_answer(capital):
			print("✓ Correct!\n")
			score += 1
		else:
			print(f"✗ Incorrect. The correct answer is: {capital}\n")
  
	# Final results
	percentage = (score / total) * 100

	print("=" * 60)
	print("QUIZ COMPLETED!")
	print("=" * 60)
	print(f"Final Score: {score}/{total} ({percentage:.1f}%)")
	
	if percentage == 100:
		print("Perfect score! You're a geography master! 🌍")
	elif percentage >= 90:
		print("Excellent work! You know your capitals! 🎉")
	elif percentage >= 75:
		print("Great job! Very impressive knowledge! 👏")
	elif percentage >= 60:
		print("Good effort! Keep studying! 📚")
	else:
		print("Keep practicing! You'll improve with time! 💪")
	print("=" * 60)

run_quiz()