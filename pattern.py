#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

class pattern():
    """
    For the password pattern
    Length
    numbers
    Capital Letters
    """
    all_specials="#$%&\'()*+,-./:;?@[\\]^_`{|}~"
    capital=False
    numbers=False
    min_length=8
    max_length=8
    special_characters = False
    specialCh_list = []
