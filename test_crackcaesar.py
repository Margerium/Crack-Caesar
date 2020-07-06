import unittest

from crackcaesar import is_dict_file_valid
from crackcaesar import cipher
from crackcaesar import cracker

default_dictionary = ["that", "with", "they", "this", "have", "from", "word", "what", "were", "when", "your",
                      "said", "there", "each", "which", "their", "will", "other", "about", "many", "then", "them",
                      "these", "some", "would", "make", "like", "into", "time", "look", "more", "write", "number",
                      "could"]

empty_dictionary = []

bool_dictionary = [True, False]

int_dictionary = [1, 2, 3]

float_dictionary = [0.1, 0.2, 0.3]


class IsDictFileValidTestCase(unittest.TestCase):

    def test_cipher_type(self):

        result = is_dict_file_valid("caesarcipher", "dict", default_dictionary)
        self.assertEqual(result, True)

        result = is_dict_file_valid("", "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid(bool, "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid(True, "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid(False, "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid(int, "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid(-1, "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid(535325324124312542, "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid(float, "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid(0.432562532, "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid(str, "dict", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("a random string", "dict", default_dictionary)
        self.assertEqual(result, False)

    def test_file_type(self):

        result = is_dict_file_valid("caesarcipher", "dict", default_dictionary)
        self.assertEqual(result, True)

        result = is_dict_file_valid("caesarcipher", "", default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", bool, default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", True, default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", False, default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", int, default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", -1, default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", 535325324124312542, default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", float, default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", 0.432562532, default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", str, default_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "a random string", default_dictionary)
        self.assertEqual(result, False)

    def test_dictionary(self):

        result = is_dict_file_valid("caesarcipher", "dict", default_dictionary)
        self.assertEqual(result, True)

        result = is_dict_file_valid("caesarcipher", "dict", "")
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", bool)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", True)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", False)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", int)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", -1)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", 535325324124312542)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", float)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", 0.432562532)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", str)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", "a random string")
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", empty_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", bool_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", int_dictionary)
        self.assertEqual(result, False)

        result = is_dict_file_valid("caesarcipher", "dict", float_dictionary)
        self.assertEqual(result, False)


