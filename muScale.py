import random

def get_key():
    '''Prompt user for root, convert to upper case if it is lower'''

    print("What is the root key? E.g: A, g")
    input_key = input("> ")
    if input_key.islower() == True:
        print("Key input was lower case, making upper")
        input_key = input_key.upper()
    return input_key

def get_scale():
    '''Prompt user for scale'''
    
    print("Scale? 1 - Minor, 2 - Major")
    input_scale = input("> ")

    #if type(input_scale) is not int:
    #    print("Please enter a number")
    #    get_scale()
    #else:
    #    pass
    return int(input_scale)

octave = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def minor(root, octave):
    ''' Returns minor scale based on input'''

    output = []

    minor_scale = [2, 1, 2, 2, 1, 2, 2]
    start = octave.index(root)
    print(f"Start key number is {start}")
    output.append(root)

    for step in minor_scale:

        #if step == 0:
            #output.append(root)
        #    pass

        start += step

        # If start > 11 then it will be out of bounds...
        if start  > 11:
            print(f"Start was larger than 11 at {start}, reducing by 11")
            start -= start
            print(f"Value of start after subtraction is {start} Note {octave[start]}")
            output.append(octave[start])
            continue
        else:
            output.append(octave[start])
            continue
    
    return output

def major(root, octave):
    ''' Input root note and the octave, spit out major scale'''

    output = []
    major_scale = [2, 2, 1, 2, 2, 2, 1]
    start = octave.index(root)
    output.append(root)

    for step in major_scale:

        start += step

        # If start > 11 then it will be out of bounds...
        if start  > 11:
            print(f"Start was larger than 11 at {start}, reducing by {start}")
            start -= 12
            #print(f"Value of start after subtraction is {start} Note {octave[start]}")
            output.append(octave[start])
            continue

        # Otherwise values is within bounds, get the note at the positon of start in octave[]
        else:
            output.append(octave[start])
            continue
    
    return output

x = get_key()
y = get_scale()

if y == 1:
    print(minor(x, octave))
elif y == 2:
    print(major(x, octave))