"""from text import to_upper, to_word_list_isupper
import unittest

    




if __name__ == '__main__':
    unittest.main()"""

print("_____________________________________________________")

"""# Solution Task 1
import unittest
from text import to_upper

class TestToUpper(unittest.TestCase):
    def test_to_upper(self):
        with self.assertRaises(TypeError):
           to_upper(1)

if __name__ == '__main__':
    unittest.main()"""

# Solution Task 2
"""
import unittest
from text import to_word_list_isupper

class TestToWordListIsUpper(unittest.TestCase):
    def test_to_word_list_isupper(self):
        input_list = ['I', 'LOVE', 'YOU']
        #expected_output = True
        result = to_word_list_isupper(input_list)
        self.assertTrue(result, "Expected output does not match actual output.")

if __name__ == '__main__':
    unittest.main()"""


# Solution Task 3
"""import unittest
from text import to_word_list_isupper

class TestToWordListIsUpper(unittest.TestCase):
    def test_to_word_list_isupper(self):
        input_list = ['i', 'LOVE', 'YOU']
        #expected_output = False
        result = to_word_list_isupper(input_list)
        self.assertFalse(result, "Expected output does not match actual output.")

if __name__ == '__main__':
    unittest.main()"""


# Solution Task 4
"""import unittest
from text import to_upper

class TestToUpper(unittest.TestCase):
    def test_to_upper_type_error(self):
        with self.assertRaises(TypeError):
            to_upper(123)

if __name__ == '__main__':
    unittest.main()"""

# Solution Task 5

## Task5

import unittest
from text import to_word_list_isupper

class TestToWordListIsUpper(unittest.TestCase):
    def test_to_word_list_isupper_type_error(self):
        with self.assertRaises(TypeError) as context:
            to_word_list_isupper("hello")
        self.assertEqual(str(context.exception), "'str' object is not iterable")

        with self.assertRaises(TypeError) as context:
            to_word_list_isupper(123)
        self.assertEqual(str(context.exception), "'int' object is not iterable")

if __name__ == '__main__':
    unittest.main()


