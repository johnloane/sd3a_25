import pyttsx3
import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import speech_recognition
import os
import qrcode


def main():
    test_list()
    


def greet_user():
    engine = pyttsx3.init()
    # use the input function which returns a string to get the user's name and say hello to them
    name = input("Please enter your name: ")
    engine.say(f"hello {name}")
    engine.runAndWait()
    

def python_types():
    # string, int, float, bool
    number = 1000000000000
    print(number)
    one_over_three = 1/3
    print(f"{one_over_three:.50}")
    
    
def calculator():
    x = get_int()
    y = get_int()
    print(x+y)
    
    
def get_int():
    while True:
        try:
            x = int(input("Enter int: "))
            break
        except ValueError:
            print("Not an integer")
    return x


def find_faces(image):
    image_to_search = face_recognition.load_image_file(image)
    face_locations = face_recognition.face_locations(image_to_search)
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image_to_search[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()
        
        
def find_christopher(image_of_chris, group_image):
    christopher = face_recognition.load_image_file(image_of_chris)
    chris_encoding = face_recognition.face_encodings(christopher)[0]
    # Load the image with the unknown faces
    sd3a_class = face_recognition.load_image_file(group_image)
    # Find all faces and face_encodings in sd3a
    face_locations = face_recognition.face_locations(sd3a_class)
    face_encodings = face_recognition.face_encodings(sd3a_class, face_locations)
    pil_image = Image.open(group_image)
    draw = ImageDraw.Draw(pil_image)
    for (top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces([chris_encoding], face_encodings)
        face_distances = face_recognition.face_distance([chris_encoding], face_encodings)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            draw.rectangle(((left - 20, top - 20), (right+ 20, bottom+20)), outline=(0, 255, 0), width=10)
            
    del draw
    pil_image.show()
    
    
def recognise_speech():
    recogniser = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Say something")
        audio = recogniser.listen(source)
        print("You said: ")
        print(recogniser.recognize_google(audio))
    
    
def create_qrcode():
    img = qrcode.make("https://github.com/johnloane/sd3a_25")
    img.save("qr.png", "PNG")
    
        
def add_two_integers():
    x = get_integer()
    y = get_integer()
    print(int(x+y))
    
    
def get_integer():
    while True:
        try:
            x = int(input("Please enter an integer: "))
            break
        except ValueError:
            print("Not an integer, please try again")
    return x


# Types int, str, bool, float, list, dict, set, tuple, NoneType
   
   
def test_mutable():
    grocery_list = ["Milk", "Bananas", "Bread", "Monster"]
    print(grocery_list)
    grocery_list[3] = "Red Bull"
    print(grocery_list)
    
    
def test_immutable():
    misspelled_vegetable = "Cawrots"
    misspelled_vegetable = "Carrot"
    print(misspelled_vegetable)
    
    
def test_list():
    sd3a_names = ["Iker", "Sofia", "Ikram"]
    print(len(sd3a_names))
    print(max(sd3a_names))
  

if __name__ == "__main__":
    main()

