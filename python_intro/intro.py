import pyttsx3
import face_recognition
from PIL import Image


def main():
    find_faces("iut_lens.jpg")


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
  

if __name__ == "__main__":
    main()

