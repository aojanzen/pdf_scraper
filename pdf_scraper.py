#!/usr/bin/env python3

"""
==============
pdf_scraper.py
==============

Author : Dr. Andreas Janzen
Email  : janzen (at) gmx (dot) net
Date   : 2021-05-15
Version: V0.1

Scrape all pdf documents in the current folder and all sub-folders, extract the
text from these files, remove all punctuation and numbers, and then count the
remaining words in the text to identify the most frequently used characteristic
words in the document. These words will be stored (e.g. in an SQLite database)
so that -- finally -- pdf files with similar content can be identified
automatically.

The motivation for this app is the vast number of scientific publications that
I have gathered at work and which have now become too many to sort them by
hand.
"""

import os
import PyPDF2
import sys

from collections import Counter
from string import ascii_letters, digits, punctuation


STOP_WORDS_ENGLISH = "./stop_words/stop_words_english.txt"
STOP_WORDS_GERMAN  = "./stop_words/stop_words_german.txt"


def get_pdf_filenames(directory):
    """ TO DO: write docstring
    """
    files = list()
    dirlist = [directory]

    while len(dirlist) > 0:
        for (dirpath, dirnames, filenames) in os.walk(dirlist.pop()):
            dirlist.extend(dirnames)
            files.extend(map(lambda n: os.path.join(*n), zip([dirpath] *
                len(filenames), filenames)))

    pdf_files = [file for file in files if file.endswith(".pdf")]

    print("Found the following pdf files:\n")
    for file in pdf_files:
        print(f"\t{file}")

    return pdf_files


def get_keywords(text):
    """ TO DO: write docstring
    """
    return keywords


def write_keyword_table():
    """ TO DO: write docstring
    """
    pass


# Program starts here
def main():
    if len(sys.argv) == 2:
        directory = sys.argv[1]
        get_pdf_filenames(directory)
    else:
        print("\nUSAGE: pdf_scraper <path>")

    sys.exit()


if __name__ == "__main__":
    main()
