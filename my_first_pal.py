import time
import re

print("Hello, welcome to my first chatbot.\n")
time.sleep(2)
print("This chat bot will repeat exactly what you say.\n")
time.sleep(2)

stuff_to_echo = None
while stuff_to_echo is None:
    stuff_to_echo = input("Well, say something! \n # ")
    search = re.search(r'^[a-zA-Z]+$', stuff_to_echo)
    if search is not None:
      print('You said: {}'.format(stuff_to_echo))
      break
    else:
      print("Please say a coherent sentence! \n")
      stuff_to_echo = None
