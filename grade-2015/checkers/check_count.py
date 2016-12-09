# coding=UTF-8

import utilities
import os

os.chdir(os.path.dirname(__file__))
utilities.check_script('count.py', '../data/gulliver.txt')
