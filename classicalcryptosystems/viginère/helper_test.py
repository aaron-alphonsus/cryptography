from __future__ import absolute_import
import unittest

class TestFrequencyFunction(unittest.TestCase):

    def test_correctcount(self):
        """
        Simple test to calculate frequency of characters in a word

        :return: None
        """
        from helper import frequency
        actual = frequency("cryptography")
        expected = {'c': 1, 'r': 2, 'y': 2, 'p': 2, 't': 1, 'o': 1, 'g': 1,
                    'a': 1, 'h': 1}
        self.assertDictEqual(expected, actual, msg=None)


# text = "VVHQWVVRHMUSGJGTHKIHTSSEJCHLSFCBGVWCRLRYQTFSVGAHWKCUHWAUGLQHNSLRLJSH" \
#        "BLTSPISPRDXLJSVEEGHLQWKASSKUWEPWQTWVSPGOELKCQYFNSVWLJSNIQKGNRGYBWLWG" \
#        "OVIOKHKAZKQKXZGYHCECMEIUJOQKWFWVEFQHKIJRCLRLKBIENQFRJLJSDHGRHLSFQTWL" \
#        "AUQRHWDMWLGUSGIKKFLRYVCWVSPGPMLKASSJVOQXEGGVEYGGZMLJCXXLJSVPAIVWIKVR" \
#        "DRYGFRJLJSLVEGGVEYGGEIAPUUISFPBTGNWWMUCZRVTWGLRWUGUMNCZVILE,':',"

if __name__ == '__main__':
    unittest.main()
