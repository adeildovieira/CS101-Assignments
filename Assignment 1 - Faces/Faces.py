"""
Created on 9/19/22

@author: Adeildo Vieira Silva Neto (av259)
"""

import random

def faces_random():
    # Print a possibly different group of 3 faces each time the program is run.
    face_random()

#Hairs
def part_hair_wavy():
    # Returns a string of a stylish hair and the divider to the face.
    a1 = r"012345678901234567"
    a2 = r" //////////////// " + "\n" #The stylish hair.
    a2 += r"+----------------+" #The divider to the face.
    return a2

def part_hair_kingy():
    # Returns the King shocked hair or his crown? I don't know.
    a1 = r"012345678901234567"
    a2 = r"    /\  /\  /\    " + "\n"
    a2 += r"    ==========    " + "\n"
    a2 += r"+----------------+"
    return a2

def part_hair_normal():
    # Returns an S hair.
    a1 = r"012345678901234567"
    a2 = r"SSSSSSSSSSSSSSSSSS" + "\n"
    a2 += r"+----------------+"
    return a2

#Eyes
def part_eye_bored():
    # Returns a string of a closed eye of a bored guy.
    a1 = r"012345678901234567"
    a2 = r"||    _    _    ||"
    return a2

def part_eye_kingsoshocked():
    # Returns a very shocked eye.
    a1 = r"012345678901234567"
    a2 = r"|  ----    ----  |" + "\n"
    a2 += r"| /    \  /    \ |" + "\n"
    a2 += r"|     o    o     |" + "\n"
    a2 += r"| \    /  \    / |" + "\n"
    a2 += r"|  ----    ----  |"
    return a2

def part_eye_normal():
    # Returns the 0.0 emoji eyes.
    a1 = r"012345678901234567"
    a2 = r"|    O      O    |"
    return a2

#Noses
def part_nose_diagonal():
    # Returns a string of the noise with double /.
    a1 = r"012345678901234567"
    a2 = r"||      /       ||" + "\n"
    a2 += r"||     /        ||"
    return a2

def part_nose_simple():
    # Returns a simple nose /.
    a1 = r"012345678901234567"
    a2 = r"|      /         |"
    return a2

def part_nose_normal():
    # Returns a normal nose very similar to the simple one.
    a1 = "012345678901234567"
    a2 = r"        /         "
    return a2


#Mouths
def part_mouth_plane():
    #Returns a string of a closed mouth.
    a1 = r"012345678901234567"
    a2 = r"||     --       ||"
    return a2

def part_mouth_tongue():
    #Returns a string of a surprised opened mouth.
    a1 = r"012345678901234567"
    a2 = r"|      ------    |" + "\n"
    a2 += r"|        \  \    |" + "\n"
    a2 += r"|         \  \   |" + "\n"
    a2 += r"|           ---  |"
    return a2

def part_mouth_normal():
    #Returns a string of a normal mouth.
    a1 = r"012345678901234567"
    a2 = r"|     (    )     |"
    return a2

#Chins
def part_chin_plane():
    #Returns the chin of the face and the space between the faces.
    a1 = r"012345678901234567"
    a2 = r"+----------------+" + "\n"
    a2 += r"                  "
    return a2

#Helper Function
def part_selfie_band():
    # Defines the helper function that generates a band with my NetID.
    a1 = r"012345678901234567"
    a2 = r"+----------------+" + "\n"
    a2 += r"| av259    av259 |" + "\n"
    a2 += r"+----------------+"
    return a2

#Defining the faces
def bored_face():
    # Print a face that looks like so bored at a Friday night after Shooters.
    print(part_hair_wavy())
    print(part_eye_bored())
    print(part_nose_diagonal())
    print(part_mouth_plane())
    print(part_chin_plane())

def king_face():
    # Defines the king face putting all the parts to print together.
    print(part_hair_kingy())
    print(part_eye_kingsoshocked())
    print(part_nose_simple())
    print(part_mouth_tongue())
    print(part_chin_plane())

def happy_face():
    # Defines the happy face putting all the parts to print together.
    print(part_hair_normal())
    print(part_eye_normal())
    print(part_nose_normal())
    print(part_mouth_normal())
    print(part_chin_plane())

def selfie_band():
    # Defines the supportive function for selfie faces.
    print(part_selfie_band())

# Whole Face Functions With Parameters
def face_with_mouth(mouthfunc):
    # Print a face with eye and a big nose, but with a mouth specified
    # by mouthfunc.
    print(part_hair_kingy())
    print(part_eye_bored())
    print(part_nose_diagonal())
    print(mouthfunc())
    print(part_chin_plane())

def face_with_dreams(eyefunc):
    # Print a face with eye and a big nose, but with a mouth specified
    # by eyefunc.
    print(part_hair_wavy())
    print(eyefunc())
    print(part_nose_normal())
    print(part_mouth_plane())
    print(part_chin_plane())

def face_with_hairstyles(hairfunc):
    # Print a face with eye and a big nose, but with a mouth specified
    # by hairfunc.
    print(hairfunc())
    print(part_eye_bored())
    print(part_nose_diagonal())
    print(part_mouth_tongue())
    print(part_chin_plane())

#Defining the three types of function

def faces_fixed():
    # Defines the function that prints 3 faces in the console.
    bored_face()
    king_face()
    happy_face()

def faces_selfie():
    # Defines the function that prints 3 faces with a band (av259) in console.
    selfie_band()
    bored_face()
    selfie_band()
    king_face()
    selfie_band()
    happy_face()
    selfie_band()

def face_random():
    # Defines the function that prints 3 random faces in console.
    eyefunc = part_eye_bored # Eyes random.
    mouthfunc = part_mouth_tongue # Mouth random.
    hairfunc = part_hair_wavy # Hair random.
    x = random.randint(1,4)
    if x == 1:
        mouthfunc = part_mouth_plane
        eyefunc = part_eye_bored
        hairfunc = part_hair_wavy
    elif x == 2:
        mouthfunc = part_mouth_tongue
        eyefunc = part_eye_kingsoshocked
        hairfunc = part_hair_normal
    else:
        mouthfunc = part_mouth_normal
        eyefunc = part_eye_normal
        hairfunc = part_hair_wavy

    face_with_mouth(mouthfunc) # Mouth is random on this one.
    face_with_dreams(eyefunc) # Eye is random on this one.
    face_with_hairstyles(hairfunc) # Hair is random on this one.


if __name__ == '__main__':
    print("\nfixed group of three faces\n")

    faces_fixed()

    print("\ngroup of three self faces\n")

    faces_selfie()

    print("\ngroup of three random faces\n")

    faces_random()