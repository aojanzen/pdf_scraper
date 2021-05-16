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

from collections import Counter
from string import ascii_letters, whitespace # digits, punctuation

import os
import sys

import PyPDF2


KEYWORD_NUMBER = 20
ALLOWED_CHARS = set(ascii_letters).union(set(whitespace))

STOP_WORDS = "./stop_words/stop_words_english.txt"
# STOP_WORDS = "./stop_words/stop_words_german.txt"


def make_full_path(root, extensions):
    """ TO DO: write docstring
    """
    return [os.path.join(root, ext) for ext in extensions]


def get_pdf_filenames(directory):
    """ TO DO: write docstring
    """
    pdf_files = list()

    for (dirpath, _, filenames) in os.walk(directory):
        filenames = [f for f in filenames if f.endswith(".pdf")]
        pdf_files.extend(make_full_path(dirpath, filenames))

    return pdf_files


def get_text_from_pdf(filepath):
    """ TO DO: write docstring
    """
    text = ""

    with open(filepath, "rb") as pdf_file_obj:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        for page in range(pdf_reader.numPages):
            page_obj = pdf_reader.getPage(page)
            text = " ".join([text, page_obj.extractText()])

    remove_chars = set(list(text)).difference(ALLOWED_CHARS)
    for char in remove_chars:
        text = text.replace(char, " ")

    return text


def remove_stop_words(word_list):
    """ TO DO: write docstring
    """
    with open(STOP_WORDS, "r") as f_in:
        stop_words = f_in.read().split("\n")

    word_list = [word for word in word_list if word not in stop_words]

    return word_list


def find_keywords(text):
    """ TO DO: write docstring
    """
    word_list = [word.lower() for word in text.split()]

    word_list = remove_stop_words(word_list)
    text_count = Counter(word_list)

    return text_count.most_common(KEYWORD_NUMBER)


def print_keyword_table(summary):
    """ TO DO: write docstring
    """
    print(f"\nSummary for {len(summary)} analyzed files:")
    for filename in summary.keys():
        print(f"\n...{filename[-45:]}:")
        print([word for (word, _) in summary[filename]])
    print()

    return None


def main():
    """ TO DO: write docstring
    """
    if len(sys.argv) == 2:
        directory = sys.argv[1]
    else:
        print("\nUSAGE: pdf_scraper <path>")
        sys.exit()

    keyword_summary = dict()

    pdf_files = get_pdf_filenames(directory)
    print(f"\n\nFound {len(pdf_files)} pdf files for further processing.")

    for filepath in pdf_files:
        text = get_text_from_pdf(filepath)
        result = find_keywords(text)

        if not result:
            print(f"\nCould not read text from file {filepath}.")
            continue

        keyword_summary[filepath] = result

    print_keyword_table(keyword_summary)


if __name__ == "__main__":
    main()

