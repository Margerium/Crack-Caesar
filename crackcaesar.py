# Program to crack a Caesar Cipher and return the shift used in the input file to the user

import time
import argparse
import json

# the argparse arguments that give this program commandline functionality
parser = argparse.ArgumentParser()
parser.add_argument("-i", type=str, required=True, help="Provide a name for your input file")
parser.add_argument("-d", type=str, required=False, help="Provide a dictionary to be used,"
                                                         " file should be of form .dict and contain json data")
parser.add_argument("-n", type=int, required=False, help="Sets how many characters shall be read")
args = parser.parse_args()

# assigns the -i argument to the input file name: -i "my_input.txt" will assign "my_input.txt" as the input file name
input_file_name = args.i

# json object assigned as None type, this will change below if the -d argument is used
json_object = None

# if the -d argument is used, then the user is trying to assign their own dictionary
if isinstance(args.d, str):

    # opens the users .dict file, and loads the json objects that should be inside, then closes the .dict file
    dict_file_name = args.d
    dict_file = open(dict_file_name, "r", encoding="utf8")
    json_object = json.load(dict_file)
    dict_file.close()

# opens the input file, assigns it to a variable and then closes the input file
input_file = open(input_file_name, "r", encoding="utf8")
input_text = input_file.read()
input_file.close()

# if the user used the -n argument, assigns the integer value of this argument below to limit the number of characters
# the program will read
if isinstance(args.n, int):
    number_of_characters_to_read = args.n
    input_text = input_text[:number_of_characters_to_read]

# takes the input text and puts all of it in lower case since all dictionary words should be in lower case
input_text = input_text.lower()

# splits the input text at every space, this turns the input text into a list[str] type and allows each entry in that
# list to checked against each entry in the dictionary for exact matches
input_text = input_text.split()


def is_dict_file_valid(cipher_type, file_type, dictionary):
    """Function that checks the validity of the '.dict' json file

    :param cipher_type: Checks the json object 'ciphertype' for 'caesarcipher' as this is the only valid input
    :type cipher_type: str

    :param file_type: Checks the json object 'filetype' for 'dict' as this is the only valid input
    :type file_type: str

    :param dictionary: Checks that the dictionary has at least 1 entry
    :type dictionary: list

    """

    if cipher_type != "caesarcipher":
        print("\nInvalid cipher type, expecting 'caesarcipher', please check your .dict file!")
        return False

    elif file_type != "dict":
        print("\nInvalid file type, expecting 'dict', please check your .dict file!")
        return False

    elif not isinstance(dictionary, list):
        print("\n Your dictionary is invalid, please check your .dict file!")
        return False

    elif len(dictionary) == 0:
        print("\nYour dictionary does not contain any entries, please check your .dict file!")
        return False

    else:
        for word in dictionary:
            if not isinstance(word, str):
                print("\nYour dictionary does not contain words or has non-word entries, please check your .dict file!")
                return False

        else:
            print("\n Dictionary is valid!")
            return True


def cipher(text):
    """This function will encode/decode your input text and return the output. It is the same function from caesar.py
    simplified for the purpose of encoding the dictionary in the cracker function. As such the input text will always be
    the individual words from the dictionary, the shift will always be 1 and this function will always be encoding lower
    case letters only.

    :param text: Takes the input text provided and shifts each letter one place to the right (encoding only).
    In this simplified function, the input text will always be a lower case word taken from the dictionary in the
    cracker function below.
    :type text: str
    """

    if not isinstance(text, str):
        return "Expecting input to be a string of text, please check your input file!"

    # the encoded output, starts as an empty string
    translated = ""

    # for each character, including punctuation, in the text provided to this function
    for character in text:

        # if the character is a letter in A - Z
        if character.isalpha():

            # converts the character to its ASCII value
            num = ord(character)

            # adds the shift to this character (always 1 in this case as that is all we need this function to do)
            num = num + 1

            # these make sure the shifted character remain in A - Z
            if num > ord("z"):
                num = num - 26

            elif num < ord("a"):
                num = num + 26

            # the encoded character is now added to the output of this function
            translated = translated + chr(num)

        else:
            # characters that were outside A - Z (not .isalpha) are immediately added to the output
            translated = translated + character

            # finally, the output of this function is returned - in this case, the dictionary below in the cracker
            # function with each character in each word shifted 1 to the right
    return translated


def cracker(text, dictionary):
    """This function will attempt to work out the shift used to encode your input text - assuming it was done with a
    caesar cipher.

    :param text: Takes your input text and by using a dictionary of common english words and shifting them using a
    caesar cipher up to a shift value of 25 (all useful possible encoding values), attempts to find word matches in
    your text with the dictionary, the shift with the highest number of matches will be returned. If no matches are
    found, "FAIL" will be returned
    :type text: list[str]

    :param dictionary: The dictionary of words, this is checked against words in the input text for matches.
    The dictionary will be taken from a default dictionary unless the user provides their own via a .dict file using the
    -d command
    :type dictionary
    """

    # when using a dictionary of un-coded words, the starting shift will be 0
    shift = 0

    # stores the time at the start of this function into a variable
    start_time = time.time()

    # lets the user know the program is working and performing operations on their input
    print("\n Your file is being processed, please wait.")

    # lists to store the shift value and the number of occurrences found with that shift
    shift_list = [0]
    occurrences_list = [0]

    # program checks for shifts between 0 and 25, a shift of 26 would be the equivalent of a shift of 0
    while shift < 26:

        # for each shift, the number of occurrences at the start of the check should be set to 0
        # to prevent false positives
        occurrences = 0

        # each word in the input text is checked for matches against each word in the dictionary used,
        # if a match is found the number of occurrences is iterated
        for word_in_text in text:
            for word in dictionary:
                if word_in_text == word:
                    occurrences = occurrences + 1

        # if occurrences are found and the number of occurrences for the current shift being checked is greater than
        # the number of occurrences found for a previous shift, the values contained in the lists are updated
        # this means that the shift returned at the end of this function is the shift with the most occurrences found
        if occurrences > (occurrences_list[0]):
            occurrences_list.pop(0)
            occurrences_list.append(occurrences)
            shift_list.pop(0)
            shift_list.append(shift)

        # once the check for a shift has been completed, the shift is iterated up and the dictionary used is
        # encoded to be used to check for the next shift
        shift = shift + 1
        for i in range(0, len(dictionary)):
            dictionary[i] = cipher(dictionary[i])

    # once all shifts are checked, the shift value stored in the shift list is used as the output for this function
    output = shift_list[0]
    shift = int(output)

    # assuming the above shift had match occurrences then the operation is assumed successful,
    # this shift value is then returned as the console output
    if occurrences_list[0] > 0:
        print("\nThe operation took %s seconds to perform" % (time.time() - start_time))
        return shift

    # if there were no matches found between the text and dictionary, FAIL is returned
    else:
        print("\nThe operation took %s seconds to perform" % (time.time() - start_time))
        return "FAIL"


# if the -d argument was used
if isinstance(args.d, str):

    # runs the function below that checks the provided .dict file is valid
    if is_dict_file_valid(json_object["ciphertype"], json_object["filetype"], json_object["dictionary"]):

        # if the .dict file is valid, attempts to crack using the dictionary provided
        print("\n", cracker(input_text, json_object["dictionary"]))

else:
    # if no .dict file was used, the program attempts to crack using the default dictionary defined below
    default_dictionary = ["that", "with", "they", "this", "have", "from", "word", "what", "were", "when", "your",
                          "said", "there", "each", "which", "their", "will", "other", "about", "many", "then", "them",
                          "these", "some", "would", "make", "like", "into", "time", "look", "more", "write", "number",
                          "could"]

    print("\n", cracker(input_text, default_dictionary))
