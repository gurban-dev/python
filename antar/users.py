import string

users_db = {
  # admin username and password
  "adm": "1",
  # guest username and password
  "guest": "guest"
}

def sign_in():
  print("Hello! How is your day today?")

  user = input("Login:\n")
  password = input("Password:\n")
  
  # Check if the user exists in the database
  # and that the password matches.
  if user in users_db and users_db[user] == password:
    print(f"Access granted! Hello back, {user}!")
    return user  # Return the username of the signed-in user
  else:
    print("Authorization denied. Please check your credentials.")
    return None  # Return None for failed authentication

'''
Remember that each function should honour the
single responsibility principle which states
that each function should handle one task.'''
def sign_up():
  print("Hello! New here? Join now!")

  user = input("Name:\t")
  
  # Check if the username already exists.
  if user in users_db:
    print("This username is already taken. Please choose a different one.")
    return
  
  password = input("Password:\t")
  
  # Check for special characters in the username.
  special_characters = (
    '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '_', '=', '+',
    '{', '}', '[', ']', '|', ':', ';',
    '"', "'", '<', '>', ',', '.', '?', '/')
  
  for letter in user:
    if letter in string.punctuation:
      print(f"The name should not contain any of the"
          f"following special characters:"
          f"\n{special_characters}")
      return

  # for letter in special_characters:
  #   if letter in user:
  #     print(f"The name should not contain any of the"
  #           f"following special characters:"
  #           f"\n{special_characters}")
  #     return  # Exit the function if a special character is found
  
  # Add the new user to the database
  users_db[user] = password

  print("Welcome! Your account has been created.")

def greeting():
  while True:
      print('''
Hello and welcome to the website!
1. Sign in
2. Sign up
3. Exit
''')
      choice = input("Please choose an option (1, 2, or 3): ")
      
      if choice == '1':
          user_type = sign_in()
          if user_type:
              while True:
                  action = input("Do you want to sign out? (yes/no): ").strip().lower()
                  if action == 'yes':
                      print("You have signed out.")
                      break  # Exit the inner loop to go back to the main menu
                  elif action == 'no':
                      print("You are still signed in. Let's read what the A.I. has to say about cats!",end='\n')
                      print('''
Cats, scientifically known as Felis catus, are small,
agile mammals that have captivated human hearts for thousands of years. 
With their graceful movements and keen senses, they are natural hunters, 
originally domesticated for their ability to control rodent populations in 
agricultural settings. Cats possess a unique blend of independence and affection, 
often displaying a range of behaviors that endear them to their owners. They are 
known for their playful antics, which can include chasing after toys, pouncing on 
imaginary prey, or engaging in spirited play with their human companions. This playful
nature is complemented by their curious disposition; cats are often seen exploring their 
surroundings, investigating every nook and cranny of their environment.
One of the most fascinating aspects of cats is their communication style. They 
use a variety of vocalizations, including purring, meowing, and hissing, to express 
their feelings and needs. Purring is often associated with contentment, while meowing is 
a way for cats to communicate specifically with humans, as they rarely meow at each other. Additionally,
cats communicate through body language, using their tails, ears, and whiskers to convey emotions. A raised tail can 
indicate happiness, while flattened ears may signal fear or aggression.
Cats are also known for their grooming habits, spending a significant portion of their day cleaning 
their fur. This behavior not only helps them maintain hygiene but also serves to regulate their body 
temperature and strengthen social bonds with other cats. Their retractable claws are a remarkable adaptation, 
allowing them to climb, hunt, and defend themselves effectively. The variety of breeds, from the sleek Siamese 
to the fluffy Maine Coon, showcases the incredible diversity within the species, each with its own unique personality 
traits and physical characteristics.
In terms of companionship, cats have a special way of forming bonds with their human caregivers. 
They often seek out attention and affection, curling up in laps or following their owners from room to 
room. This companionship can have numerous benefits for humans, including reduced stress and increased 
feelings of happiness. Studies have shown that interacting with cats can lower blood pressure and promote a 
sense of well-being, making them not just pets but also valuable emotional support animals.
Despite their independent nature, many cats thrive on routine and can be quite sensitive to changes in 
their environment. They often establish a territory and may become attached to specific spots in the home, 
such as sunny windowsills or cozy blankets. Understanding a cat's behavior and preferences can enhance the human-animal 
bond, leading to a fulfilling relationship that enriches the lives of both parties.
In conclusion, cats are complex creatures that embody a blend of independence, playfulness, and affection. 
Their unique behaviors, communication styles, and adaptability make them fascinating companions. Whether they are 
perched on a windowsill, playfully batting at a feather toy, or curling up beside their owners, cats have a special way
of bringing joy and companionship into our lives, making them one of the most beloved pets around the world.
''')
                  else:
                      print("Please enter 'yes' or 'no'.")
      
      elif choice == '2':
          sign_up()
      
      elif choice == '3':
          print("Exiting the program. Goodbye!")
          break  # Exit the main loop
      
      else:
          print("Please choose a valid option!")

# Start the program
greeting()