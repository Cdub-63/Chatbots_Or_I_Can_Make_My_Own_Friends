#TODO: what about a back option for the menu?

import time
import sys

# Define functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  time.sleep(2)
  print(f"\nAlright, that's a {size} {drink_type}!\n")
  time.sleep(2)
  name = input("Can I get your name please?\n> ")
  time.sleep(2)
  print(f"\nThanks, {name.capitalize()}! Your drink will be ready shortly.")
  
def print_message():
  print("\nI'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.\n")

def quit():
  print("It's good to lay off the caffeine for awhile!")
  sys.exit(0)

def get_drink_type():
  res = None
  while res is None:
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n[q] Quit \n> ')
    if res == "a":
      res = "brewed coffee"
    elif res == "b":
      res = "mocha"
    elif res == "c":
      res = order_latte()
    elif res == "q":
      quit()
    else:
      print_message()
      time.sleep(2)
      return get_drink_type()
  return res

def order_latte():
  res = None
  while res is None:
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n[q] Quit \n> ')
    if res == "a":
      res = "latte"
    elif res == "b":
      res = "non-fat latte"
    elif res == "c":
      res = "soy latte"
    elif res == "q":
      quit()
    else:
      print_message()
      time.sleep(2)
      return order_latte()
  return res

def get_size():
  res = None
  selected_coffee_size = True
  while res is None:
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n[q] Quit \n> ')
    if res == "a":
      res = "small"
    elif res == "b":
      res = "medium"
    elif res == "c":
      res = "large"
    elif res == "q":
      quit()
    else:
      print_message()
      time.sleep(2)
      return get_size()
  return res

# Call coffee_bot()!
coffee_bot()
