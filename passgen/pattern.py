#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

from enum import Enum

class pattern():
    """
    For the password pattern
    Length
    numbers
    Capital Letters
    """
    all_specials="# $ % & \ ' ( ) * + , - . / : ; ? @ [ \ \ ] ^ _ ` { | } ~ "
    capital=None
    numbers=None
    min_length=8
    max_length=8
    special_characters = None
    specialCh_list = []


class pattern_Status(Enum):
    """
    Specifies if pattern Settings is
    [forced to be right
    [optional
    [forbidden to be
    """
    musthave = 1
    optional = 2
    forbidden = 3
