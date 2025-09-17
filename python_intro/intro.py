import pyttsx3


engine = pyttsx3.init()
# use the input function which returns a string to get the user's name and say hello to them
name = input("Please enter your name: ")
engine.say(f"hello {name}")
engine.runAndWait()
