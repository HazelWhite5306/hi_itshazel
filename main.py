import random

def bot_responses(user_input):
  responses = [
    "thats so cool!",
    "I agree.",
    "OMG me too!",
    "Really!?",
    "I love that for you."
  ]
  return random.choice(responses)

#Let the convo begin!

def in_chat():
  end_it = 'bye'

  user_input = input("Hello, I am Chatbot :)\n What do you want to talk about?\n (To End this Convo Please Type: bye)\n - Your Day\n - Drama/Tea\n - Your Background\n")

#If it aint dead yet then its responding time!

  if user_input == "Your Day":
    user_input = input("How was your Day?\n")
  elif user_input == "Drama/Tea":
    user_input = input("Yes! My favorite topic... well go on!")
  elif user_input == "Your Background":
    user_input = input("Cool! So, where are you from?")

    
  while user_input != end_it:

    user_input = input(bot_responses(user_input)+ "\n")

if __name__ == "__main__":
  in_chat()

  