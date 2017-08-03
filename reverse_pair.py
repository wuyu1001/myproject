from __future__ import print_function, division

from inlist import in_bisect_cheat, make_word_list

def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect_cheat(word_list, rev_word)

if __name__ == '__main__':
    word_list = make_word_list()

    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])



