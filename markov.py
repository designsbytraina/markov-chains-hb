"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    words.append(None)

    for idx in range(len(words) - 2):
        if words[idx+1]:
            tuple_key = tuple([words[idx], words[idx+1]])
        else:
            break

        if tuple_key not in chains:
            chains[tuple_key] = [words[idx+2]]
        else:
            chains[tuple_key].append(words[idx+2])

        # chains.get(tuple_key, []) + [words[idx+2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    markov_key = choice(list(chains.keys()))

    while True:
        words.append(markov_key[0])
        if markov_key[1]:
            markov_key = tuple([markov_key[1], choice(chains[markov_key])])
        else:
            break

    return " ".join(words)


# Add ability to pass in a different corpus
try:
    input_path = sys.argv[1]
except:
    input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
